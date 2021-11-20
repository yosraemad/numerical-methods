from tkinter import *
from tkinter.filedialog import askopenfilename
import sys

sys.path.append('./methods')

from Bisection import Bisection
from FalsePosition import FalsePosition
from FixedPoint import FixedPoint
from NewtonRaphson import NewtonRaphson
from Secant import Secant

root = Tk()

options = ['Bisection', 'False Position', 'Fixed Point', 'Newton Raphson', 'Secant']

chosen = StringVar(root)
chosen.set(options[0])

function = StringVar(root)
precision = StringVar(root)
maxIterations = StringVar(root)


def read_from_file():
    filename = askopenfilename()
    file = open(filename, "r")
    text = file.read()
    file.close()


def submit():
    if chosen.get() == 'Bisection':
        Bisection(function, precision, maxIterations)
    elif chosen.get() == 'False Position':
        FalsePosition(function, precision, maxIterations)
    elif chosen.get() == 'Fixed Point':
        FixedPoint(function, precision, maxIterations)
    elif chosen.get() == 'Newton Raphson':
        NewtonRaphson(function, precision, maxIterations)
    elif chosen.get() == 'Secant':
        Secant(function, precision, maxIterations)
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
Entry(root, width=30, textvariable=maxIterations).grid(row=2, column=3)

Button(root, text="Submit", command=submit).grid(row=3, column=0)

mainloop()
