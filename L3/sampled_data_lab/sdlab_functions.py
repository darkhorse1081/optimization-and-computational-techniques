# ENGSCI233: Lab - Sampled Data
# sdlab_functions.py

# PURPOSE:
# To IMPLEMENT cubic spline interpolation.

# PREPARATION:
# Notebook sampling.ipynb, ESPECIALLY Section 1.3.1 theory of cubic splines.

# SUBMISSION:
# - YOU MUST submit this file to complete the lab. 
# - DO NOT change the file name.

# TO DO:
# - COMPLETE the functions spline_coefficient_matrix(), spline_rhs() and spline_interpolation().
# - COMPLETE the docstrings for each of these functions.
# - TEST each method is working correctly by passing the asserts in sdlab_practice.py.
# - DO NOT modify the other functions.

import numpy as np


# **this function is incomplete**
#					 ----------
def spline_coefficient_matrix(xi):
    ''' **complete the docstring**
    '''

    d1 = (4*(len(xi)-1))
    d2 = (d1,d1)
    A = np.zeros(d2)

    for i in range(0, len(xi)-1):
        if i == 0:
            A[i][i] = 1
            v = 1
            for j in range(0,4):
                if j == 0:
                    A[i+1][j] = 1
                else:
                    A[i+1][j] = xi[i+1]-xi[i]**v
                    v = v + 1
        else:
            A[i*2][i*4] = 1
            exp = 1
            for a in range(i*4,(i*4)+4):
                if a == i*4:
                    A[(2*i)+1][a] = 1
                else:
                    A[(2*i)+1][a] = (xi[i+1]-xi[i])**exp
                    exp = exp+1

    cntr = 0
    cl_cnt = 1

    for i in range(1, len(xi)-1):

        A[int((d1/2))+cntr][cl_cnt] = 1         
        A[int((d1/2))+cntr][cl_cnt+1] = 2*(xi[i]-xi[i-1]) 
        A[int((d1/2))+cntr][cl_cnt+2] = 3*(xi[i]-xi[i-1]) 
        A[int((d1/2))+cntr+1][cl_cnt+1] = 2
        A[int((d1/2))+cntr+1][cl_cnt+2] = 6*(xi[i]-xi[i-1])

        # this is near the end of the array segment
        A[int((d1/2))+cntr][cl_cnt+4] = -1 # wrong
        A[int((d1/2))+cntr+1][cl_cnt+5] = -2

        cntr = cntr + 2
        cl_cnt = cl_cnt + 4

    A[d1-2][2] = 2
    A[d1-1][d1-2] = 2
    A[d1-1][d1-1] = 6*(xi[len(xi)-1]-xi[len(xi)-2])


    return A


# **this function is incomplete**
#					 ----------
def spline_rhs(xi, yi):
    ''' **complete the docstring**
    '''
    # **use structure of spline_coefficient_matrix() as a guide for
    #   completing this function**

    a1 = spline_coefficient_matrix(xi)
    rhs = np.zeros(4*(len(xi)-1))
    rhs[int((4*(len(xi)-1))/2):4*(len(xi)-1)] = 0

    cnt = 1
    for i in range(0,int((4*(len(xi)-1))/2),2):
        rhs[i] = yi[int(i/2)]
        rhs[i+1] = yi[i+cnt]
        cnt = cnt-1

    # delete this command once you have written your code
    return rhs


# **this function is incomplete**
#					 ----------
def spline_interpolate(xj, xi, ak):
    ''' **complete the docstring**

        Notes
        -----
        You may assume that the interpolation points XJ are in ascending order.
        Evaluate polynomial using polyval function DEFINED below.
    '''

    # Suggested strategy (you could devise another).
    # 1. Initialise FIRST subinterval (and polynomial) as CURRENT subinterval (and polynomial).
    # 2. FOR each interpolation point.
    # 3. WHILE interpolation point NOT inside CURRENT subinterval, iterate
    #    to NEXT subinterval (and polynomial).
    # 4. Evaluate CURRENT polynomial at interpolation point.
    # 5. RETURN when all interpolation points evaluated.

    pass


# this function is complete
def display_matrix_equation(A, b):
    ''' Prints the matrix equation Ax=b to the screen.

        Parameters
        ----------
        A : np.array
            Matrix.
        b : np.array
            RHS vector.

        Notes
        -----
        This will look horrendous for anything more than two subintervals.
    '''

    # problem dimension
    n = A.shape[0]

    # warning
    if n > 8:
        print('this will not format well...')

    print(' _' + ' ' * (9 * n - 1) + '_  _       _   _        _')
    gap = ' '
    for i in range(n):
        if i == n - 1:
            gap = '_'
        str = '|{}'.format(gap)
        str += ('{:+2.1e} ' * n)[:-1].format(*A[i, :])
        str += '{}||{}a_{:d}^({:d})'.format(gap, gap, i % 4, i // 4 + 1) + '{}|'.format(gap)
        if i == n // 2 and i % 2 == 0:
            str += '='
        else:
            str += ' '
        if b is None:  # spline_rhs has not been implemented
            str += '|{}{}{}|'.format(gap, 'None', gap)
        else:
            str += '|{}{:+2.1e}{}|'.format(gap, b[i], gap)
        print(str)


# this function is complete
def get_data():
    # returns a data vector used during this lab
    xi = np.array([2.5, 3.5, 4.5, 5.6, 8.6, 9.9, 13.0, 13.5])
    yi = np.array([24.7, 21.5, 21.6, 22.2, 28.2, 26.3, 41.7, 54.8])
    return xi, yi


# this function is complete
def ak_check():
    # returns a vector of predetermined values
    out = np.array([2.47e+01, -4.075886048665986e+00, 0., 8.758860486659859e-01, 2.15e+01,
                    -1.448227902668027e+00, 2.627658145997958e+00, -1.079430243329928e+00, 2.16e+01,
                    5.687976593381042e-01, -6.106325839918264e-01, 5.358287012458253e-01, 2.22e+01,
                    1.170464160078432e+00, 1.157602130119396e+00, -2.936967278262911e-01, 2.82e+01,
                    1.862652894849505e-01, -1.485668420317224e+00, 1.677900564431842e-01, 2.63e+01,
                    -2.825777017172887e+00, -8.312872001888050e-01, 1.079137281294699e+00, 4.17e+01,
                    2.313177016138269e+01, 9.204689515851896e+00, -6.136459677234598e+00])
    return out


# this function is complete
def polyval(a, xi):
    ''' Evaluates a polynomial.

        Parameters
        ----------
        a : np.array
            Vector of polynomial coefficients.
        xi : np.array
            Points at which to evaluate polynomial.

        Returns
        -------
        yi : np.array
            Evaluated polynomial.

        Notes
        -----
        Polynomial coefficients assumed to be increasing order, i.e.,

        yi = Sum_(i=0)^len(a) a[i]*xi**i

    '''
    # initialise output at correct length
    yi = 0. * xi

    # loop over polynomial coefficients
    for i, ai in enumerate(a):
        yi = yi + ai * xi ** i

    return yi
