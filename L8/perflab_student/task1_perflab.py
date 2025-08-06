# TASK 1: Profiling

# imports
from functions_perflab import *


if __name__ == "__main__":

    # create a profiling object
    pr = cProfile.Profile()

    # enable the profiler, run the thing to profile, and then disable the profiler
    pr.enable()
    multiply_square_matrices(10, 50, matmul1)
    pr.disable()

    # get and print useful stats from the profiler
    ps = pstats.Stats(pr).sort_stats('tottime')
    ps.print_stats()

    # print total time to screen
    print('Total time taken:', ps.total_tt)

    # set 1 -> n = matrix dimensions how much by how much
    data_set1 = [2,4,8,16,32,64,128, 256]
    execution_time = profile_matmul(10, data_set1, matmul1)
    print('Total time set 1:',execution_time)

    plot_polynomial_performance(execution_time, data_set1)





