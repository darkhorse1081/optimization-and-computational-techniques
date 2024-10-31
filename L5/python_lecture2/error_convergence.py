import numpy as np
import matplotlib.pyplot as plt


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

    # initialise lists for truncation error, convergence tests and iteration numbers
    truncation = []
    test_abs = []
    test_rel = []
    test_uni = []
    iterations = np.arange(5, 100)

    # compute Leibniz series of increasing number of components, n
    for n in iterations:

        # get leibniz series result for consecutive iterations
        l64_a = leibniz(n, '64')
        l64_b = leibniz(n-1, '64')

        # calculate the numerical convergence tests
        truncation.append(np.abs(l64_a - np.pi))
        test_abs.append(np.abs(l64_a - l64_b))
        test_rel.append(np.abs(l64_a - l64_b)/np.abs(l64_a))
        test_uni.append(np.abs(l64_a - l64_b)/(1. + np.abs(l64_a)))

    # plot the results
    fig, ax = plt.subplots(figsize=[9, 7])
    ax.plot(iterations, truncation, 'k-', label="truncation error")
    ax.plot(iterations, test_abs, 'b.', label="absolute test")
    ax.plot(iterations, test_rel, 'g--', label="relative test")
    ax.plot(iterations, test_uni, 'r-.', label="uniform test")
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Convergence Tests')
    plt.legend()
    plt.show()
