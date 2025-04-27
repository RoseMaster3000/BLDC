''' 
This script represents the model to be optimized. The model is developed in MATLAB, MotorCalcs_MATLAB.m

Inputs: 
    vars,          optimization vatriables in `params` dictionary
    consts,        constants in `params` dictionary
    MinEffReq_,       minimum acceptable Efficiency
    MinTor_ozin,   minimum acceptable Torque ozin
    MaxWeight_lbm, maximum acceptable Weight lbm
    eng,           Matlab engine

Outputs:
    Mtr_res,       objectives as a list of NumPy array with length of NumObj_. Note: The objectives are minimized. Implement a mathematical operand to convert all maximized objectives into minimized objectives.
    [g1,g2,g3],    constraints with a length of NumInEqConst_.

'''
def MotorCalcs_Vectorized(vars, consts, MinEffReq_, MinTor_Nm, MaxWeight_kg, VDC, MagnetBr_T, MaxBMagnetIron_T, PresentBLaminationBackIron_T, SpeedReq_rpm, eng, variables, NumObj_, **kwargs):
    assert isinstance(vars, dict)
    assert isinstance(consts, dict)
    NumTurnThreshold = 0.03 # force the number of turns to be an integer +/-0.03
    PostProcess = False 
    # print(list(vars.keys()))
    # print(list(vars.values()))
    # print(list(consts.keys()))
    # print(list(consts.values()))
    # # print(consts.get("EfficinecyOpt_min"))
    # # if consts.get("EfficinecyOpt_min") == True:
    # #     print('tru')
    # print(MagnetBr_T)
    # print(MaxBMagnetIron_T)
    # print(PresentBLaminationBackIron_T)
    # print(SpeedReq_rpm)
    # print(type(MinTor_Nm))
    # print(vars.get("R_GearRatio_"))
    Mtr_res = eng.UI_MotorCalcs_MATLAB_Vectorized(list(vars.keys()),list(vars.values()),list(consts.keys()),list(consts.values()), MinTor_Nm, MagnetBr_T, MaxBMagnetIron_T, PresentBLaminationBackIron_T, SpeedReq_rpm, PostProcess,NumObj_,  nargout=1)
    
    # print(Mtr_res[0])
    F = []
    g = []
    NumPts = len(SpeedReq_rpm)
    EfficienciesPerf = list(Mtr_res[0][NumPts:NumPts*2])
    MinEffPerf_ = max(EfficienciesPerf)  # reported efficiencies have (-1)
    MaxEffPerf_ = min(EfficienciesPerf)  # reported efficiencies have (-1)

    if consts.get("TorqueOpt") == True: 
        for i in range(NumPts):
            F.append(Mtr_res[0][i])
            
    if consts.get("EfficinecyOpt_min") == True: 
        min_index = EfficienciesPerf.index(MinEffPerf_)
        F.append(Mtr_res[0][NumPts+min_index])
        
    if consts.get("EfficinecyOpt_max") == True: 
        max_index = EfficienciesPerf.index(MaxEffPerf_)
        F.append(Mtr_res[0][NumPts+max_index])
        
    if consts.get("WeightOpt") == True:     
        F.append(Mtr_res[0][2*NumPts])
        
    if consts.get("MagWeightOpt") == True:     
        F.append(Mtr_res[0][2*NumPts+1])   
        
    if consts.get("VoltageOpt") == True:     
        F.append(Mtr_res[0][2*NumPts+2])      

    if consts.get("MtrLengthOpt") == True:     
        F.append(Mtr_res[0][2*NumPts+3])   

    if consts.get("MtrRadiusOpt") == True:     
        F.append(Mtr_res[0][2*NumPts+4])   

    for i in range(NumPts):
        g.append(MinTor_Nm[i] + Mtr_res[0][i])   # Requirement - torque <0
    g.append(MinEffReq_ + MinEffPerf_)           # Requirement - efficiency <0 
    g.append(Mtr_res[0][2*NumPts] - MaxWeight_kg) # Weight - Requirement <0 
    g.append(Mtr_res[0][2*NumPts+2] - VDC) # Voltage - Requirement <0
    g.append(abs(round(Mtr_res[0][2*NumPts+3])-Mtr_res[0][2*NumPts+3]) - NumTurnThreshold) # force the number of turns to be close to an integer number
    g.append( 1 - NumTurnThreshold - Mtr_res[0][2*NumPts+3]) # to get at least 1 turn

    # print('g')
    # print(g)
    # The function return statement should always be in the form of [f1, f2, ...] , [g1, g2, ...]
    # If no constrains are defined, use [] instead of [g1, g2, ...]
    return [F], [g]