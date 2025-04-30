# Python Modules
import sys
import json      # For saving/loading UI values from file
import traceback # For detailed error reporting
from pint import UnitRegistry # For unit conversion
import matlab.engine

# User Interface Libraries / Pymoo
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QSpinBox
from PySide2.QtWidgets import QDoubleSpinBox, QComboBox, QLineEdit, QCheckBox, QWidget
from PySide2.QtCore import QObject, Signal, Slot, QThread, Qt
from pymoo.core.variable import Real, Integer, Choice, Binary
from pymoo.core.callback import Callback

# Project Imports
from UI_MotorOptimizer import MotorOpt 
from UI_MotorModel import MotorCalcs_Vectorized
from BLDC_UI import Ui_MainWindow

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


# QT worker (threaded signal receiver -> updates progress bar)
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
        # --- Initialize GUI ---
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Intitialize Worker (dedicated thread for progress bar) ---
        self.optimization_thread = None
        self.optimization_worker = None

        # --- Initialize Pint (unit conversion module) ---
        self.ureg = UnitRegistry()

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


    # --- Save/Load UI State ---
    @Slot()
    def on_actionSave_triggered(self):
        """Saves the current values of all relevant UI fields to a JSON file."""
        print("Save action triggered!")
        options = QFileDialog.Options()
        # Suggest JSON file type
        fileName, _ = QFileDialog.getSaveFileName(self, "Save UI State", "", 
                                                  "JSON Files (*.json);;All Files (*)", options=options)
        
        if not fileName:
            print("Save cancelled.")
            return

        # Ensure the filename ends with .json
        if not fileName.lower().endswith('.json'):
            fileName += '.json'
        
        print(f"Attempting to save UI state to: {fileName}")

        ui_state = {}
        try:
            # Find all relevant input widgets within the central widget (or main window)
            # Adjust the list of types if you have other input widgets
            all_widgets = self.findChildren(QWidget) 
            widgets_to_save = [w for w in all_widgets if isinstance(w, (QSpinBox, QDoubleSpinBox, QComboBox, QLineEdit, QCheckBox))]

            for widget in widgets_to_save:
                object_name = widget.objectName()
                if not object_name: # Skip widgets without an object name
                    print(f"Warning: Skipping widget of type {type(widget)} because it has no object name.")
                    continue

                value = None
                if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                    value = widget.value()
                elif isinstance(widget, QComboBox):
                    value = widget.currentText() # Save the selected text
                elif isinstance(widget, QLineEdit):
                    value = widget.text()
                elif isinstance(widget, QCheckBox):
                    value = widget.isChecked()
                
                if value is not None:
                    # print(f"Saving: {object_name} = {value}")
                    ui_state[object_name] = value
                else:
                    print(f"Warning: Could not determine value for widget {object_name} of type {type(widget)}")
            
            # Also save the current tab index
            ui_state['__current_tab_index__'] = self.ui.tabWidget.currentIndex()

            # Write the dictionary to the JSON file
            with open(fileName, 'w') as f:
                json.dump(ui_state, f, indent=4)

            print(f"UI state successfully saved to {fileName}")
            QMessageBox.information(self, "Save Successful", f"UI state saved to:\n{fileName}")

        except Exception as e:
            print(f"Error saving UI state: {e}")
            detailed_error = traceback.format_exc()
            QMessageBox.critical(self, "Save Error", f"Could not save UI state:\n{e}\n\nDetails:\n{detailed_error}")


    @Slot()
    def on_actionLoad_triggered(self):
        """Loads UI state from a selected JSON file."""
        print("Load action triggered!")
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Load UI State", "", 
                                                  "JSON Files (*.json);;All Files (*)", options=options)
        if not fileName:
            print("Load cancelled.")
            return
        print(f"Attempting to load UI state from: {fileName}")
        try:
            # Read the state from the JSON file
            with open(fileName, 'r') as f:
                ui_state = json.load(f)

            # Apply the loaded state to the UI widgets
            for object_name, value in ui_state.items():
                
                # Handle special keys like the saved tab index
                if object_name == '__current_tab_index__':
                    if isinstance(value, int) and 0 <= value < self.ui.tabWidget.count():
                         self.ui.tabWidget.setCurrentIndex(value)
                    continue # Move to the next item

                # Find the widget by its object name
                # Important: Search within the 'ui' object if widgets are attributes of it
                # Or search within the main window ('self') if they are direct children
                widget = self.findChild(QObject, object_name) 

                if widget:
                    # print(f"Loading: {object_name} = {value} into {type(widget)}")
                    # Set the value based on the widget type
                    if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                        # Ensure value type compatibility (JSON loads numbers as float or int)
                        try:
                            widget.setValue(float(value) if isinstance(widget, QDoubleSpinBox) else int(value))
                        except (TypeError, ValueError) as type_err:
                             print(f"Warning: Type mismatch for {object_name}. Expected number, got {type(value)}. Error: {type_err}")
                    elif isinstance(widget, QComboBox):
                        # Find the index of the text and set it
                        index = widget.findText(str(value)) 
                        if index != -1:
                            widget.setCurrentIndex(index)
                        else:
                            print(f"Warning: Could not find text '{value}' in ComboBox '{object_name}'.")
                    elif isinstance(widget, QLineEdit):
                        widget.setText(str(value))
                    elif isinstance(widget, QCheckBox):
                        # Ensure value is boolean
                        widget.setChecked(bool(value))
                    else:
                        print(f"Widget {object_name} found, but its type ({type(widget)}) is not handled for loading.")
                else:
                    print(f"Warning: Widget with object name '{object_name}' not found in the UI.")

            print(f"UI state successfully loaded from {fileName}")
            QMessageBox.information(self, "Load Successful", f"UI state loaded from:\n{fileName}")

        except FileNotFoundError:
            print(f"Error: File not found - {fileName}")
            QMessageBox.critical(self, "Load Error", f"File not found:\n{fileName}")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON file - {fileName}. Error: {e}")
            QMessageBox.critical(self, "Load Error", f"Could not parse JSON file:\n{fileName}\n\nError: {e}")
        except Exception as e:
            print(f"Error loading UI state: {e}")
            detailed_error = traceback.format_exc()
            QMessageBox.critical(self, "Load Error", f"An unexpected error occurred while loading UI state:\n{e}\n\nDetails:\n{detailed_error}")

        

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
        """
        Reads Tab 1, CONVERTS UNITS for relevant Real variables to SI, 
        creates pymoo variables, and returns params dict.
        """
        parameters = {}
        
        # Maps UI text to Pint-compatible unit strings
        ui_to_pint_map = {
            "Meter": "meter", "Millimeter": "mm", "Inch": "inch",
            "Apk": "ampere", 
            "kg.m/s^2": "kg * meter**2",  # Correcting for Moment of Inertia
            "oz.in/s^2": "oz * inch**2",  # Correcting for Moment of Inertia
            "rpm": "rpm", "rad/s": "rad/s", "Hz": "Hz", # For speed (if needed elsewhere)
            "Nm": "N*m", "in.lb": "inch*lbf", "ft.lb": "foot*lbf", # For torque (if needed elsewhere)
            "cSt": "cSt", # Centistokes
            "H/m": "H/m", # Henry per meter
        }
        
        # Maps base variable names to their expected SI unit for the optimizer
        base_name_to_si_unit = {
            'R_MagnetRadialLength': 'meter',
            'R_MagnetOutR': 'meter',
            'R_MagnetBackIronInnerR': 'meter',
            'R_PhaseCurrentAmp': 'ampere', # Already SI
            'R_WireCopperR': 'meter',
            'R_InsulThick': 'meter',
            'R_LaminatToothWedgeThickness': 'meter',
            'R_LaminatR': 'meter',
            'R_LamSlotLinerThick': 'meter',
            'R_LoadInertia': 'kg * meter**2', # Moment of Inertia SI unit
            'R_MtrLength': 'meter',
            'R_AirgapRadialLength': 'meter',
            'R_FluidKinVisc': 'meter**2 / second', # Kinematic viscosity SI unit
            'R_VacMagneticPerm': 'H/m', # Already SI
             # Variables without units (or handled differently) don't need mapping here
            'R_MagneticLossCoef1': '', 'R_MagneticLossCoef2': '', 'R_MagneticLossCoef3': '',
            'R_FillFactor': '', 'R_GearRatio': '', 'R_FluidSpecificGrav': '',
        }
        # --- End Unit Mapping ---

        var_base_names = list(base_name_to_si_unit.keys()) # Get names from map keys
        # Add Integer variables manually
        var_base_names.extend(['I_PolePair', 'I_NumElecPhase']) 

        for base_name in var_base_names:
            try:
                widget1 = getattr(self.ui, base_name + '_1')
                widget2 = getattr(self.ui, base_name + '_2', None) 
                unit_widget = getattr(self.ui, base_name + '_unit', None)

                val1 = widget1.value()
                # Determine bounds: use widget2 if exists, else val1
                val2 = widget2.value() if widget2 else val1

                # Handle Integer types first (no unit conversion needed here)
                if base_name.startswith('I_'):
                    int_bounds = (int(val1), int(val2))
                    if int_bounds[0] > int_bounds[1]:
                         raise ValueError(f"Lower bound ({int_bounds[0]}) > Upper bound ({int_bounds[1]})")
                    parameters[base_name] = Integer(bounds=int_bounds)
                    continue # Move to next base_name

                # Handle Real types (check for unit conversion)
                elif base_name.startswith('R_'):
                    target_si_unit = base_name_to_si_unit.get(base_name)
                    
                    # Perform unit conversion IF a unit widget exists AND a target SI unit is defined
                    if unit_widget and target_si_unit:
                        selected_unit_text = unit_widget.currentText()
                        pint_unit_str = ui_to_pint_map.get(selected_unit_text)
                        
                        if not pint_unit_str:
                            raise ValueError(f"Unit '{selected_unit_text}' selected for '{base_name}' is not defined in ui_to_pint_map.")
                        
                        # Use Pint for conversion
                        pint_unit = self.ureg(pint_unit_str)
                        val1_si = (val1 * pint_unit).to(target_si_unit).magnitude
                        # Convert val2 only if widget2 exists, otherwise use val1_si
                        val2_si = (val2 * pint_unit).to(target_si_unit).magnitude if widget2 else val1_si
                        
                        # Create Pymoo Real variable with SI bounds
                        float_bounds_si = (float(val1_si), float(val2_si))

                    # No unit conversion needed (either no unit widget or no target SI defined)
                    else:
                        float_bounds_si = (float(val1), float(val2))

                    # Final bounds check for Real variables
                    if float_bounds_si[0] > float_bounds_si[1]:
                         raise ValueError(f"Lower bound ({float_bounds_si[0]}) > Upper bound ({float_bounds_si[1]}) in SI units")
                    
                    parameters[base_name] = Real(bounds=float_bounds_si)

            except AttributeError as e:
                raise AttributeError(f"UI element not found for '{base_name}'. Check UI file/names. Error: {e}")
            except ValueError as e: 
                raise ValueError(f"Input or Unit error for '{base_name}': {e}")
            except pint.UndefinedUnitError as e:
                 raise pint.UndefinedUnitError(f"Unit error for '{base_name}': {e}")
            except pint.DimensionalityError as e:
                 raise pint.DimensionalityError(f"Unit conversion error for '{base_name}' from '{pint_unit_str}' to '{target_si_unit}': {e}")
            except Exception as e:
                raise ValueError(f"Unexpected error processing UI variable '{base_name}': {e}\n{traceback.format_exc()}")
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