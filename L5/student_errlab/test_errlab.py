# ENGSCI233: Lab - Numerical Errors

# PURPOSE:
# To TEST your functions for LU factorisation with partial pivoting.

# SUBMISSION:
# - YOU MUST submit this file.

# imports
from functions_errlab import *
from numpy.linalg import norm

# set tolerance for error, must be greater than machine epsilon
tol = 1.e-10

def test_lu_factor_nopivot():
    """
    Test implemention of LU factorisation without partial pivoting.
    """
    # read in from a data file the matrix A and vector b
    [a, b] = lu_read('system1.txt')

    # set your 2D NumPy array containing the combined LU matrices, which you worked out by hand
    # lu_exact = np.array([ [ , , , ], [ , , , ], [ , , , ], [ , , , ] ])

    # call the lu_factor function
    lu, p = lu_factor(a)

    # compare your hard-code matrix with that returned by lu_factor
    assert norm(lu - lu_exact) < tol

def test_lu_forward_sub_nopivot():
    pass

def test_lu_backward_sub_nopivot():
    pass