import sys
import traceback # For detailed error reporting
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtCore import QObject, Signal, Slot, QThread # Qt threading and signals/slots

# Import your generated UI class and other necessary components
from BLDC_UI import Ui_MainWindow
from pint import UnitRegistry
from pymoo.core.variable import Real, Integer, Choice, Binary
from pymoo.core.callback import Callback # Import Callback base class
from UI_MotorOptimizer import MotorOpt # Your optimization function
from UI_MotorModel import MotorCalcs_Vectorized # Your calculation function
import matlab.engine


# PyMoo progress bar callback (emit signals to QT worker)
class ProgressCallback(Callback):
    def __init__(self, progress_signal: Signal, total_gens: int):
        super().__init__()
        self.progress_signal = progress_signal # Signal to emit progress
        self.total_gens = total_gens           # Total generations for percentage (optional)
        # print(f"ProgressCallback initialized. Total generations: {self.total_gens}") 

    def update(self, algorithm):
        current_gen = algorithm.n_gen
        # print(f"Callback Update: Gen {current_gen}") 
        if self.progress_signal:
            self.progress_signal.emit(current_gen)


# QT worker (threaded signal reveicver -> updates progress bar)
class OptimizationWorker(QObject):
    progress_signal = Signal(int)
    finished_signal = Signal(object)
    error_signal = Signal(str)

    def __init__(self, motor_calcs_func, motor_params_pymoo, opt_conf, other_args):
        super().__init__()
        self.motor_calcs_func = motor_calcs_func
        self.motor_params_pymoo = motor_params_pymoo # Now expects pymoo Real/Integer objects
        self.opt_conf = opt_conf
        self.other_args = other_args # Tuple: (mag_br, max_b_mag, pres_b_lam, eng, Real, Integer, Choice, Binary)
        self.ngens = opt_conf.get("ngens", 0)

    @Slot()
    def run_optimization(self):
        try:
            print("Worker thread starting optimization...")
            callback = ProgressCallback(self.progress_signal, self.ngens)
            mag_br, max_b_mag, pres_b_lam, eng, R, I, Ch, B = self.other_args # Unpack

            # Call MotorOpt with parameters already containing Pymoo variables
            results = MotorOpt(
                self.motor_calcs_func,
                self.motor_params_pymoo, # Pass the dict with Pymoo objects
                mag_br, max_b_mag, pres_b_lam,
                eng, R, I, Ch, B, # Pass engine and types
                self.opt_conf,
                callback_instance=callback
            )
            print("Worker thread finished optimization.")
            self.finished_signal.emit(results)

        except Exception as e:
            print(f"Error in worker thread: {e}")
            detailed_error = traceback.format_exc()
            self.error_signal.emit(f"Optimization failed: {e}\n---\n{detailed_error}")


