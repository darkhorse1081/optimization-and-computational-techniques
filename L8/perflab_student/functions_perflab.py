# ENGSCI: Lab - Performance

# imports
import numpy as np
from matplotlib import pyplot as plt
import multiprocessing
import itertools
import time
import psutil
import os
import platform
import cProfile
import pstats
import io
import time

def multiply_square_matrices(multiplications, n, matmul):
    """
    Performs matrix multiplication for many square matrices.
    
    Parameters
    ----------
    multiplications : int
        Number of matrix multiplications to perform.
    n : int
		Number of rows and columns in square matrices being multiplied.
	matmul : callable
        Function to use to perform matrix multiplication
    """
    # iteratively multiply square matrices of random numbers, then return
    for i in range(multiplications):
        a = square_matrix_rand(n)
        b = square_matrix_rand(n)
        _ = matmul(a, b)
    return

def square_matrix_rand(n):
    """
    Create a square matrix of random values between -1 and 1.

    Parameters
    ----------
    n : int
        Size of the square matrix (n x n).

    Returns
    -------
    matrix : numpy array
        Square matrix containing uniformly distributed random numbers between -1 and 1.
    """
    matrix = np.random.rand(n, n) * 2. - 1.
    return matrix

def matmul1(a, b):
    """
    Multiply two matrices using "naive" method.

        Parameters
        ----------
        a : numpy array
            Left multiplying matrix i.e. A.
        b : numpy array
            Right multiplying matrix i.e. B.

        Returns
        -------
        c : numpy array
            Matrix product i.e. AB = C.

        Raises
        ------
        ValueError
            If inner dimensions of matrix product are inconsistent
    """
    # check dimension consistency precondition
    if a.shape[1] != b.shape[0]:
        raise ValueError('Dimension inconsistency: A must have the same number of columns as B has rows.')

    # compute matrix product as dot products of rows and columns
    product = np.zeros((a.shape[0], b.shape[1]))
    for i in range(product.shape[0]):
        for j in range(product.shape[1]):
            for k in range(a.shape[1]):
                product[i, j] += a[i, k] * b[k, j]
    return product

def matmul2(a, b):
    """
    Multiply two matrices together, making use of built-in NumPy dot. Utilises NumPy dot product to replace
    third and final nested for loop of naive implementation.

        Parameters
        ----------
        a : numpy array
            Left multiplying matrix i.e. A.
        b : numpy array
            Right multiplying matrix i.e. B.

        Returns
        -------
        c : numpy array
            Matrix product i.e. AB = C.

        Raises
        ------
        ValueError
            If inner dimensions of matrix product are inconsistent
    """
    if a.shape[1] != b.shape[0]:
        raise ValueError('Dimension inconsistency: A must have the same number of columns as B has rows.')
    
    # compute matrix product as dot products of rows and columns
    product = np.zeros((a.shape[0], b.shape[1]))
    for i in range(product.shape[0]):
        for j in range(product.shape[1]):
            product[i, j] = np.dot(a[i,:],b[:,j])

    return product

def profile_matmul(multiplications, n, matmul):

    # takes list of n
    p_size = []

    # logs data from n matrix dimensions - stores times in list to return
    for i in n:
        profiler_id = cProfile.Profile()

        profiler_id.enable()
        multiply_square_matrices(multiplications, i, matmul)
        profiler_id.disable()

        ps = pstats.Stats(profiler_id).sort_stats('tottime')
        p_size.append(ps.total_tt)
    
    return p_size

def plot_polynomial_performance(times, n):

    # create the empty figure
    f, ax = plt.subplots(1, 1)

    logged_execution_time = np.log(times)
    logged_size_of_problem = np.log(n)

    z = np.polyfit(logged_size_of_problem, logged_execution_time, 1)
    p = np.poly1d(z)

    # show the plot
    ax.plot(logged_size_of_problem, logged_execution_time, 'kx')
    ax.plot(logged_size_of_problem, p(logged_size_of_problem), label='Linear Fit', color='blue')
    ax.set_title('profiler')
    ax.legend(loc=2)
    ax.set_xlabel('logged_problem_size log(N)')
    ax.set_ylabel('logged_execution_time log(t/s)')
    plt.show()


def time_serial_multiply_square_matrices(multiplications, n, matmul, verbose=False):

    tic = time.perf_counter() # regular operation w matmul1
    multiply_square_matrices(multiplications, n, matmul)
    toc = time.perf_counter()
    time_taken = toc - tic
    if verbose:
        print('time serial: ', time_taken)
    return time_taken


def time_parallel_multiply_square_matrices(multiplications, order, matmul, cpu_cap=None, verbose=False):

    time_parallel = [] 
    ncpu_used = [] 

    if cpu_cap is None:
        max_ncpu = os.cpu_count() # available cpu in sys if not specified else spec iter calc
    else:
        max_ncpu = cpu_cap+1

    for ncpu in range(2, max_ncpu): # range starting from 2 -> max_cpu [2-8]

        multiplications_per_cpu = [int(multiplications / ncpu)] * ncpu # -> start 2 -> [500/2]*2 = [250, 250]
        i = 0
        while sum(multiplications_per_cpu) < multiplications: 
            multiplications_per_cpu[i] += 1 # int op reduces raw values -> iterator add + compares < 500 
            i += 1
            if i >= len(multiplications_per_cpu): # fills mult_cpu list sum() = 500
                i = 0

        # TODO - if this is struggling to work, try using command that uses limit_cpu
        with multiprocessing.Pool(ncpu) as pool:
        # with multiprocessing.Pool(ncpu, limit_cpu) as pool:
            tic = time.perf_counter() # starmap -> distributes processes to pool of cpus
            pool.starmap(multiply_square_matrices, zip(multiplications_per_cpu, itertools.repeat(order),
                                                       itertools.repeat(matmul)))
            toc = time.perf_counter()

        time_parallel.append(toc - tic) # final_time - inital_time = program execution time
        ncpu_used.append(ncpu)

        if verbose:
            print('time parallel with ', ncpu, 'CPU: ', toc - tic) # printed within the current cpu cycle

    return ncpu_used, time_parallel 


def limit_cpu():
    """
    Called at every process start. For Windows will attempt to reduce CPU priority and reduce chance of computer
    freezing due to full CPU utilisation.
    """
    if platform.system() == 'Windows':
        p = psutil.Process(os.getpid())
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)

def plot_runtime_ncpu(runtime, ncpu):

    # create the empty figure with two subplots
    f, (ax1, ax2) = plt.subplots(2, 1)
    speedup_calc = []
    efficiency_calc = []

    for i in range(0, len(ncpu)):
        speedup_calc.append(runtime[0]/runtime[i]) # --
        efficiency_calc.append(runtime[0]/(runtime[i]*ncpu[i])) # --

    # parralel speedup Ts/Tp -> y1
    ax1.set_xlabel('[cpus]')
    ax1.set_ylabel('[speed up]')
    ax1.plot(ncpu, speedup_calc, color='green')
    ax1.set_title('parralel speedup')

    # parralel efficiency Ts/Tp*n -> y2
    ax2.set_xlabel('[cpus]')
    ax2.set_ylabel('[efficiency]')
    ax2.plot(ncpu, efficiency_calc, color='blue')
    ax2.set_title('parralel efficiency')

    # show the plot 
    plt.show()
