import traceback
from PySide2.QtCore import QObject, Signal, Slot
from gui.progress_callback import ProgressCallback #, OperationCancelledError (if using exception model)


class OptimizationWorker(QObject):
    progress_signal = Signal(int)
    finished_signal = Signal(object)
    error_signal = Signal(str)
    table_update_data = Signal(dict)

    def __init__(self, motor_calcs_func, motor_params_pymoo, opt_conf, other_args, motor_opt_func):
        super().__init__()
        self.motor_calcs_func = motor_calcs_func
        self.motor_params_pymoo = motor_params_pymoo
        self.opt_conf = opt_conf
        self.other_args = other_args
        self.ngens = opt_conf.get("ngens", 0)
        self.motor_opt_func = motor_opt_func
        self._is_stop_requested = False

    @Slot()
    def request_stop(self):
        print("OptimizationWorker: Stop request received.")
        self._is_stop_requested = True

    def get_stop_state(self):
        return self._is_stop_requested

    @Slot()
    def run_optimization(self):
        try:
            if self._is_stop_requested:
                print("Worker: Optimization not started as stop was already requested.")
                self.error_signal.emit("Optimization cancelled by user before starting.")
                return

            print("Worker thread starting optimization...")
            # Pass a lambda to the callback that checks our internal stop flag
            callback = ProgressCallback(
                self.progress_signal,
                self.ngens,
                stop_checker_func=self.get_stop_state
            )
            callback.new_data_point.connect(self.table_update_data)

            mag_br, max_b_mag, pres_b_lam, eng, R, I, Ch, B = self.other_args

            results = self.motor_opt_func(
                self.motor_calcs_func,
                self.motor_params_pymoo,
                mag_br, max_b_mag, pres_b_lam,
                eng, R, I, Ch, B,
                self.opt_conf,
                callback_instance=callback # This callback signals Pymoo via return True
            )

            # After motor_opt_func returns, check if it was due to a stop request
            if self._is_stop_requested:
                print("Worker: Optimization process was stopped by user.")
                # Even if Pymoo returns results, if a stop was requested,
                # we treat it as a user-initiated stop.
                # The main GUI expects an error_signal in this case.
                self.error_signal.emit("Optimization stopped by user.")
            else:
                print("Worker thread finished optimization normally.")
                self.finished_signal.emit(results)

        # This specific error might be raised if ProgressCallback.update() raises it
        # and MotorOpt doesn't catch it. If using Pymoo's callback return True, this isn't needed.
        # except OperationCancelledError as oce:
        #     print(f"Worker: Optimization explicitly cancelled via OperationCancelledError: {oce}")
        #     self.error_signal.emit(str(oce))
        except Exception as e:
            # If a stop was requested and an unrelated error occurs, prioritize the stop message
            # if it happened because the stop caused an unclean exit.
            # However, usually, the error 'e' would be more specific.
            if self._is_stop_requested:
                print(f"Worker: Error during optimization after stop requested: {e}")
                detailed_error = traceback.format_exc()
                self.error_signal.emit(f"Optimization stopped with error: {e}\n---\n{detailed_error}")
            else:
                print(f"Error in worker thread: {e}")
                detailed_error = traceback.format_exc()
                self.error_signal.emit(f"Optimization failed: {e}\n---\n{detailed_error}")