from tkinter.constants import TRUE


def f(x):
    return x ** 4 - 2 * x ** 3 - 4 * x ** 2 - 4 * x + 4


def secant(fun_details):
    precision = float(0.01)
    max_iterations = 10
    print("Secant\n")

    iteration = 0
    xl = float(-1)
    xu = float(0)
    xold = 0

    while TRUE:

        if f(xu) == f(xl):
            print('Error! division by zero')
            break

        iteration += 1

        x = float(xl - f(xl) * (xu - xl) / (f(xu) - f(xl)))
        error = float(abs(x - xold) / abs(x))

        print('iteration %d  a= %0.10f  b= %0.10f  f(a)= %0.10f  f(b)= %0.10f  x= %0.10f  error= %0.10f\n' % (
            iteration, xl, xu, f(xl), f(xu), x, error))

        if iteration >= max_iterations or error < precision:
            print('Approximate root is %0.10f' % x)
            break

        xl = xu
        xu = x
        xold = x
