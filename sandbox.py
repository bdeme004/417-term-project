import numpy as np
#from numpy.polynomial import Polynomial as npp

points = {
    0: 0,
    1: 2,
    2: 8,
    3: 18
}

points2 = {
    1: 2,
    2: 3,
    3: 5,
    4: 6
}


def doMath(data):
    return data


def printPoly(data):
    print(data)


def cubicSpline(p0, p1, p2):

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


#rename this
def spline(dataset):

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
        c0, c1 = cubicSpline(p0, p1, p2)
        result.setdefault(i, c0)
        i += 1
        result.setdefault(i, c1)
        p0 = p1
        p1 = p2
    return result


cats = spline(points)

print(cats)
