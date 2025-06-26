import numpy as np
from pymoo.core.callback import Callback
from PySide2.QtCore import Signal
from PySide2.QtCore import QObject

class ProgressCallback(QObject, Callback): 
    new_data_point = Signal(dict) 

    def __init__(self, progress_signal, total_generations_hint, stop_checker_func=None):
        QObject.__init__(self)
        Callback.__init__(self)
        self.progress_signal = progress_signal 
        self._stop_checker_func = stop_checker_func
        self.current_generation = 0
        # self.headers_sent = False # Not needed if MainWindow sets headers

    def notify(self, algorithm, **kwargs):
        self.notifyProgress(algorithm)
        self.notifyTable(algorithm)
        return self.notifyStop(algorithm)

    # update progress bar
    def notifyProgress(self, algorithm):
        self.current_generation = algorithm.n_gen
        if self.progress_signal:
             self.progress_signal.emit(self.current_generation)


    # Update table 
    def notifyTable(self, algorithm):
        # --- Prepare data for the table ---
        data_dict = {}
        data_dict['n_gen'] = algorithm.n_gen
        data_dict['n_eval'] = algorithm.evaluator.n_eval
        opt = algorithm.opt # Non-dominated solutions
        pop = algorithm.pop # Current population

        data_dict['n_nds'] = len(opt) if opt is not None and opt.size > 0 else 0

        pop_cv = pop.get("CV")
        if pop_cv is not None and pop_cv.ndim > 0 and pop_cv.size > 0:
            # Pymoo CV is often already a scalar per individual, <=0 is feasible
            flat_pop_cv = pop_cv.flatten()
            data_dict['cv_min'] = np.min(flat_pop_cv)
            data_dict['cv_avg'] = np.mean(flat_pop_cv)
        else:
            data_dict['cv_min'] = 0.0
            data_dict['cv_avg'] = 0.0
        
        n_obj = algorithm.problem.n_obj
        opt_f = opt.get("F") if opt is not None and opt.size > 0 else None

        for i in range(n_obj):
            obj_key_min = f"obj{i+1}_min"
            obj_key_max = f"obj{i+1}_max"
            obj_key_avg = f"obj{i+1}_avg"
            if opt_f is not None and opt_f.shape[0] > 0:
                data_dict[obj_key_min] = np.min(opt_f[:, i])
                data_dict[obj_key_max] = np.max(opt_f[:, i])
                data_dict[obj_key_avg] = np.mean(opt_f[:, i])
            else: # No non-dominated solutions yet, or single objective not in opt.F in expected way
                # Fallback to population stats if opt is empty for early generations?
                # For now, NaN or None if opt is empty
                data_dict[obj_key_min] = np.nan 
                data_dict[obj_key_max] = np.nan
                data_dict[obj_key_avg] = np.nan
        
        self.new_data_point.emit(data_dict)

    # Stop algorithm (user pressend STOP)
    def notifyStop(self, algorithm):
        if self._stop_checker_func and self._stop_checker_func():
            print("ProgressCallback.notify: Stop request detected by stop_checker_func.")
            print(f"  Algorithm object ID in callback: {id(algorithm)}") # For debugging
            print(f"  Current algorithm generation: {algorithm.n_gen}, evaluations: {algorithm.evaluator.n_eval}")

            # Attempt 1: Direct flag on the algorithm instance passed to callback
            print(f"  Setting algorithm.state_if_terminated = True")
            algorithm.state_if_terminated = True

            # Attempt 2: Modify termination criteria directly (more forceful, can be hacky)
            if algorithm.termination is not None:
                print(f"  Forcing algorithm.termination flags if possible.")
                if hasattr(algorithm.termination, 'force_termination'): # Some custom terminations might have this
                    algorithm.termination.force_termination = True
                # For DefaultMultiObjectiveTermination, try to make it think it's done
                if hasattr(algorithm.termination, '_n_max_gen_val') and algorithm.termination._n_max_gen_val is not None:
                     #This is an internal Pymoo variable, use with caution
                     print(f"  Setting termination's max_gen to current gen via internal var _n_max_gen_val")
                     algorithm.termination._n_max_gen_val = algorithm.n_gen
                elif hasattr(algorithm.termination, 'n_max_gen') and algorithm.termination.n_max_gen is not None: # For basic termination
                    print(f"  Setting termination's n_max_gen to current gen")
                    algorithm.termination.n_max_gen = algorithm.n_gen
            print("  Returning True from callback.notify to stop Pymoo minimize loop.")
            return True 

        return False
