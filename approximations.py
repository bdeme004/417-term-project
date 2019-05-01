import numpy as np
from numpy.polynomial import Polynomial as npp
import re


def load_data(infile):
    """Return a dictionary of temperature data."""
    with open(infile) as inf:
        cores = [dict(), dict(), dict(), dict()]
        time = 0
        for line in inf:
            temps = [make_float(val) for val in line.split()]
            for val in temps:
                i = temps.index(val)
                cores[i].setdefault(time, val)
            time += 30
    return cores


def make_float(string):
    pattern = re.compile("[+-]*\\d+(\\.\\d+)*")
    result = pattern.match(string)
    if(result):
        return float(result.group())
    return None


def print_data(data):
    """Print the input data in a table."""
    print("time(sec)\ttemperature (C)")
    print("\t\tC1\t  C2\t    C3\t      C4")
    for x in data[0].keys():
        print("%d\t\t%f %f %f %f"
              % (x, data[0][x], data[1][x], data[2][x], data[3][x]))


class leastSquares:

    def __init__(self, dataset, n=2):
        x = [x for x in dataset]
        y = [dataset[x] for x in dataset]

        A = np.array([self.make_row(i, x) for i in range(0, n)])
        b = np.array([self.make_row_b(i, x, y) for i in range(0, n)])

        c = np.linalg.lstsq(A, b, rcond=None)
        self.x = x
        self.coef = c[0]

    def basis_PI(self, n, x):
        if n == 0:
            return 1
        return x

    def sum_PIiPIj(self, i, j, x):
        k = len(x)
        PIiPIj = [self.basis_PI(i, x[r]) * self.basis_PI(j, x[r]) for r in range(0, k)]
        return sum(PIiPIj)

    def make_row(self, i, x):
        return [self.sum_PIiPIj(i, j, x) for j in range(0, 2)]

    def make_row_b(self, i, x, y):
        k = len(x)
        PIiY = [self.basis_PI(i, x[r]) * y[r] for r in range(0, k)]
        return [sum(PIiY)]

    def toString(self):
        return ("%d <= x < %d; y = %.3f + %.3fx; least-squares\n"
                % (self.x[0], self.x[-1], self.coef[0], self.coef[1])
                )


class linear:
    def __init__(self, dataset):
        self.coef = []
        self.x = list(dataset.keys())

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
            px.coef.resize((1, 2))
            self.coef.append(px.coef[0])
            x0, y0 = (x, y)

    def toList(self):
        i = 0
        li = []
        for c in self.coef:
            li.append("%d <= x < %d; y%d = %.3f + %.fx; linear interpolation"
                      % (self.x[i], self.x[i + 1], i, c[0], c[1])
                      )
            i += 1
        return li

    def toString(self):
        i = 0
        s = ""
        for c in self.coef:
            s += ("%d <= x < %d; y%d = %.3f + %.3fx; linear interpolation\n"
                  % (self.x[i], self.x[i + 1],
                     i, c[0], c[1])
                  )
            i += 1
        return s


class cubicSpline:
    def __init__(self, dataset):
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
            s0, s1 = self.solve_matrix(p0, p1, p2)
            result.setdefault(i, s0)
            i += 1
            result.setdefault(i, s1)
            p0 = p1
            p1 = p2

            self.coef = list(result.values())
            self.x = list(dataset.keys())

    def solve_matrix(self, p0, p1, p2):

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

    def toList(self):
        i = 0
        li = []
        for c in self.coef:
            # broken up into substrings because it's really long.
            s = ""
            s += "%d <= x < %d;" % (self.x[i], self.x[i + 1])
            s += "y%d = %.3f + %.3f(x-%d)" % (i, c[0], c[1], self.x[i])
            s += " + %.3f(x-%d)^2" % (c[2], self.x[i])
            s += " + %.3f(x-%d)^3" % (c[3], self.x[i])
            s += "; cubic spline interpolation"

            li.append(s)
            i += 1
        return li

    def toString(self):
        i = 0
        s = ""
        for c in self.coef:
            # broken up into substrings because it's really long.
            s += "%d <= x < %d; " % (self.x[i], self.x[i + 1])
            s += "y%d = %.3f + %.3f(x-%d)" % (i, c[0], c[1], self.x[i])
            s += " + %.3f(x-%d)^2" % (c[2], self.x[i])
            s += " + %.3f(x-%d)^3" % (c[3], self.x[i])
            s += "; cubic spline interpolation"
            s += "\n"
            i += 1
        return s
