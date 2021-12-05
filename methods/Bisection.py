from function_details import FunctionDetails, calc_relative_error
import time
import ctypes
from random import random


def bisection(fun_details: FunctionDetails):
    if(fun_details.calc_function(random()) == None):
        ctypes.windll.user32.MessageBoxW(0, "Please enter a valid function", "Error", 0)
        return
    start_time = time.time()
    xl = float(fun_details.initial_guess1)
    xu = float(fun_details.initial_guess2)

    xr = 0.0

    fx = fun_details.calc_function
    if fx(xl) * fx(xu) >= 0:
        print("Initial guesses do not bracket a root")
        return

    count = 0
    error = 100
    x_prev = 0.0

    while count < fun_details.max_iterations and error > fun_details.precision:
        fu = fx(xu)
        fl = fx(xl)
        xr = (xl + xu) / 2.0
        fr = fx(xr)

        if fr == 0:
            return xr
        if fl * fr < 0:
            xu = xr
        else:
            xl = xr

        error = calc_relative_error(x_prev, xr)
        x_prev = xr
        count += 1
        fun_details.add_iteration_result(count, x_prev, xr, fr, error, "Xu: {}, Xl: {}, F(Xu): {}, F(Xl): {}".format(xu, xl, fu, fl))

    end_time = time.time()
    fun_details.showResult("Bisection", end_time - start_time)
    return xr
