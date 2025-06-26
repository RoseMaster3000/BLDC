import traceback
import pint       # For unit conversion
from pymoo.core.variable import Real, Integer, Choice, Binary

# These could also be moved to a central config if they are used by more than just this parser
UI_TO_PINT_MAP = {
    "m": "meter", "mm": "mm", "in": "inch",
    "Apk": "ampere", "Arms": "ampere",
    "kg-m^2": "kg * meter**2",
    "N-m-s^2": "N*m * s**2", 
    "lbm-ft^2": "lbm*foot**2",
    "lbm-in^2": "lbm*inch**2",
    "ozm-in^2": "oz * inch**2", 
    "ozf-in-s^2": "ozf * inch * s**2", 
    "rpm": "rpm", "rad/s": "rad/s", "Hz": "Hz",
    "N-m": "N*m", "in-lb": "inch*lbf", "ft-lb": "foot*lbf",
    "cSt": "cSt",
    "m^2/s": "meter**2/s",
    "H/m": "H/m",
}

BASE_NAME_TO_SI_UNIT = {
    'R_MagnetRadialLength': 'meter',
    'R_MagnetOutR': 'meter',
    'R_MagnetBackIronInnerR': 'meter',
    'R_PhaseCurrentAmp': 'ampere',
    'R_WireCopperR': 'meter',
    'R_InsulThick': 'meter',
    'R_LaminatToothWedgeThickness': 'meter',
    'R_LaminatR': 'meter',
    'R_LamSlotLinerThick': 'meter',
    'R_LoadInertia': 'kg * meter**2', # SI for Moment of Inertia
    'R_MtrLength': 'meter',
    'R_AirgapRadialLength': 'meter',
    'R_FluidKinVisc': 'cSt', # Pymoo problem might expect 'meter**2 / second' but UI gives cSt
    'R_MagneticLossCoef1': '', 'R_MagneticLossCoef2': '', 'R_MagneticLossCoef3': '', # Dimensionless
    'R_FillFactor': '', 'R_GearRatio': '', 'R_FluidSpecificGrav': '', # Dimensionless
}

def create_pymoo_parameters_from_ui(main_window_instance):
    """
    Reads Tab 1, CONVERTS UNITS for relevant Real variables to SI,
    creates pymoo variables, and returns params dict.
    """
    parameters = {}
    ureg = main_window_instance.ureg # Access pint UnitRegistry from main window

    var_base_names = list(BASE_NAME_TO_SI_UNIT.keys())
    var_base_names.extend(['I_PolePair', 'I_NumElecPhase'])

    for base_name in var_base_names:
        try:
            widget1 = getattr(main_window_instance.ui, base_name + '_1')
            widget2 = getattr(main_window_instance.ui, base_name + '_2', None)
            unit_widget = getattr(main_window_instance.ui, base_name + '_unit', None)

            val1 = widget1.value()
            val2 = widget2.value() if widget2 else val1

            if base_name.startswith('I_'):
                int_bounds = (int(val1), int(val2))
                if int_bounds[0] > int_bounds[1]:
                    raise ValueError(f"Lower bound ({int_bounds[0]}) > Upper bound ({int_bounds[1]}) for {base_name}")
                parameters[base_name] = Integer(bounds=int_bounds)
                continue

            elif base_name.startswith('R_'):
                target_si_unit_str = BASE_NAME_TO_SI_UNIT.get(base_name)
                
                if unit_widget and target_si_unit_str: # Unit conversion needed
                    selected_unit_text = unit_widget.currentText()
                    pint_ui_unit_str = UI_TO_PINT_MAP.get(selected_unit_text)
                    
                    if not pint_ui_unit_str:
                        raise ValueError(f"Unit '{selected_unit_text}' for '{base_name}' not in UI_TO_PINT_MAP.")

                    ui_unit = ureg(pint_ui_unit_str)
                    target_si_unit = ureg(target_si_unit_str)

                    # Special handling for 'Arms' to 'ampere' conversion if needed
                    if base_name == 'R_PhaseCurrentAmp' and selected_unit_text == 'Arms':
                        # Convert RMS current to peak current (assuming sinusoidal)
                        val1_si = (val1 * ui_unit * (2 ** 0.5)).to(target_si_unit).magnitude
                        val2_si = (val2 * ui_unit * (2 ** 0.5)).to(target_si_unit).magnitude if widget2 else val1_si
                    # Special handling for viscosity: UI might be cSt, but calculation needs m^2/s
                    elif base_name == 'R_FluidKinVisc' and pint_ui_unit_str == 'cSt' and target_si_unit_str == 'meter**2 / second':
                        # 1 cSt = 1 mm^2/s = 1e-6 m^2/s
                        val1_si = (val1 * ureg.mm**2 / ureg.second).to(target_si_unit).magnitude
                        val2_si = (val2 * ureg.mm**2 / ureg.second).to(target_si_unit).magnitude if widget2 else val1_si
                    elif base_name == 'R_FluidKinVisc' and pint_ui_unit_str == 'cSt' and target_si_unit_str == 'cSt':
                        # If the target is already cSt, no conversion needed beyond fetching value.
                        # This branch is for if the optimization problem *itself* expects cSt.
                        # However, the original code implies conversion to a standard SI m^2/s for most physics.
                        # Let's assume for now the problem takes cSt directly if target_si_unit_str IS 'cSt'.
                        val1_si = val1
                        val2_si = val2 if widget2 else val1
                    else:
                        val1_si = (val1 * ui_unit).to(target_si_unit).magnitude
                        val2_si = (val2 * ui_unit).to(target_si_unit).magnitude if widget2 else val1_si
                    
                    float_bounds_si = (float(val1_si), float(val2_si))
                
                elif not target_si_unit_str: # Dimensionless or no unit conversion specified
                    float_bounds_si = (float(val1), float(val2))
                
                else: # No unit widget, assume values are already in target SI if target_si_unit is defined
                      # Or, if target_si_unit is not defined for a R_ variable (should not happen with current map)
                    print(f"Warning: No unit widget for {base_name}, assuming values [{val1}, {val2}] are in expected SI ({target_si_unit_str or 'dimensionless'}).")
                    float_bounds_si = (float(val1), float(val2))

                if float_bounds_si[0] > float_bounds_si[1]:
                    raise ValueError(f"Lower bound ({float_bounds_si[0]}) > Upper bound ({float_bounds_si[1]}) for {base_name} in SI units")
                parameters[base_name] = Real(bounds=float_bounds_si)

        except AttributeError as e:
            raise AttributeError(f"UI element not found for '{base_name}'. Check UI file/names. Error: {e}")
        except ValueError as e:
            raise ValueError(f"Input or Unit error for '{base_name}': {e}")
        except pint.UndefinedUnitError as e:
            raise pint.UndefinedUnitError(f"Unit error for '{base_name}': {e}")
        except pint.DimensionalityError as e:
            # Construct a more informative error message for dimensionality issues
            source_unit_display = pint_ui_unit_str if 'pint_ui_unit_str' in locals() else "unknown source unit"
            target_unit_display = target_si_unit_str if 'target_si_unit_str' in locals() else "unknown target unit"
            raise pint.DimensionalityError(f"Unit conversion error for '{base_name}' from '{source_unit_display}' to '{target_unit_display}': {e}")
        except Exception as e:
            raise ValueError(f"Unexpected error processing UI variable '{base_name}': {e}\n{traceback.format_exc()}")
    return parameters


