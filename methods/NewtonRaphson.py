from function_details import FunctionDetails, calc_relative_error
import time


def newton_raphson(fun_details: FunctionDetails):
    start_time = time.time()
    # TODO: USE THE INITIAL GUESS
    x = fun_details.initial_guess1

    count = 0
    error = 100
    x_prev = 0.0
    while count < fun_details.max_iterations and error > fun_details.precision:

        f_dash = fun_details.diff_f_at_point(x)
        fx = fun_details.calc_function(x)

        x = x_prev - (fx / f_dash)

        error = calc_relative_error(x_prev, x)

        details = "f`(x)= {}".format(f_dash)
        fun_details.add_iteration_result(count, x_prev, x, fx, error, details)

        if fx == 0:
            return x

        count += 1
        x_prev = x

    fun_details.showResult("Newton Raphson", time.time() - start_time)
    return x
