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
precision = StringVar(root)
max_iterations = StringVar(root)


def read_from_file():
    filename = askopenfilename()
    file = open(filename, "r")
    text = file.read()
    file.close()


def submit():

    # TODO: TAKE INITIAL GUESS FROM THE GUI
    initial_guess = 0
    fun_details = FunctionDetails(function, precision, max_iterations, initial_guess)

    if chosen.get() == 'Bisection':
        bisection(fun_details)
    elif chosen.get() == 'False Position':
        false_position(fun_details)
    elif chosen.get() == 'Fixed Point':
        fixed_point(fun_details)
    elif chosen.get() == 'Newton Raphson':
        newton_raphson(fun_details)
    elif chosen.get() == 'Secant':
        secant(fun_details)
    else:
        print("Invalid")


root.title("Behaviour of Numerical Methods")
root.geometry("800x600")

Label(root, text="Enter a function:").grid(row=0, column=0)
Entry(root, width=60, textvariable=function).grid(row=0, column=1)
Button(root, text="Choose a file", command=read_from_file).grid(row=0, column=2)

Label(root, text="Choose a method").grid(row=1, column=0)
OptionMenu(root, chosen, *options).grid(row=1, column=1)

# TODO: MAKE SURE THAT THE USER CAN ONLY ENTER NUMBERS
Label(root, text="Precision:").grid(row=2, column=0)
Entry(root, width=30, textvariable=precision).grid(row=2, column=1)

Label(root, text="Max Number of Iterations:").grid(row=2, column=2)
Entry(root, width=30, textvariable=max_iterations).grid(row=2, column=3)

Button(root, text="Submit", command=submit).grid(row=3, column=0)

mainloop()
