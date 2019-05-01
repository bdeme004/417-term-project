#import numpy as np
from numpy.polynomial import Polynomial as npp
import re


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


# generates data with known correct answers
# based on wk10 lecture notes
# correct least-squares: p = -2 + 6x
# correct piecewise linear: [2x, 6x-4, 10x-12]
def testerData():
    x = [0, 1, 2, 3]
    y = [0, 2, 8, 18]

    cores = [dict(), dict(), dict(), dict()]
    for i in range(0, 4):
        for j in range(0, 4):
            cores[j].setdefault(x[i], y[i])
    return cores


def testerData2():
    """generate data with known correct answers"""
    # based on 'Numerical Analysis', Burden, p. 144
    # correct cubic spline:
    # [RTC]
    x = [0, 1, 2, 3]
    y = [0, 2, 8, 18]

    cores = [dict(), dict(), dict(), dict()]
    for i in range(0, 4):
        for j in range(0, 4):
            cores[j].setdefault(x[i], y[i])
    return cores


def makeFloat(string):
    pattern = re.compile("[+-]*\\d+(\\.\\d+)*")
    result = pattern.match(string)
    if(result):
        return float(result.group())
    return None


def printData(data):
    print("time(sec)\ttemperature (C)")
    print("\t\tC1\t  C2\t    C3\t      C4")
    for time in data[0].keys():
        print("%d\t\t%f %f %f %f" % (time, data[0][time], data[1][time], data[2][time], data[3][time]))


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


def linear(dataset):

    x0, y0 = (None, None)
    x1, y1 = (None, None)

    for (x, y) in dataset.items():
        if x0 is None:
            x0, y0 = (x, y)
            continue
        x1, y1 = (x, y)
        px = doMath(x0, y0, x1, y1)
        printPoly(px)
        x0, y0 = (x, y)


# || rename this ||
# VV    (-_-)    VV
def doMath(x0, y0, x1, y1):
    # print("(%d, %d), (%d, %d)" % (x0, y0, x1, y1))

    c0 = y0 / (x0 - x1)
    c1 = y1 / (x1 - x0)
    px = npp([(-c0 * x1), c0]) + npp([(-c1 * x0), c1])
    return px


def piecewise(dataset, method=linear):
    pass


def printPoly(npPoly):
    print(npPoly)
