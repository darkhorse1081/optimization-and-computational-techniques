import numpy as np


def leibniz(n, precision='single'):
    """
    Computes the sum of the Leibniz series up to n terms, with specified precision.
    Then multiply by 4 to approximate pi as return.
    """
    # set precision
    if precision == 'single':
        sum = np.float32(0.)
    else:
        sum = np.float64(0.)

    # compute sum
    for k in range(n):
        if precision == 'single':
            sum = sum + np.float32(4.*(-1.)**k/(2*k+1.))
        else:
            sum = sum + np.float64(4.*(-1.)**k/(2*k+1.))

    return sum


if __name__ == '__main__':

    # display built-in numpy pi representation
    print(("Numpy built-in pi = {:18.18f}").format(np.pi))

    # compute Leibniz series of increasing number of components, n
    for n in [10, 100, 1000, 10000, 100000]:

        # caclculate leibniz series estimate of pi in different precision
        l64 = leibniz(n)
        l32 = leibniz(n, 'single')

        # display to screen
        print(("n={:7d}: l64={:18.18f}  l32={:18.18f}").format(n, l64, l32))
