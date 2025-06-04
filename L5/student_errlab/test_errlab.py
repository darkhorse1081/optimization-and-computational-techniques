# ENGSCI233: Lab - Numerical Errors

# PURPOSE:
# To TEST your functions for LU factorisation with partial pivoting.

# SUBMISSION:
# - YOU MUST submit this file.

# imports
import os
from functions_errlab import *
from numpy.linalg import norm

# set tolerance for error, must be greater than machine epsilon
tol = 1.e-10

def test_lu_factor_nopivot():

    [a, b] = lu_read('system1.txt')
    lu_exact = np.array([ [ 2, 3, -4, 2], [ -2, 1, -2, 1], [ 1, -1, 3, -1], [ -3, 2, 2, 2] ]) # expected
    lu, p = lu_factor(a, True)
    assert norm(lu - lu_exact) < tol

def test_lu_forward_sub_nopivot():

    [a, b] = lu_read('system1.txt')
    lu, p = lu_factor(a)
    b2 = lu_forward_sub(lu, b, p=None)
    b_exact = np.array([4, 0, 5, 8])
    assert norm(b2 - b_exact) < tol


def test_lu_backward_sub_nopivot():

    [a, b] = lu_read('system1.txt')
    lu, p = lu_factor(a)
    b2 = lu_forward_sub(lu, b, p=None)
    x2 = lu_backward_sub(lu,b2)

    x_exact = np.array([1, 2, 3, 4])
    assert norm(x2 - x_exact) < tol


test_lu_factor_nopivot()
test_lu_forward_sub_nopivot()
test_lu_backward_sub_nopivot()