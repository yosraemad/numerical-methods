from function_details import calc_relative_error, FunctionDetails
import time

def secant(fun_details: FunctionDetails):
    start_time = time.time()
    precision = fun_details.precision
    max_iterations = fun_details.max_iterations
    xl = fun_details.initial_guess1
    xu = fun_details.initial_guess2
    xold = 0
    count = 0
    error = 100
    while count < max_iterations and error > precision:
        fxu = fun_details.calc_function(xu)
        fxl = fun_details.calc_function(xl)
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
    fun_details.showResult("Secant", start_time - end_time)
    return x
