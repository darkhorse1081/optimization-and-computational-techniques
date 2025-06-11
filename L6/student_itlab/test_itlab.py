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

    # test branch for euler
    ysoln_exact = np.array([1.0,3.0,5.0,7.0,9.0])
    tsoln, ysoln = solve_explicit_rk(dydt1,0,8,1,2,'ieuler')
    assert norm(ysoln - ysoln_exact) < tol

    # test branch for rk4
    ysoln_exact = np.array([1.0,5/3,3.222222222222223,5.074074074074074,7.024691358024692])
    tsoln, ysoln = solve_explicit_rk(dydt1,0,8,1,2,'rk4')
    assert norm(ysoln - ysoln_exact) < tol





# test_step_ieuler()
# test_step_rk4()
test_solve_explicit_rk()