from function_details import FunctionDetails
import sys
sys.path.append('./methods')
from Bisection import bisection
from FalsePosition import false_position
from FixedPoint import fixed_point
from NewtonRaphson import newton_raphson
from Secant import secant

class Submit:
    def __init__(self, function, chosen, precision = 0.01, max_iterations = 20, initial_guess1 = None, initial_guess2 = None):
        self.function = function
        self.precision = precision
        self.max_iterations = max_iterations
        self.initial_guess1 = initial_guess1
        self.initial_guess2 = initial_guess2
        self.chosen = chosen
        self.function_details = FunctionDetails(function, precision, max_iterations, initial_guess1, initial_guess2)
        self.submit()
    
    def submit(self):
        if self.chosen == 'Bisection':
            xr = bisection(self.function_details)
        elif self.chosen == 'False Position':
            xr = false_position(self.function_details)
        elif self.chosen == 'Fixed Point':
            fixed_point(self.function_details)
        elif self.chosen == 'Newton Raphson':
            newton_raphson(self.function_details)
        elif self.chosen == 'Secant':
            xr = secant(self.function_details)
        else:
            print("Invalid")