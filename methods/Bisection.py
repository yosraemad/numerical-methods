from function_details import FunctionDetails


def bisection(fun_details: FunctionDetails):
    xl = fun_details.initial_guess1
    xu = fun_details.initial_guess2

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

        error = abs(xr - x_prev) / abs(xr)
        x_prev = xr
        count += 1
    return xr
