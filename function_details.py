class FunctionDetails:

    initial_guess = 0

    def __init__(self, function_string, precision, max_iterations, initial_guess):
        self.function_string = function_string
        self.precision = precision
        self.max_iterations = max_iterations
        self.initial_guess = initial_guess

    def calc_function(self, x: int):
        fun_with_val = self.function_string.replace("x", f"({x})")
        return eval(fun_with_val)
