from function_details import FunctionDetails


def false_position(fun_details: FunctionDetails):
    xl = fun_details.initial_guess
    xu = fun_details.initial_guess + 1

    fx = fun_details.calc_function

    count = 0
    error = 100
    x_prev = 0
    xr = 0
    while count < fun_details.max_iterations and error > fun_details.precision:

        fu = fx(xu)
        fl = fx(xl)
        xr = (xl * fu + xu * fl) / (fu - fl)
        fxr = fx(xr)

        if fxr == 0:
            return xr
        elif fxr > 0:
            xu = xr
        else:
            xl = xr

        error = (xr - x_prev) / xr

        count += 1
        x_prev = xr

    return xr
