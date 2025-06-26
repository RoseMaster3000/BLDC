''' 
This script plot the objectives in MATLAB

Input:
    eng,  Matlab engine
    F,    optimized objectives
    
Output:
    N/A
'''

import matlab.engine 
eng = matlab.engine.start_matlab()
#def PlotMat(eng,F,G):
    
import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk  # Import ttk for Combobox

class PlotMat:
    def __init__(self, root):
        self.root = root
        self.root.title("Select Signals for Plotting")
        self.root.geometry("350x400")  # Set the window size wxh

        # Hardcoded labels for each row and their associated strings
        self.labels = [
            "Minimum Torque Margin",
            "Average Torque Margin",
            "Minimum Efficiency",
            "Average Efficiency",
            "Motor Weight",
            "Magnet Volume",
            "Phase Voltage",
            "Motor Length",
            "Motor Radius",
            "Maximum Motor Loss",
        ]

        # Associated strings for each label
        self.associated_strings = [
            "MinTrqMargin_Percent",
            "MeanTrqMargin_Percent",
            "MinEffMtr_Percent",
            "MeanEffMtr_Percent",
            "Weight_kg",
            "MagVol_m3",
            "VDC",
            "R_MtrLength_m",
            "R_LaminatR_m",
            "MaxTotalLoss_W",
        ]

        self.checkboxes = []  # List to store checkbox variables

        # Create rows with hardcoded labels
        for label, option in zip(self.labels, self.associated_strings):
            frame = tk.Frame(self.root)  # Create a frame for each row
            label_widget = tk.Label(frame, text=label)  # Create a label for the row
            label_widget.pack(side=tk.RIGHT, padx=(0, 5))  # Pack the label to the right
            
            # Create a variable to store the checkbox state
            var = tk.BooleanVar()  # Create a BooleanVar for the checkbox state
            checkbox = tk.Checkbutton(frame, variable=var)  # Create a checkbox linked to the variable
            checkbox.pack(side=tk.LEFT)  # Pack the checkbox to the left
            
            self.checkboxes.append((var, option))  # Store the variable and associated string for later use
            frame.pack(anchor='w', padx=(50))  # Pack the frame to the main window


        # Create three drop-down menus
        self.dropdown1 = ttk.Combobox(self.root, width=40)
        self.dropdown1['values'] = ("# of pole pairs", "Radial length of magnet", "Wire copper radius", "Fill factor", "Lamination tooth tip and wedge thickness", 
                                    "Lamination slot liner thickness", "Gear ratio", "Magnet backiron inner radius" ,
                                    "Magnet backiron outer radius", "Tooth width", "Lamination tooth tip radius", "Lamination slot radius", 
                                    "Magnet inner radius", "Backiron thickness, lamination", 
                                    "Backiron thickness, magnet assembly", "Lamination slot outer", "Lamination slot area", "Winding Slot area", 
                                    "Arc length of lamination ID", "Arc length of one tooth pitch"
                                   , "Approx width of slot opening", "# of turns", "Actual flux density", 
                                    "Actual coil flux", "Rated Torque per phase", "Torque constant", 
                                    "BackEMF constant", "Phase inductance", "Phase resistance", 
                                    "Inertia", "torque/inertia", "Motor volume"
                                   , "Stator surface area", "Fe weight", "Cu weight", "Rotor weight", 
                                    "Current density", "Mean resistive losses", "Mean back iron losses", 
                                    "Mean fluid losses")  # Example options
        self.dropdown1.pack(pady=5)  # Pack the first drop-down menu
        self.dropdown2 = ttk.Combobox(self.root, width=40)
        self.dropdown2['values'] = ("# of pole pairs", "Radial length of magnet", "Wire copper radius", "Fill factor", "Lamination tooth tip and wedge thickness", 
                                    "Lamination slot liner thickness", "Gear ratio", "Magnet backiron inner radius" ,
                                    "Magnet backiron outer radius", "Tooth width", "Lamination tooth tip radius", "Lamination slot radius", 
                                    "Magnet inner radius", "Backiron thickness, lamination", 
                                    "Backiron thickness, magnet assembly", "Lamination slot outer", "Lamination slot area", "Winding Slot area", 
                                    "Arc length of lamination ID", "Arc length of one tooth pitch"
                                   , "Approx width of slot opening", "# of turns", "Actual flux density", 
                                    "Actual coil flux", "Rated Torque per phase", "Torque constant", 
                                    "BackEMF constant", "Phase inductance", "Phase resistance", 
                                    "Inertia", "torque/inertia", "Motor volume"
                                   , "Stator surface area", "Fe weight", "Cu weight", "Rotor weight", 
                                    "Current density", "Mean resistive losses", "Mean back iron losses", 
                                    "Mean fluid losses")  # Example options
        self.dropdown2.pack(pady=5)  # Pack the second drop-down menu
        self.dropdown3 = ttk.Combobox(self.root, width=40)
        self.dropdown3['values'] = ("# of pole pairs", "Radial length of magnet", "Wire copper radius", "Fill factor", "Lamination tooth tip and wedge thickness", 
                                    "Lamination slot liner thickness", "Gear ratio", "Magnet backiron inner radius" ,
                                    "Magnet backiron outer radius", "Tooth width", "Lamination tooth tip radius", "Lamination slot radius", 
                                    "Magnet inner radius", "Backiron thickness, lamination", 
                                    "Backiron thickness, magnet assembly", "Lamination slot outer", "Lamination slot area", "Winding Slot area", 
                                    "Arc length of lamination ID", "Arc length of one tooth pitch"
                                   , "Approx width of slot opening", "# of turns", "Actual flux density", 
                                    "Actual coil flux", "Rated Torque per phase", "Torque constant", 
                                    "BackEMF constant", "Phase inductance", "Phase resistance", 
                                    "Inertia", "torque/inertia", "Motor volume"
                                   , "Stator surface area", "Fe weight", "Cu weight", "Rotor weight", 
                                    "Current density", "Mean resistive losses", "Mean back iron losses", 
                                    "Mean fluid losses")  # Example options
        self.dropdown3.pack(pady=5)  # Pack the third drop-down menu


           # Create a frame for the buttons at the bottom
        button_frame = tk.Frame(self.root)
        
        # Add a Parallel Plot button
        self.parallel_plot_button = tk.Button(button_frame, text="Parallel Plot", command=self.parallel_submit_selection)
        self.parallel_plot_button.pack(side=tk.LEFT, padx=5)  # Pack the button with some padding

        # Add a 3D Plot button
        self.three_d_plot_button = tk.Button(button_frame, text="3D Plot", command=self.threeD_submit_selection)
        self.three_d_plot_button.pack(side=tk.LEFT, padx=5)  # Pack the button with some padding

        button_frame.pack(pady=10)  # Pack the button frame with some vertical padding

    def parallel_submit_selection(self):
        """Store the selections in the coordvars variable."""
        coordvars = [option for var, option in self.checkboxes if var.get()]  # Collect associated strings of checked boxe     
        selected_dropdown1 = self.dropdown1.get()  # Get selected value from the first drop-down
        selected_dropdown2 = self.dropdown2.get()  # Get selected value from the second drop-down
        selected_dropdown3 = self.dropdown3.get()  # Get selected value from the third drop-down

        dropdown_strings = {
            "# of pole pairs": "I_PolePair_",
            "Radial length of magnet": "R_MagnetRadialLength_m",
            "Wire copper radius": "R_WireCopperR_m",
            "Fill factor": "R_FillFactor_",
            "Lamination tooth tip and wedge thickness": "R_LaminatToothWedgeThickness_m",
            "Lamination slot liner thickness": "R_LamSlotLinerThick_m",
            "Gear ratio": "R_GearRatio_", 
            "Magnet backiron inner radius": "MagBackIronInR_m",
            "Magnet backiron outer radius": "MagBackIranOutR_m",
            "Tooth width": "ToothWidth_m",
            "Lamination tooth tip radius": "LamTTipR_m",
            "Lamination slot radius": "LamSlotR_m",
            "Magnet inner radius": "MagInR_m",
            "Backiron thickness, lamination": "BackIronThickLam_m",
            "Backiron thickness, magnet assembly": "BackIronThickMag_m",
            "Lamination slot outer": "LamSlotOutR_m",
            "Lamination slot area": "LamSlotA_m2",
            "Winding Slot area": "WindSlotA_m2",
            "Arc length of lamination ID": "ArcLamID_m",
            "Arc length of one tooth pitch": "ArcToothPitch_m",
            "Approx width of slot opening": "SlotOpenWidth_m",
            "# of turns": "NumTurn",
            "Actual flux density": "ActualFluxDens",
            "Actual coil flux": "ActualCoilFlux",
            "Rated Torque per phase": "RateTrqPPhase_Nm",
            "Torque constant": "KT_Nm_A",
            "BackEMF constant": "KB_VLLPkNs_rad",
            "Phase inductance": "InducPh_H",
            "Phase resistance": "ResisPh_ohm",
            "Inertia": "Inertia_Nms2",
            "torque/inertia": "TrqPerInertia_1_s2",
            "Motor volume": "Volume_m3",
            "Stator surface area": "StatorSurfA_m2",
            "Fe weight": "FeWeight_kg",
            "Cu weight": "CuWeight_kg",
            "Rotor weight": "RotWeight_kg",
            "Current density": "CurrDens_A_m2",
            "Mean resistive losses": "MeanResLoss_W",
            "Mean back iron losses": "MeanBackIronLoss_W",
            "Mean fluid losses": "MeanFluidLoss_W",
        }

        # Add the corresponding string for each selected dropdown value to coordvars
        if selected_dropdown1 in dropdown_strings:
            coordvars.append(dropdown_strings[selected_dropdown1])
        if selected_dropdown2 in dropdown_strings:
            coordvars.append(dropdown_strings[selected_dropdown2])
        if selected_dropdown3 in dropdown_strings:
            coordvars.append(dropdown_strings[selected_dropdown3])

        tsunami = eng.UI_ParallelPlot_MATLAB(coordvars,ExcelFileName,nargout=1)
        
    def threeD_submit_selection(self):
        coordvars = [option for var, option in self.checkboxes if var.get()]  # Collect associated strings of checked boxe     
        selected_dropdown1 = self.dropdown1.get()  # Get selected value from the first drop-down
        selected_dropdown2 = self.dropdown2.get()  # Get selected value from the second drop-down
        selected_dropdown3 = self.dropdown3.get()  # Get selected value from the third drop-down

        dropdown_strings = {
            "# of pole pairs": "I_PolePair_",
            "Radial length of magnet": "R_MagnetRadialLength_m",
            "Wire copper radius": "R_WireCopperR_m",
            "Fill factor": "R_FillFactor_",
            "Lamination tooth tip and wedge thickness": "R_LaminatToothWedgeThickness_m",
            "Lamination slot liner thickness": "R_LamSlotLinerThick_m",
            "Gear ratio": "R_GearRatio_", 
            "Magnet backiron inner radius": "MagBackIronInR_m",
            "Magnet backiron outer radius": "MagBackIranOutR_m",
            "Tooth width": "ToothWidth_m",
            "Lamination tooth tip radius": "LamTTipR_m",
            "Lamination slot radius": "LamSlotR_m",
            "Magnet inner radius": "MagInR_m",
            "Backiron thickness, lamination": "BackIronThickLam_m",
            "Backiron thickness, magnet assembly": "BackIronThickMag_m",
            "Lamination slot outer": "LamSlotOutR_m",
            "Lamination slot area": "LamSlotA_m2",
            "Winding Slot area": "WindSlotA_m2",
            "Arc length of lamination ID": "ArcLamID_m",
            "Arc length of one tooth pitch": "ArcToothPitch_m",
            "Approx width of slot opening": "SlotOpenWidth_m",
            "# of turns": "NumTurn",
            "Actual flux density": "ActualFluxDens",
            "Actual coil flux": "ActualCoilFlux",
            "Rated Torque per phase": "RateTrqPPhase_Nm",
            "Torque constant": "KT_Nm_A",
            "BackEMF constant": "KB_VLLPkNs_rad",
            "Phase inductance": "InducPh_H",
            "Phase resistance": "ResisPh_ohm",
            "Inertia": "Inertia_Nms2",
            "torque/inertia": "TrqPerInertia_1_s2",
            "Motor volume": "Volume_m3",
            "Stator surface area": "StatorSurfA_m2",
            "Fe weight": "FeWeight_kg",
            "Cu weight": "CuWeight_kg",
            "Rotor weight": "RotWeight_kg",
            "Current density": "CurrDens_A_m2",
            "Mean resistive losses": "MeanResLoss_W",
            "Mean back iron losses": "MeanBackIronLoss_W",
            "Mean fluid losses": "MeanFluidLoss_W",
        }

        # Add the corresponding string for each selected dropdown value to coordvars
        if selected_dropdown1 in dropdown_strings:
            coordvars.append(dropdown_strings[selected_dropdown1])
        if selected_dropdown2 in dropdown_strings:
            coordvars.append(dropdown_strings[selected_dropdown2])
        if selected_dropdown3 in dropdown_strings:
            coordvars.append(dropdown_strings[selected_dropdown3])

        if len(coordvars) !=3:
            messagebox.showinfo("Selections Submitted", "For 3D plots, select 3 parameters.")
        else:
            tsunami = eng.UI_3DPlot_MATLAB(coordvars,ExcelFileName,nargout=1)