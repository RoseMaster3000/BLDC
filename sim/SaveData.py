'''
This script saves the optimized objectives and corresponding parameters in an Excel file.

Input:
    X,      optimized motor parameters
    F,      optimized objectives
    file_path,  The full path (including filename) to save the Excel file to.
    ... other parameters
   
Output:
    N/A
'''
import numpy as np
import pandas as pd
from scipy.io import savemat
from pymoo.core.variable import Real, Integer, Choice, Binary
import os


# Add 'file_path' as the last argument
def SaveMat(eng, X, F, G, variables, params, MagnetBr_T, MaxBMagnetIron_T, PresentBLaminationBackIron_T, file_path):

    consts = dict()
    for key, value in params.items():
        if type(value) not in [Real, Integer, Binary, Choice]:
            consts[key]=value
            
    MinEff_ = variables.get("MinEff_")
    MaxWeight_kg = variables.get("MaxWeight")
    VDC = variables.get("VDC")
    MinTor_Nm_str = variables.get("MinTor")
    SpeedReq_rpm_str = variables.get("SpeedReq")   
    
    Tor_numbers = MinTor_Nm_str.split(',')
    MinTor_Nm = [float(num) for num in Tor_numbers]
    Speed_numbers = SpeedReq_rpm_str.split(',')
    SpeedReq_rpm = [float(num) for num in Speed_numbers]    

    NumPts = len(SpeedReq_rpm)
    NumInEqConst_ = NumPts + 5
    NumEqConst_ = 0
    NumObj_ = 0
    if params.get("TorqueOpt") == True:
        NumObj_ = NumObj_ + NumPts
    # ... (rest of your NumObj_ calculations)
    if params.get("MtrRadiusOpt") == True:
        NumObj_ = NumObj_ + 1

    data1 = {
        'SpeedReq_rpm': SpeedReq_rpm,
        'TorReq_Nm': MinTor_Nm,
        'EffReq_': MinEff_,
        'WeightReq_kg' : MaxWeight_kg,
        'VDCReq' : VDC,
    }

    temp_data_file1 = 'temp_data_1.xlsx'
    temp_data_file2 = 'temp_data_2.xlsx'
    
    df_X = pd.DataFrame(list(X))
    df_data1 = pd.DataFrame([data1])
    df_updated = pd.concat([df_data1, df_X], axis=1)
    
    df_updated.to_excel(temp_data_file1, index=False)
    
    PostProcess = True
    i = 0
    Mtr_res = eng.UI_MotorCalcs_MATLAB_Vectorized(
        list(X[i].keys()),
        list(X[i].values()),
        list(consts.keys()),
        list(consts.values()),
        MinTor_Nm,
        MagnetBr_T,
        MaxBMagnetIron_T,
        PresentBLaminationBackIron_T,
        SpeedReq_rpm, PostProcess, NumObj_, nargout=1
    )
    a = list(Mtr_res.values())
    df_a0 = pd.DataFrame(a[0])
    df_a1 = pd.DataFrame(a[1])
    a_row = pd.concat([df_a0, df_a1], axis=1)
    df_exis = pd.DataFrame(a_row)
    for i in range(1, len(X)):
        Mtr_res = eng.UI_MotorCalcs_MATLAB_Vectorized(list(X[i].keys()),list(X[i].values()),list(consts.keys()),list(consts.values()), MinTor_Nm, MagnetBr_T, MaxBMagnetIron_T, PresentBLaminationBackIron_T, SpeedReq_rpm, PostProcess,NumObj_,  nargout=1)
        a = list(Mtr_res.values())
        df_a0 = pd.DataFrame(a[0])
        df_a1 = pd.DataFrame(a[1])
        a_row = pd.concat([df_a0, df_a1], axis=1)
        df_new_row = pd.DataFrame(a_row)
        df_exis = pd.concat([df_exis, df_new_row], axis=0)
    df_exis.to_excel(temp_data_file2, index=False)

    df_1 = pd.read_excel(temp_data_file1)
    df_2 = pd.read_excel(temp_data_file2)
    df_all = pd.concat([df_1, df_2], axis=1)


    # Use the file_path passed from the Qt dialog
    df_all.to_excel(file_path, index=False)
    
    # Clean up temporary files
    os.remove(temp_data_file1)
    os.remove(temp_data_file2)