from function_details import calc_relative_error, FunctionDetails
import time
import ctypes
from random import random

def fixed_point(fun_details: FunctionDetails):
    if(fun_details.calc_function(random()) == None):
        ctypes.windll.user32.MessageBoxW(0, "Please enter a valid function", "Error", 0)
        return
    start_time = time.time()
    precision = fun_details.precision
    max_iterations = fun_details.max_iterations
    xold = float(fun_details.initial_guess1)
    count = 0
    error = 100
    while count < max_iterations and error > precision:
        x = fun_details.calc_g_function(xold)
        fx = fun_details.calc_function(x)
        error = calc_relative_error(xold, x)
        details = ""
        fun_details.add_iteration_result(count, xold, x, fx, error, details)

        if fx == 0:
            return x
        count += 1
        xold = x

    end_time = time.time()
    fun_details.showResult("Fixed Point", end_time - start_time)
    return x
