# utils/material_manager.py

# Material Properties Data
MAGNET_BR_VALUES = {
    "Recoma 18": 0.87, "Recoma 20": 0.90, "Recoma 22": 0.94, "Recoma 25": 1.00,
    "Recoma 24HE": 1.02, "Recoma 26": 1.04, "Recoma 26HE": 1.07, "Recoma 28": 1.10,
    "Recoma 28HE": 1.10, "Recoma 30": 1.12, "Recoma 30HE": 1.12, "Recoma 30S": 1.12,
    "Recoma 32": 1.15, "Recoma 32S": 1.15, "Recoma 33E": 1.16, "Recoma 35E": 1.19,
}
IRON_BR_VALUES = {
    "430 Stainless Steel": 1.3, "1215 Steel": 1.5, "1018 Steel": 1.4,
    "1008 Steel": 1.4, "1010 Steel": 1.4, "Hiperco 50": 2.0, "M19": 1.75,
}
LAMINATION_BR_VALUES = {
    "M19": 1.75, "Hiperco 50": 2.3,
}

# Unit mapping for get_unit, could be expanded or moved if it becomes more complex
UNIT_MAP = {
    'R_MagnetRadialLength': 'meter',
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

def update_magnet_br_property(main_window_instance):
    """Updates MagnetBr_T on the main_window_instance based on UI selection."""
    selected_material = main_window_instance.ui.Magnet_Material.currentText()
    main_window_instance.MagnetBr_T = MAGNET_BR_VALUES.get(selected_material, 1.1) # Default if needed
    # print(f"Updated MagnetBr_T: {main_window_instance.MagnetBr_T}")

def update_max_b_magnet_iron_property(main_window_instance):
    """Updates MaxBMagnetIron_T on the main_window_instance based on UI selection."""
    selected_option = main_window_instance.ui.Iron_Material.currentText()
    main_window_instance.MaxBMagnetIron_T = IRON_BR_VALUES.get(selected_option, 1.5)
    # print(f"Updated MaxBMagnetIron_T: {main_window_instance.MaxBMagnetIron_T}")

def update_present_b_lamination_property(main_window_instance):
    """Updates PresentBLaminationBackIron_T on the main_window_instance based on UI selection."""
    selected_option = main_window_instance.ui.Lamination_Material.currentText()
    main_window_instance.PresentBLaminationBackIron_T = LAMINATION_BR_VALUES.get(selected_option, 1.75)
    # print(f"Updated PresentBLaminationBackIron_T: {main_window_instance.PresentBLaminationBackIron_T}")

def get_unit_for_variable(variable_name):
    """Return the unit corresponding to the variable name."""
    return UNIT_MAP.get(variable_name, 'meter') # Default to 'meter' or raise error