def read_opt_config_from_ui(main_window_instance):
    """Reads Tab 2 configuration."""
    conf = {}
    ui = main_window_instance.ui
    try:
        conf['npop'] = ui.npop.value()
        conf['ngens'] = ui.ngens.value()
        conf['nprocesses'] = ui.nprocesses.value()
        conf['DisMut'] = ui.DisMut.value()
        conf['ProbMut'] = ui.ProbMut.value()

        conf['SpeedReq'] = ui.SpeedReq.text() # Consider converting to float/int with units if applicable
        conf['MinTor'] = ui.MinTor.text()     # Consider converting to float/int with units
        conf['MinEff_'] = ui.MinEff_.value()
        conf['MaxWeight'] = ui.MaxWeight.value()
        conf['VDC'] = ui.VDC.value()

        conf['TorqueOpt'] = ui.TorqueOpt.isChecked()
        conf['Efficinecy_minOpt'] = ui.Efficinecy_minOpt.isChecked()
        conf['Efficinecy_maxOpt'] = ui.Efficinecy_maxOpt.isChecked()
        conf['WeightOpt'] = ui.WeightOpt.isChecked()
        conf['MagWeightOpt'] = ui.MagWeightOpt.isChecked()
        conf['VoltageOpt'] = ui.VoltageOpt.isChecked()
        conf['MtrLengthOpt'] = ui.MtrLengthOpt.isChecked()
        conf['MtrRadiusOpt'] = ui.MtrRadiusOpt.isChecked()

        if not any(v for k, v in conf.items() if k.endswith('Opt')):
            raise ValueError("No optimization objectives selected in Tab 2!")
        
        # Example: Convert SpeedReq and MinTor if they are expected as numbers
        # try:
        #     conf['SpeedReq_val'] = float(conf['SpeedReq']) # Add unit handling if needed
        #     conf['MinTor_val'] = float(conf['MinTor'])     # Add unit handling if needed
        # except ValueError:
        #     raise ValueError("Speed Requirement and Minimum Torque must be valid numbers.")


    except AttributeError as e:
        raise ValueError(f"Error accessing UI element in Tab 2 (check names): {e}")
    except Exception as e:
        raise ValueError(f"Error reading configuration from Tab 2: {e}")
    return conf


def get_other_opt_args(main_window_instance):
    """Gets fixed args: material props, engine, pymoo types."""
    # Ensure current material properties are fetched/updated from MainWindow instance
    # These properties (MagnetBr_T, etc.) should have been set on main_window_instance
    # by calling the update_..._property functions from material_manager.py
    # before this function is called.

    if not main_window_instance.matlab_engine:
        raise ValueError("MATLAB Engine not available!")

    return (main_window_instance.MagnetBr_T,
            main_window_instance.MaxBMagnetIron_T,
            main_window_instance.PresentBLaminationBackIron_T,
            main_window_instance.matlab_engine,
            Real, Integer, Choice, Binary)