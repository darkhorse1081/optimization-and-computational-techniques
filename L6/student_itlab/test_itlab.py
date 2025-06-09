# ENGSCI233 Lab: Iteration

# PURPOSE:
# To TEST your RK methods for a simple ODE.
from functions_itlab import *
from numpy.linalg import norm

tol = 1.e-10


def test_step_ieuler():

    value = step_ieuler(dydt1,0.,1.,2.)
    exact_val = 3

    value2 = step_ieuler(dydt2,0.,1.,2., [2.,1.])
    exact_val2 = 5

    assert norm(value - exact_val) < tol
    assert norm(value2 - exact_val2) < tol

def test_step_rk4():

    value3 = step_rk4(dydt1,0.,1.,2.)
    exact_val3 = 5/3

    value4 = step_rk4(dydt2,0.,1.,2., [2.,1.])
    exact_val4 = 3

    assert norm(value3 - exact_val3) < tol
    assert norm(value4 - exact_val4) < tol


def test_solve_explicit_rk():
    pass

def dydt1(t, y):
    return t - y

def dydt2(t, y, a, b):
    return a * t - b * y


test_step_ieuler()
test_step_rk4()