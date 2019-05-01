import numpy as np
from numpy.polynomial import Polynomial as npp
import re

#------------------------------------------------------------
# functions for processing input/output
#------------------------------------------------------------


def loadData(infile):
    """Return a dictionary of temperature data."""
    with open(infile) as inf:
        cores = [dict(), dict(), dict(), dict()]
        time = 0
        for line in inf:
            temps = [makeFloat(val) for val in line.split()]
            for val in temps:
                i = temps.index(val)
                cores[i].setdefault(time, val)
            time += 30
    return cores


def testerData():
    """generate data with known correct answers"""
    # based on wk10 lecture notes
    # correct least-squares: p = -2 + 6x
    # correct piecewise linear: [2x, 6x-4, 10x-12]
    x = [0, 1, 2, 3]
    y = [0, 2, 8, 18]

    cores = [dict(), dict(), dict(), dict()]
    for i in range(0, 4):
        for j in range(0, 4):
            cores[j].setdefault(x[i], y[i])
    return cores


def testerData2():

    # based on 'Numerical Analysis', Burden, p. 144
    # correct cubic spline:
    # [ 2 + 3/4(x-1) + 1/4(x-1)^3,
    #   3 + 3/2(x-2) + 3/4(x-2)^2 - 1/4(x-2)^3 ]
    x = [1, 2, 3]
    y = [2, 3, 5]

    cores = [dict(), dict(), dict(), dict()]
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            cores[j].setdefault(x[i], y[i])
    return cores


def makeFloat(string):
    pattern = re.compile("[+-]*\\d+(\\.\\d+)*")
    result = pattern.match(string)
    if(result):
        return float(result.group())
    return None


def printPoly(npPoly):
    # print(npPoly)
    print("Xk <= X < Xk+1; Yk = C0 + C1X; type")


def printData(data):
    """Print the input data in a table."""
    print("time(sec)\ttemperature (C)")
    print("\t\tC1\t  C2\t    C3\t      C4")
    for time in data[0].keys():
        print("%d\t\t%f %f %f %f" % (time, data[0][time], data[1][time], data[2][time], data[3][time]))


#------------------------------------------------------------
# functions for least-squares approximation
#------------------------------------------------------------


def leastSquares(dataset, n=2):
    x = [x for x in dataset]
    y = [dataset[x] for x in dataset]

    A = np.array([makeRow(i, x) for i in range(0, n)])
    b = np.array([makeRowinb(i, x, y) for i in range(0, n)])

    c = np.linalg.lstsq(A, b, rcond=None)

    return c[0]


def basisPi(n, x):
    if n == 0:
        return 1
    return x


def sumPIiPIj(i, j, x):
    k = len(x)
    PIiPIj = [basisPi(i, x[r]) * basisPi(j, x[r]) for r in range(0, k)]
    return sum(PIiPIj)


def makeRow(i, x):
    return [sumPIiPIj(i, j, x) for j in range(0, 2)]


def makeRowinb(i, x, y):
    k = len(x)
    PIiY = [basisPi(i, x[r]) * y[r] for r in range(0, k)]
    return [sum(PIiY)]


#------------------------------------------------------------
# functions for piecewise approximation
#------------------------------------------------------------


def linear(dataset):

    result = []
    x0, y0 = (None, None)
    x1, y1 = (None, None)

    for (x, y) in dataset.items():
        if x0 is None:
            x0, y0 = (x, y)
            continue
        x1, y1 = (x, y)
        c0 = y0 / (x0 - x1)
        c1 = y1 / (x1 - x0)
        px = npp([(-c0 * x1), c0]) + npp([(-c1 * x0), c1])
        result.append(px.coef)
        x0, y0 = (x, y)
    return result


def cubicSpline(dataset):

    def toString():
        return "cat"

    result = dict()
    p0 = p1 = p2 = None
    i = 0

    for (x, y) in dataset.items():
        if p0 is None:
            p0 = (x, y)
            continue
        if p1 is None:
            p1 = (x, y)
            continue
        p2 = (x, y)
        s0, s1 = solveMatrix(p0, p1, p2)
        result.setdefault(i, s0)
        i += 1
        result.setdefault(i, s1)
        p0 = p1
        p1 = p2
    return list(result.values())


def piecewise(dataset, approximation=linear):
    functions = approximation(dataset)
    apxType = approximation.__name__

    for function in functions:
        print("Xk <= X < Xk+1; Yk = C0 + C1X; %s" % apxType)

    return functions


def solveMatrix(p0, p1, p2):

    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2

    A = np.array((
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, (x1 - x0), ((x1 - x0) ** 2), ((x1 - x0) ** 3), 0, 0, 0, 0],
        [0, 0, 0, 0, 1, (x2 - x1), ((x2 - x1) ** 2), ((x2 - x1) ** 3)],
        [0, 1, (2 * (x1 - x0)), (3 * ((x1 - x0) ** 2)), 0, -1, 0, 0],
        [0, 0, 2, (6 * ((x1 - x0) ** 2)), 0, 0, -2, 0],
        [0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, (6 * ((x2 - x1) ** 2))]
    ))

    b = np.array((
        [y0],
        [y1],
        [y1],
        [y2],
        [0],
        [0],
        [0],
        [0]
    ))

    c = np.linalg.lstsq(A, b, rcond=None)
    c0 = c[0][0:4]
    c1 = c[0][4:8]

    return (c0, c1)


def printLSQ(dataset, approximation=leastSquares):
    functions = approximation(dataset)
#    apxType = approximation.__name__

    for function in functions:
        print(function)
#        print("Xk <= X < Xk+1; Yk = C0 + C1X; %s" % apxType)

    return functions
