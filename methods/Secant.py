from function_details import calc_relative_error, FunctionDetails
import time
import ctypes
from random import random

def secant(fun_details: FunctionDetails):
    if(fun_details.calc_function(random()) == None):
        ctypes.windll.user32.MessageBoxW(0, "Please enter a valid function", "Error", 0)
        return
    start_time = time.time()
    precision = fun_details.precision
    max_iterations = fun_details.max_iterations
    xl = float(fun_details.initial_guess1)
    xu = float(fun_details.initial_guess2)
    fxu = fun_details.calc_function(xu)
    fxl = fun_details.calc_function(xl)
    xold = 0
    count = 0
    error = 100
    while count < max_iterations and error > precision:

        if fxu == fxl:
            print('Error! division by zero')
            break
        x = float(xl - fxl * (xu - xl) / (fxu - fxl))
        fx = fun_details.calc_function(x)
        error = calc_relative_error(xold, x)

        details = "Xu: {}, Xl: {}".format(xu, xl)
        fun_details.add_iteration_result(count, xold, x, fx, error, details)

        count += 1
        xl = xu
        xu = x
        xold = x

    end_time = time.time()
    fun_details.showResult("Secant", end_time - start_time)
    return x
