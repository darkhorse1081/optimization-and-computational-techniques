import numpy as np
from numpy.random import randint

def sum(n, u):
    """
    Computes the sum of components of length N vector U.
    """
    # set precision
    sum = type(u[0])(0.)

    # compute sum
    for i in range(n):
        sum = sum + u[i]

    return sum


def dot(n, u, v):
    """
    Computes the dot product of length N vectors U and V.
    """
    # set precision
    sum = type(u[0])(0.)

    # compute sum
    for i in range(n):
        sum = sum + u[i]*v[i]

    return sum


if __name__ == '__main__':
    # set vector length
    n = 100001

    # create random vector in double, single and half precision
    u64 = 1. + 1 / 2 ** randint(1, 12, n)
    u32 = np.float32(u64)
    u16 = np.float16(u64)

    # # compute vector sum of increasing number of components, i
    # for i in [10, 100, 1000, 10000, 100000]:
    #
    #     # compare single and double precision
    #     e32 = sum(i, u64[:i] - u32[:i])
    #
    #     # compare half and double precision
    #     e16 = sum(i, u64[:i] - u16[:i])
    #
    #     # display to screen
    #     print(("i={:7d}: e32={:18.18f}  e16={:18.18f}").format(i, e32, e16))

    # compute dot product of increasing numbers of components
    for i in [10, 100, 1000, 10000, 100000]:
        # compute dot product
        # at high precision
        d64 = dot(i, u64[:i], u64[:i])
        # at low precision
        d32 = dot(i, u32[:i], u32[:i])

        # error between low and high precision dot products
        e32 = d32 - d64

        # display to screen
        print(("i={:7d}: e32={:18.18f}").format(i, e32))