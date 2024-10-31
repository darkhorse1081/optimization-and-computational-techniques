import numpy as np

if __name__ == '__main__':

    # get computer zero for given precision
    eps64 = np.finfo(np.float64).eps
    eps32 = np.finfo(np.float32).eps
    eps16 = np.finfo(np.float16).eps

    # set two similar numbers
    a = np.float16(1.0)
    b = np.float16(1.00001)

    if abs(a-b) <= 0:
        print('same')
    else:
        print('not same')
