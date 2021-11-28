from sympy import diff, symbols


def calc_relative_error(x_old: float, x_new: float):
    return float(abs(x_new - x_old) / abs(x_new))


class FunctionDetails:

    def __init__(self, function_string, precision, max_iterations, initial_guess1=None, initial_guess2=None):
        self.function_string = function_string
        self.precision = precision
        self.max_iterations = max_iterations
        self.initial_guess1 = initial_guess1
        self.initial_guess2 = initial_guess2
        self.result_arr = []

    def calc_function(self, x: float):
        fun_with_val = self.function_string
        return eval(fun_with_val)

    def diff_f_at_point(self, x: float):
        f_dash = diff(self.function_string, symbols('x'))
        fun_with_val = f_dash.__str__()
        return eval(fun_with_val)

    def add_iteration_result(self, iteration: int, x_prev: float, x: float, fx: float, error: float, details):
        result_string = "Iteration: {}, Xi: {}, Xi+1: {}, F(Xi+1): {}, Error: {}, {}"\
            .format(iteration, x_prev, x, fx, error, details)
        print(result_string)
        self.result_arr.append(result_string)

