def testData1():
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


def testData2():

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
