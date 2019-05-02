Module approximations
=====================

Functions
---------

`load_data(infile)`
:   Return a list of dictionaries, each containing data for one core.

`make_float(string)`
:   Convert a given string representation into a floating point number.
    
    The string is assumed to be any number of digits before and after a decimal
    point, optionally preceded by + or -.

`print_data(data)`
:   Print the input data in a table.

Classes
-------

`cubicSpline`
:   Set of piecewise cubic interpolation functions of the input data.

    ### Methods

    `__init__(self, dataset)`
    :   Determine a linear interpolation between point i and i+1 for all i.

    `solve_matrix(self, p0, p1, p2)`
    :   Return a tuple of two arrays, each containing the coefficients
        to a cubic interpolant.

    `toList(self)`
    :   Return a list containing one string representation per linear interpolant.

    `toString(self)`
    :   Return a single string representation of all linear interpolants.
        
        **print(csp.toString())** produces the same visual output as
        **for line in csp.toList(): print(line)**.

`leastSquares`
:   Global least-squares approximation of the input data.

    ### Methods

    `__init__(self, dataset, n=2)`
    :   Determine an approximating linear function using n basis functions.
        
        Values of n other than 2 are not currently supported. Arguments passed
        to the n parameter are ignored.

    `basis_PI(self, n, x)`
    :   Return the value of the nth basis function at x.

    `make_row(self, i, x)`
    :   Return an array which represents one row of a matrix A.

    `make_row_b(self, i, x, y)`
    :   Return an array which represents one row of a vector b.

    `sum_PIiPIj(self, i, j, x)`
    :   Return an integer equal to the sum of all (PIi(x) * PIj(x))
        where PIi is the ith basis function and PIj is the jth basis function.

    `toString(self)`
    :   Return a string representation of the approximation polynomial.

`linear`
:   Set of piecewise linear interpolation functions of the input data.

    ### Methods

    `__init__(self, dataset)`
    :   Determine a linear interpolation between point i and i+1 for all i.

    `toList(self)`
    :   Return a list containing one string representation per linear interpolant.

    `toString(self)`
    :   Return a single string representation of all linear interpolants.
        
        **print(lsq.toString())** produces the same visual output as
        **for line in lsq.toList(): print(line)**.
