''' 
This script sets up and runs the GA Optimizer

Inputs: 
    MotorCalcs,    a function that calculates the motor performances
    params,        a dictionary  that include the model parameters including constans and optimization OptimizationConf
    NumEqConst_,   number of equality constraints
    NumInEqConst_, number of inequality constraints
    MinEff_,       Minimum acceptable efficiency
    MinTor_ozin,   Minimum acceptable torque ozin
    MaxWeight_lbm, Maximum acceptable weight lbm
    eng,           Matlab engine
    Real,          A class from Pymoo that defines continuous OptimizationConf with specified bounds
    Integer,       A class from Pymoo that defines integer OptimizationConf with specified bounds
    Choice,        A class from Pymoo that allows selection from a predefined set of options
    Binary,        A class from Pymoo that defines binary OptimizationConf (0 or 1)
    
Outputs:
    res,           Optimization results
'''

from pymoo.core.problem import ElementwiseProblem
from pymoo.optimize import minimize
from pymoo.core.mixed import MixedVariableGA
from pymoo.termination.default import DefaultMultiObjectiveTermination
from pymoo.operators.survival.rank_and_crowding import RankAndCrowding
from pymoo.operators.mutation.pm import PolynomialMutation
from pymoo.termination import get_termination
# from pymoo.termination import MultiObjectiveTermination
import numpy as np



# Setup the optimizer 
# Now accepts optional "callback_instance" (for progress bar)
def MotorOpt(MotorCalcs, params, MagnetBr_T, MaxBMagnetIron_T, PresentBLaminationBackIron_T, eng, Real, Integer, Choice, Binary, OptimizationConf, callback_instance=None):
    MinEff_ = OptimizationConf.get("MinEff_")
    MaxWeight_kg = OptimizationConf.get("MaxWeight")
    VDC = OptimizationConf.get("VDC")
    MinTor_Nm_str = OptimizationConf.get("MinTor")
    SpeedReq_rpm_str = OptimizationConf.get("SpeedReq")
    # print('SpeedReq_rpm_str')
    # print(SpeedReq_rpm_str)
    Tor_numbers = MinTor_Nm_str.split(',')
    MinTor_Nm = [float(num) for num in Tor_numbers]
    Speed_numbers = SpeedReq_rpm_str.split(',')
    SpeedReq_rpm = [float(num) for num in Speed_numbers]    
    
    #MinTor_Nm = np.array(MinTor_Nm)
    #SpeedReq_rpm = np.array(SpeedReq_rpm)
    
    NumPts = len(SpeedReq_rpm)
    
    NumInEqConst_ = NumPts +5    # number of inequality constraints
    NumEqConst_ = 0       # number of equality constraints   
    NumObj_ = 0           # number of objectives
    if OptimizationConf.get("TorqueOpt") == True: 
        NumObj_ = NumObj_+NumPts
    if OptimizationConf.get("Efficinecy_minOpt") == True:
        NumObj_ = NumObj_+1
    if OptimizationConf.get("Efficinecy_maxOpt") == True: 
        NumObj_ = NumObj_+1
    if OptimizationConf.get("WeightOpt") == True: 
        NumObj_ = NumObj_+1
    if OptimizationConf.get("MagWeightOpt") == True: 
        NumObj_ = NumObj_+1
    if OptimizationConf.get("VoltageOpt") == True: 
        NumObj_ = NumObj_+1
    if OptimizationConf.get("MtrLengthOpt") == True: 
        NumObj_ = NumObj_+1
    if OptimizationConf.get("MtrRadiusOpt") == True: 
        NumObj_ = NumObj_+1
    print(f"Number of Speed Points (NumPts): {NumPts}")
    print(f"Calculated Number of Objectives (NumObj_): {NumObj_}")
    if NumObj_ <= 0:
        raise ValueError("Optimization requires at least one objective function to be selected in OptimizationConf. NumObj_ is currently 0.")

    class Optimizer(ElementwiseProblem):
    
        def __init__(self, params, NumObj_, NumEqConst_, NumInEqConst_, OptimizationConf, verbose=False, **kwargs):
            self.verbose = verbose
            
            # break `params` into `vars` and `consts`
            #############################
            self.vars = dict()
            self.consts = dict()
            for key, value in params.items():
                if type(value) in [Real, Integer, Binary, Choice]:
                    self.vars[key]=value
                else:
                    self.consts[key]=value
            # print(self.vars) 
            # print(self.vars.keys()) 
            # print(self.vars.values()) 
            # print(self.consts)
            
            # initialize the problem by defining the number of onjectives and the number of constraints
            #############################        
            super().__init__(vars=self.vars,
                             n_obj=NumObj_,
                             n_ieq_constr=NumInEqConst_,
                             n_eq_constr=NumEqConst_,
                             **kwargs)
    
        # call the `_evaluate` function to calculate the objectives and contraints
        #############################
        def _evaluate(self, x, out, *args, **kwargs):

            out["F"], out["G"] = MotorCalcs(x, OptimizationConf, MinEff_, MinTor_Nm, MaxWeight_kg, VDC, MagnetBr_T, MaxBMagnetIron_T, PresentBLaminationBackIron_T, SpeedReq_rpm, eng,OptimizationConf,NumObj_)
    npop = OptimizationConf.get("npop")
    ngens = OptimizationConf.get("ngens")
    nprocesses = OptimizationConf.get("nprocesses")
    DisMut = OptimizationConf.get("DisMut")
    ProbMut = OptimizationConf.get("ProbMut")
            
    # Set up the mutation operator
    # ProbMut = 0.1 means 10% chance that a gene will be mutated. higher number =  higher exploration
    # DisMut Low eta (e.g., < 1): Increases the likelihood of larger mutations, which can help in exploring the solution space more broadly.
    # DisMut Moderate eta (e.g., 1 to 20): Balances exploration and exploitation, making it suitable for many optimization tasks.
    # DisMut High eta (e.g., > 20): Results in smaller mutations, refining the solutions and focusing on local search. This can be useful in the later stages of optimization when you want to fine-tune solutions.
    
    mutation = PolynomialMutation(prob=ProbMut, eta=DisMut)    
    
    algorithm = MixedVariableGA(
        pop_size=npop, 
        survival=RankAndCrowding(crowding_func="cd"),
        mutation=mutation
    )
    
    termination = DefaultMultiObjectiveTermination(
        xtol=1e-3,
        cvtol=1e-3,
        ftol=1e-3,
        n_max_gen=ngens,
        n_max_evals=50000
    )
    
    problem = Optimizer(params,NumObj_,NumEqConst_,NumInEqConst_,OptimizationConf)
    
    # Run optimizer (objective function minimizer)
    res = minimize(
        problem,
        algorithm,
        termination,
        n_processes=nprocesses,
        verbose=True,
        save_history=False,
        callback=callback_instance
    )
    
    # check if there is no feasible solution
    if res.F is None:
        print("There is no solution. Consider relaxing the constraints")
    
    return res