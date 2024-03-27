from colors import bcolors
import sympy as sp
from sympy.utilities.lambdify import lambdify


def newton_raphson(f, df, interval, x0, TOL, N=50):

    a, b = interval
    for i in range(N):
        if df(x0) == 0:
            print("Derivative is zero at x0, method cannot continue (can not divide by zero)")
            return

        x1 = x0 - f(x0) / df(x0)

        if abs(x1 - x0) < TOL:

            if abs(x1 - x0) < TOL:
                if a <= x1 <= b: # check if root is within the given interval
                    return x1, i
                else:
                    return None, None

            if not (a <= x1 <= b):
                return None, None

        x0 = x1
    return x1, N


def calc_newton_raphson():
    x = sp.symbols('x')
    f = x ** 3 + 8
    df = f.diff(x)

    f = lambdify(x, f)
    df = lambdify(x, df)

    x0 = 8
    TOL = 0.0001
    N = 100
    interval = (-19, 10)

    roots, iteration = newton_raphson(f, df, interval, x0, TOL, N)
    if roots is None or iteration is None:
        print("Root could not be found within the given interval.")
    else:
        print(bcolors.OKBLUE,"-------------------------------------------------------(newton_raphson)--------------------------------------------------------------")
        print(bcolors.HEADER, "\nThe root of the equation f(x) is approximately" + f" x = {roots}")
        print(bcolors.HEADER, "\nnumber of iteration: " + str(iteration))
        print(bcolors.OKBLUE,"------------------------------------------------------------------------------------------------------------------------------------")



