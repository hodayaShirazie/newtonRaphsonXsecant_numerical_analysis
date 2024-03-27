from colors import bcolors

def secant_method(f, x0, x1, interval, TOL, N=50):
    a, b = interval
    for i in range(N):
        if f(x1) - f(x0) == 0:
            print("method cannot continue (can not divide by zero)")
            return

        x2 = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))

        if abs(x2 - x1) < TOL:
            if a <= x2 <= b:
                return x2, i
            else:
                return None, None

        if not (a <= x2 <= b):
            return None, None

        x0 = x1
        x1 = x2
    return x2, N


def calc_secant():
    f = lambda x: x ** 3 + 8

    x0 = 19
    x1 = -3
    TOL = 0.0001
    N = 100
    interval = (-19, 10)

    roots, iteration = secant_method(f, x0, x1,interval, TOL, N)

    if roots is None or iteration is None:
        print("Root could not be found within the given interval.")
    else:
        print(bcolors.OKBLUE, "-----------------------------------------------------------(secant)----------------------------------------------------------")
        print(bcolors.HEADER, "\nThe root of the equation f(x) is approximately" + f" x = {roots}")
        print(bcolors.HEADER, "\nnumber of iteration: " + str(iteration))
        print(bcolors.OKBLUE, "-----------------------------------------------------------------------------------------------------------------------------")


