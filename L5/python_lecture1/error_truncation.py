import numpy as np
from numpy.random import randint


def leibniz(n, precision='64'):
    """
    Computes the sum of the Leibniz series up to n terms, with specified precision.
    Then multiply by 4 to approximate pi as return.
    """
    # set precision
    if precision == '16':
        sum = np.float16(0.)
    elif precision == '32':
        sum = np.float32(0.)
    else:
        sum = np.float64(0.)

    # compute sum
    for k in range(n):
        sum = sum + (-1.)**k/(2*k+1.)

    return sum


if __name__ == '__main__':

    # display built-in numpy pi representation
    print(("Numpy built-in pi={:18.18f}").format(np.pi))

    # compute Leibniz series of increasing number of components, n
    for n in [10, 100, 1000, 10000, 100000]:

        # caclculate leibniz series estimate of pi in different precision
        l64 = 4.*leibniz(n)
        l32 = 4.*leibniz(n, '32')
        l16 = 4.*leibniz(n, '16')

        # display to screen
        print(("n={:7d}: l64={:18.18f}  l32={:18.18f}  l16={:18.18f}").format(n, l64, l32, l16))
