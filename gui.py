from tkinter import *
from tkinter.filedialog import askopenfilename
import sys
from function_details import FunctionDetails

sys.path.append('./methods')

from Bisection import bisection
from FalsePosition import false_position
from FixedPoint import fixed_point
from NewtonRaphson import newton_raphson
from Secant import secant

root = Tk()

options = ['Bisection', 'False Position', 'Fixed Point', 'Newton Raphson', 'Secant']

chosen = StringVar(root)
chosen.set(options[0])

function = StringVar(root)
precision = DoubleVar(root)
max_iterations = IntVar(root)
initial_guess1 = DoubleVar(root)
initial_guess2 = DoubleVar(root)


def read_from_file():
    filename = askopenfilename()
    file = open(filename, "r")
    function = file.read()
    file.close()


def submit():
    initial_guess = 0
    fun_details = FunctionDetails(function.get(), float(precision.get()), int(max_iterations.get()),
                                  initial_guess1.get(), initial_guess2.get())

    if chosen.get() == 'Bisection':
        xr = bisection(fun_details)
    elif chosen.get() == 'False Position':
        xr = false_position(fun_details)
    elif chosen.get() == 'Fixed Point':
        fixed_point(fun_details)
    elif chosen.get() == 'Newton Raphson':
        newton_raphson(fun_details)
    elif chosen.get() == 'Secant':
        secant(fun_details)
    else:
        print("Invalid")


initialGuess1Label = Label(root, text="Initial Guess 1:")
initialGuess1Entry = Entry(root, width=30, textvariable=initial_guess1)
initialGuess2Label = Label(root, text="Initial Guess 2:")
initialGuess2Entry = Entry(root, width=30, textvariable=initial_guess2)


def showInitialGuess(chosen):
    if chosen == 'Bisection' or chosen == 'False Position':
        initialGuess1Label.grid(row=3, column=0)
        initialGuess1Entry.grid(row=3, column=1)
        initialGuess2Label.grid(row=3, column=2)
        initialGuess2Entry.grid(row=3, column=3)
    elif chosen == 'Newton Raphson':
        initialGuess1Label.grid(row=3, column=0)
        initialGuess1Entry.grid(row=3, column=1)
        initialGuess2Label.grid_remove()
        initialGuess2Entry.grid_remove()
    else:
        initialGuess1Entry.grid_remove()
        initialGuess2Entry.grid_remove()
        initialGuess1Label.grid_remove()
        initialGuess2Label.grid_remove()


showInitialGuess(chosen.get())

root.title("Behaviour of Numerical Methods")
root.geometry("800x600")

Label(root, text="Enter a function:").grid(row=0, column=0)
Entry(root, width=60, textvariable=function).grid(row=0, column=1)
Button(root, text="Choose a file", command=read_from_file).grid(row=0, column=2)

Label(root, text="Choose a method").grid(row=1, column=0)
OptionMenu(root, chosen, *options, command=showInitialGuess).grid(row=1, column=1)

# TODO: MAKE SURE THAT THE USER CAN ONLY ENTER NUMBERS
Label(root, text="Precision:").grid(row=2, column=0)
Entry(root, width=30, textvariable=precision).grid(row=2, column=1)

Label(root, text="Max Number of Iterations:").grid(row=2, column=2)
Entry(root, width=30, textvariable=max_iterations).grid(row=2, column=3)

Button(root, text="Submit", command=submit).grid(row=4, column=0)

mainloop()