# QT User Interface
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Attributes for Threading ---
        self.optimization_thread = None
        self.optimization_worker = None

        # --- Other Setup ---
        self.ureg = UnitRegistry() # Keep Pint if used elsewhere
        # Start MATLAB engine once
        try:
             print("Starting MATLAB engine...")
             self.matlab_engine = matlab.engine.start_matlab()
             print("MATLAB engine started.")
        except Exception as e:
             QMessageBox.critical(self, "MATLAB Error", f"Could not start MATLAB engine: {e}")
             self.matlab_engine = None
             # Consider disabling optimization button if engine fails
             self.ui.Execution.setEnabled(False)

        # --- Connect UI Signals ---
        # Connect the Execution button to the NEW slot that handles threading
        self.ui.Execution.clicked.connect(self.start_optimization)
        # Connect material dropdowns to update derived values immediately (optional but good practice)
        self.ui.Magnet_Material.currentIndexChanged.connect(self.update_magnet_br)
        self.ui.Iron_Material.currentIndexChanged.connect(self.update_max_b_magnet_iron)
        self.ui.Lamination_Material.currentIndexChanged.connect(self.update_present_b_lamination)

        # Initialize derived material properties
        self.MagnetBr_T = 0.0
        self.MaxBMagnetIron_T = 0.0
        self.PresentBLaminationBackIron_T = 0.0
        self.update_magnet_br()
        self.update_max_b_magnet_iron()
        self.update_present_b_lamination()


    @Slot()
    def start_optimization(self):
        """Configures and starts the optimization in a separate thread."""
        if not self.matlab_engine:
             QMessageBox.critical(self, "Error", "MATLAB engine is not running. Cannot start optimization.")
             return

        if self.optimization_thread and self.optimization_thread.isRunning():
            QMessageBox.warning(self, "Busy", "Optimization is already running.")
            return

        # --- 1. Gather Parameters, Configuration, and Create Pymoo Variables ---
        try:
            parameters_pymoo = self._create_pymoo_parameters_from_ui()
            optimization_conf = self._read_opt_config_from_ui()
            other_opt_args = self._get_other_opt_args()
        except ValueError as e:
             QMessageBox.warning(self, "Input Error", f"Error reading inputs: {e}")
             return
        except AttributeError as e:
             QMessageBox.warning(self, "Input Error", f"Error accessing UI element (check names): {e}")
             return

        # --- 2. Configure Progress Bar ---
        ngens = optimization_conf.get("ngens", 1)
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(ngens)
        self.ui.progressBar.setValue(0)
        self.ui.Execution.setEnabled(False)
        print(f"Starting optimization with {ngens} generations.")

        # --- 3. Create Worker and Thread ---
        self.optimization_worker = OptimizationWorker(
            MotorCalcs_Vectorized,    # Pass the actual calculation function
            parameters_pymoo,         # Pass the dict with Pymoo variables
            optimization_conf,        # Pass the config dict
            other_opt_args            # Pass the tuple of other args
        )
        self.optimization_thread = QThread()
        self.optimization_worker.moveToThread(self.optimization_thread)

        # --- 4. Connect Worker Signals to GUI Slots ---
        self.optimization_thread.started.connect(self.optimization_worker.run_optimization)
        self.optimization_worker.progress_signal.connect(self.update_progress)
        self.optimization_worker.finished_signal.connect(self.on_optimization_finished)
        self.optimization_worker.error_signal.connect(self.on_optimization_error)

        # --- 5. Connect Cleanup Signals ---
        self.optimization_worker.finished_signal.connect(self.optimization_thread.quit)
        self.optimization_worker.error_signal.connect(self.optimization_thread.quit)
        self.optimization_worker.finished_signal.connect(self.optimization_worker.deleteLater)
        self.optimization_thread.finished.connect(self.optimization_thread.deleteLater)
        self.optimization_thread.finished.connect(lambda: self.ui.Execution.setEnabled(True))

        # --- 6. Start the Thread ---
        self.optimization_thread.start()

    # --- Slots for Handling Worker Signals ---
    @Slot(int)
    def update_progress(self, current_generation):
        """Slot to update the progress bar."""
        self.ui.progressBar.setValue(current_generation)

    @Slot(object)
    def on_optimization_finished(self, results):
        """Slot called when optimization completes successfully."""
        print("Optimization finished successfully. Results received in GUI.")
        self.ui.progressBar.setValue(self.ui.progressBar.maximum())

        if results.F is None:
             QMessageBox.information(self, "Result", "Optimization finished, but no feasible solution was found.")
        else:
             QMessageBox.information(self, "Result", f"Optimization finished. Found {len(results.F)} solution(s).")
             # TODO: Add code here to process 'results' and update Tab 3
             # self.display_results_on_tab3(results)

        self.optimization_thread = None
        self.optimization_worker = None
        # Button re-enabled via thread.finished signal

    @Slot(str)
    def on_optimization_error(self, error_message):
        """Slot called if an error occurs during optimization."""
        print(f"Optimization error received in GUI: {error_message}")
        QMessageBox.critical(self, "Optimization Error", error_message)
        self.ui.progressBar.setValue(0)
        self.optimization_thread = None
        self.optimization_worker = None
        # Button re-enabled via thread.finished signal


    # --- Helper Methods to Read UI ---
    def _create_pymoo_parameters_from_ui(self):
        """Reads Tab 1, creates pymoo variables, returns params dict."""
        parameters = {}
        # List of variable base names expected in the UI (Tab 1)
        # Assumes UI elements are named like 'VarName_1', 'VarName_2', etc.
        var_base_names = [
            'I_PolePair', 'R_MagnetRadialLength', 'R_MagnetOutR', 'R_MagnetBackIronInnerR',
            'R_MagneticLossCoef1', 'R_MagneticLossCoef2', 'R_MagneticLossCoef3',
            'I_NumElecPhase', 'R_PhaseCurrentAmp', 'R_WireCopperR', 'R_InsulThick',
            'R_FillFactor', 'R_LaminatToothWedgeThickness', 'R_LaminatR',
            'R_LamSlotLinerThick', 'R_LoadInertia', 'R_GearRatio', 'R_MtrLength',
            'R_FluidSpecificGrav', 'R_FluidKinVisc', 'R_AirgapRadialLength',
            'R_VacMagneticPerm'
        ]

        for base_name in var_base_names:
            try:
                widget1 = getattr(self.ui, base_name + '_1')
                widget2 = getattr(self.ui, base_name + '_2', None) # _2 might not exist for fixed values

                val1 = widget1.value()
                bounds = (val1, widget2.value() if widget2 else val1) # Use val1 if widget2 doesn't exist

                # Create Pymoo variable based on type prefix (I_ for Integer, R_ for Real)
                if base_name.startswith('I_'):
                    # Ensure bounds are integers for Integer type
                    int_bounds = (int(bounds[0]), int(bounds[1]))
                    parameters[base_name] = Integer(bounds=int_bounds)
                elif base_name.startswith('R_'):
                     # Ensure bounds are floats for Real type
                     float_bounds = (float(bounds[0]), float(bounds[1]))
                     parameters[base_name] = Real(bounds=float_bounds)
                else:
                     # Handle other types or fixed values if needed (e.g., Choice, Binary)
                     # For now, assume fixed values are handled elsewhere or passed directly
                     pass
            except AttributeError:
                 print(f"Warning: UI elements for '{base_name}' not found or incomplete. Skipping.")
            except Exception as e:
                 raise ValueError(f"Error processing UI variable '{base_name}': {e}")

        # Add material choices if they are optimization variables (using Choice)
        # Example: parameters['Magnet_Material'] = Choice(options=["Recoma 18", "Recoma 20", ...])
        # Currently, materials seem fixed based on dropdowns, handled in _get_other_opt_args
        # If they *become* optimization variables, add them here using Choice.

        return parameters

    def _read_opt_config_from_ui(self):
         """Reads Tab 2 configuration."""
         conf = {}
         try:
            # Optimizer settings
            conf['npop'] = self.ui.npop.value()
            conf['ngens'] = self.ui.ngens.value()
            conf['nprocesses'] = self.ui.nprocesses.value()
            conf['DisMut'] = self.ui.DisMut.value()
            conf['ProbMut'] = self.ui.ProbMut.value()

            # Performance Requirements (Constraints) - TODO: Add unit handling if needed
            conf['SpeedReq'] = self.ui.SpeedReq.text()
            conf['MinTor'] = self.ui.MinTor.text()
            conf['MinEff_'] = self.ui.MinEff_.value()
            conf['MaxWeight'] = self.ui.MaxWeight.value() # Assuming kg from UI default
            conf['VDC'] = self.ui.VDC.value()

            # Objectives to Optimize
            conf['TorqueOpt'] = self.ui.TorqueOpt.isChecked()
            conf['EfficinecyOpt_min'] = self.ui.EfficinecyOpt_min.isChecked()
            conf['EfficinecyOpt_max'] = self.ui.EfficinecyOpt_max.isChecked()
            conf['WeightOpt'] = self.ui.WeightOpt.isChecked()
            conf['MagWeightOpt'] = self.ui.MagWeightOpt.isChecked()
            conf['VoltageOpt'] = self.ui.VoltageOpt.isChecked()
            conf['MtrLengthOpt'] = self.ui.MtrLengthOpt.isChecked()
            conf['MtrRadiusOpt'] = self.ui.MtrRadiusOpt.isChecked()

            if not any(v for k, v in conf.items() if k.endswith('Opt')):
                 raise ValueError("No optimization objectives selected in Tab 2!")

         except Exception as e:
             raise ValueError(f"Error reading configuration from Tab 2: {e}")
         return conf

    def _get_other_opt_args(self):
         """Gets fixed args: material props, engine, pymoo types."""
         # Ensure current material properties are up-to-date
         self.update_magnet_br()
         self.update_max_b_magnet_iron()
         self.update_present_b_lamination()

         if not self.matlab_engine:
             raise ValueError("MATLAB Engine not available!")

         # Return tuple expected by the worker
         return (self.MagnetBr_T, self.MaxBMagnetIron_T, self.PresentBLaminationBackIron_T,
                 self.matlab_engine, Real, Integer, Choice, Binary)

    def update_magnet_br(self):
        magnet_br_values = {
            "Recoma 18": 0.87, "Recoma 20": 0.90, "Recoma 22": 0.94, "Recoma 25": 1.00,
            "Recoma 24HE": 1.02, "Recoma 26": 1.04, "Recoma 26HE": 1.07, "Recoma 28": 1.10,
            "Recoma 28HE": 1.10, "Recoma 30": 1.12, "Recoma 30HE": 1.12, "Recoma 30S": 1.12,
            "Recoma 32": 1.15, "Recoma 32S": 1.15, "Recoma 33E": 1.16, "Recoma 35E": 1.19,
        }
        selected_material = self.ui.Magnet_Material.currentText()
        self.MagnetBr_T = magnet_br_values.get(selected_material, 1.1) # Default if needed
        # print(f"Updated MagnetBr_T: {self.MagnetBr_T}") 

    def update_max_b_magnet_iron(self):
        selected_option = self.ui.Iron_Material.currentText()
        iron_br_values = {
            "430 Stainless Steel": 1.3, "1215 Steel": 1.5, "1018 Steel": 1.4,
            "1008 Steel": 1.4, "1010 Steel": 1.4, "Hiperco 50": 2.0, "M19": 1.75,
        }
        self.MaxBMagnetIron_T = iron_br_values.get(selected_option, 1.5)
        # print(f"Updated MaxBMagnetIron_T: {self.MaxBMagnetIron_T}")

    def update_present_b_lamination(self):
        selected_option = self.ui.Lamination_Material.currentText()
        lamination_br_values = {"M19": 1.75, "Hiperco 50": 2.3,}
        self.PresentBLaminationBackIron_T = lamination_br_values.get(selected_option, 1.75)
        # print(f"Updated PresentBLaminationBackIron_T: {self.PresentBLaminationBackIron_T}")

    def get_unit(self, variable_name):
        """Return the unit corresponding to the variable name."""
        # Mapping of variable names to units
        unit_map = {
            'R_MagnetRadialLength': 'meter',  # Example: replace with actual units
            'R_MagnetOutR': 'meter',
            'R_MagnetBackIronInnerR': 'meter',
            'R_MagneticLossCoef1': '1',  # Dimensionless
            'R_MagneticLossCoef2': '1',
            'R_MagneticLossCoef3': '1',
            'R_PhaseCurrentAmp': 'ampere',
            'R_WireCopperR': 'meter',
            'R_InsulThick': 'meter',
            'R_FillFactor': '1',  # Dimensionless
            'R_LaminatToothWedgeThickness': 'meter',
            'R_LaminatR': 'meter',
            'R_LoadInertia': 'kg*m^2',
            'R_GearRatio': '1',  # Dimensionless
            'R_MtrLength': 'meter',
            'R_FluidSpecificGrav': '1',  # Dimensionless
            'R_FluidKinVisc': 'cSt',
            'R_AirgapRadialLength': 'meter',
            'R_VacMagneticPerm': 'H/m',
        }
        return unit_map.get(variable_name, 'meter')

    def closeEvent(self, event):
        """Ensure MATLAB engine is stopped when closing the window."""
        if self.matlab_engine:
            print("Stopping MATLAB engine...")
            try:
                self.matlab_engine.quit()
                print("MATLAB engine stopped.")
            except Exception as e:
                print(f"Error stopping MATLAB engine: {e}")
        event.accept() # Accept the close event


# --- Main Execution Block ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())