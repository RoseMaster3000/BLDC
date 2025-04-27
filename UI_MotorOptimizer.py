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
from pymoo.core.callback import Callback
import numpy as np

# https://pymoo.org/interface/callback.html?highlight=callback
class ProgressCallback(QObject, Callback): # Inherit from QObject FIRST
    progress_updated = Signal(int) # Signal to emit progress percentage

    def __init__(self, total_gens: int) -> None:
        # Need explicit calls to both parent constructors
        QObject.__init__(self)
        Callback.__init__(self)
        self.data["best_f"] = []
        # Store total generations to calculate percentage
        self.total_gens = max(1, total_gens) # Avoid division by zero

    # The notify method is called after each generation
    @Slot(object) # Decorate if necessary, though usually not required for internal calls
    def notify(self, algorithm, **kwargs):
        # Access algorithm properties
        current_gen = algorithm.n_gen
        pop_size = algorithm.pop_size

        # Calculate progress
        progress_percent = int((current_gen / self.total_gens) * 100)
        # Emit the signal
        self.progress_updated.emit(progress_percent)

        # Keep your existing logic if needed
        if algorithm.opt is not None and len(algorithm.opt) > 0:
             # Check if opt is populated and has elements
            best_solution_so_far = algorithm.opt.get("F")[0] # Get the best objective value
            self.data["best_f"].append(best_solution_so_far)
            print(f"Generation: {current_gen}/{self.total_gens}, Pop Size: {pop_size}, Best Objective: {best_solution_so_far:.4f}, Progress: {progress_percent}%")
        else:
            # Handle cases where optimization hasn't found a feasible solution yet or it's the very start
             print(f"Generation: {current_gen}/{self.total_gens}, Pop Size: {pop_size}, Progress: {progress_percent}% (No feasible solution yet)")


# Setup the optimizer
def MotorOpt(MotorCalcs, params, MagnetBr_T, MaxBMagnetIron_T, PresentBLaminationBackIron_T, eng, Real, Integer, Choice, Binary, OptimizationConf, callback_instance): # Added callback_instance
    """
    This script sets up and runs the GA Optimizer

    Inputs:
        MotorCalcs: Function for motor performance calculations.
        params: Dictionary of model parameters.
        OptimizationConf: Dictionary with optimization settings.
        callback_instance: An instance of ProgressCallback (or similar QObject with progress signal).
        ... other inputs ...

    Outputs:
        res: Optimization results
    """
    # --- Extract parameters from OptimizationConf ---
    MinEff_ = OptimizationConf.get("MinEff_")
    MaxWeight_kg = OptimizationConf.get("MaxWeight")
    VDC = OptimizationConf.get("VDC")
    MinTor_Nm_str = OptimizationConf.get("MinTor")
    SpeedReq_rpm_str = OptimizationConf.get("SpeedReq")
    npop = OptimizationConf.get("npop")
    ngens = OptimizationConf.get("ngens")
    nprocesses = OptimizationConf.get("nprocesses")
    DisMut = OptimizationConf.get("DisMut")
    ProbMut = OptimizationConf.get("ProbMut")

    # --- Process input strings ---
    Tor_numbers = MinTor_Nm_str.split(',')
    MinTor_Nm = np.array([float(num) for num in Tor_numbers])
    Speed_numbers = SpeedReq_rpm_str.split(',')
    SpeedReq_rpm = np.array([float(num) for num in Speed_numbers])
    NumPts = len(SpeedReq_rpm)

    # --- Calculate number of constraints and objectives ---
    NumInEqConst_ = NumPts + 5
    NumEqConst_ = 0
    NumObj_ = 0
    if OptimizationConf.get("TorqueOpt"): NumObj_ += NumPts
    if OptimizationConf.get("EfficinecyOpt_min"): NumObj_ += 1
    if OptimizationConf.get("EfficinecyOpt_max"): NumObj_ += 1
    if OptimizationConf.get("WeightOpt"): NumObj_ += 1
    if OptimizationConf.get("MagWeightOpt"): NumObj_ += 1
    if OptimizationConf.get("VoltageOpt"): NumObj_ += 1
    if OptimizationConf.get("MtrLengthOpt"): NumObj_ += 1
    if OptimizationConf.get("MtrRadiusOpt"): NumObj_ += 1
    print(f"Number of Operating Points: {NumPts}")
    print(f"Number of Objectives: {NumObj_}")

    # --- Define the Pymoo Problem ---
    class Optimizer(ElementwiseProblem):
        def __init__(self, params, NumObj_, NumEqConst_, NumInEqConst_, OptimizationConf, verbose=False, **kwargs):
            self.verbose = verbose
            self.vars = dict()
            self.consts = dict()
            for key, value in params.items():
                # Check if value is a Pymoo variable type (needs Real, Integer etc. defined)
                # Assuming Real, Integer, Choice, Binary are types/classes from Pymoo
                # Make sure these types are correctly passed or imported
                if isinstance(value, (Real, Integer, Binary, Choice)):
                    self.vars[key]=value
                else:
                    self.consts[key]=value

            super().__init__(vars=self.vars,
                             n_obj=NumObj_,
                             n_ieq_constr=NumInEqConst_,
                             n_eq_constr=NumEqConst_,
                             **kwargs)

        def _evaluate(self, x, out, *args, **kwargs):
            # Ensure all necessary arguments are passed to MotorCalcs
            # Note: OptimizationConf is passed twice in the original code, check if intentional
             out["F"], out["G"] = MotorCalcs(x, self.consts, MinEff_, MinTor_Nm, MaxWeight_kg, VDC, MagnetBr_T, MaxBMagnetIron_T, PresentBLaminationBackIron_T, SpeedReq_rpm, eng, OptimizationConf, NumObj_)


    # --- Setup Algorithm ---
    mutation = PolynomialMutation(prob=ProbMut, eta=DisMut)
    algorithm = MixedVariableGA(
        pop_size=npop,
        survival=RankAndCrowding(crowding_func="cd"),
        mutation=mutation
        # Add sampling and crossover if needed for mixed variables
        # sampling=MixedVariableSampling(),
        # crossover=MixedVariableCrossover()
    )

    # --- Setup Termination ---
    termination = DefaultMultiObjectiveTermination(
        xtol=1e-3,
        cvtol=1e-3,
        ftol=1e-3,
        n_max_gen=ngens,
        n_max_evals=50000 # Consider if this should also be configurable
    )

    # --- Create Problem Instance ---
    problem = Optimizer(params, NumObj_, NumEqConst_, NumInEqConst_, OptimizationConf)

    # --- Run Optimizer ---
    # Pass the provided callback_instance here
    print("Starting optimization...")
    res = minimize(problem,
                   algorithm,
                   termination,
                   # n_processes=nprocesses, # Careful with multiprocessing and Qt Signals
                   seed=1, # Good practice for reproducibility
                   verbose=True,
                   save_history=False, # Set to True if history is needed later
                   callback=callback_instance # Use the passed instance
    )

    # --- Check for results ---
    if res.F is None:
        print("Optimization finished: No feasible solution found. Consider relaxing constraints.")
    else:
        print("Optimization finished successfully.")

    return res