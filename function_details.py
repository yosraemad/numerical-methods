class FunctionDetails:


    def __init__(self, function_string, precision, max_iterations, initial_guess1 = None, initial_guess2 = None):
        self.function_string = function_string
        self.precision = precision
        self.max_iterations = max_iterations
        self.initial_guess1 = initial_guess1
        self.initial_guess2 = initial_guess2

    def calc_function(self, x: float):
        fun_with_val = self.function_string
        return eval(fun_with_val)
