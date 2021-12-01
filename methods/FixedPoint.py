from function_details import calc_relative_error, FunctionDetails
import time


def fixed_point(fun_details: FunctionDetails):
    start_time = time.time()
    precision = fun_details.precision
    max_iterations = fun_details.max_iterations
    xold = fun_details.initial_guess1
    count = 0
    error = 100
    while count < max_iterations and error > precision:
        x = fun_details.calc_g_function(xold)
        fx = fun_details.calc_function(x)
        error = calc_relative_error(xold, x)
        details = ""
        fun_details.add_iteration_result(count, xold, x, fx, error, details)

        count += 1
        xold = x

    fun_details.showResult("Fixed Point", time.time() - start_time)
    return x
