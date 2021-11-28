from function_details import FunctionDetails


def false_position(fun_details: FunctionDetails):
    xl = fun_details.initial_guess1
    xu = fun_details.initial_guess2

    fx = fun_details.calc_function

    if fx(xl) * fx(xu) >= 0:
        print("Error: f(xl) and f(xu) have the same sign")
        return

    count = 0
    error = 100
    x_prev = 0.0
    xr = 0.0
    while count < fun_details.max_iterations and error > fun_details.precision:

        fu = fx(xu)
        fl = fx(xl)
        xr = (xl * fu - xu * fl) / (fu - fl)
        fxr = fx(xr)

        if fxr == 0:
            return xr
        elif fxr > 0:
            xu = xr
        else:
            xl = xr

        error = abs(xr - x_prev) / abs(xr)

        count += 1
        x_prev = xr

    return xr
