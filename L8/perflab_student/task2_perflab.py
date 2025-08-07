# TASK 2: Optimising

# imports
from functions_perflab import *

#TODO - your code here
if __name__ == "__main__":

    # set 1 -> n = matrix dimensions how much by how much
    data_set = [2,4,8,16,32,64,128,256]
    execution_time = profile_matmul(10, data_set, matmul1)
    execution_time2 = profile_matmul(10, data_set, matmul2)
    execution_time3 = profile_matmul(10, data_set, np.matmul)

    print('Total time set 1:',execution_time)
    print('Total time set 2:',execution_time2)
    print('Total time set 3:',execution_time3)

    # create the empty figure
    f, ax = plt.subplots(1, 1)
    logtimes1 = [(np.log(elem)) for elem in execution_time]
    logtimes2 = [(np.log(elem)) for elem in execution_time2]
    logtimes3 = [(np.log(elem)) for elem in execution_time3]
    logSize = [(np.log(elem)) for elem in data_set]
    ax.plot(logSize, logtimes1, 'k-o', label='For loop iteration - matmul1')
    ax.plot(logSize, logtimes2, 'g-o', label='NP.dot in inner loop - matmul2')
    ax.plot(logSize, logtimes3, 'b-o', label='Using Numpy Matmul function')
    ax.set_title('profiling execution_time - logarithm plot')
    ax.legend(loc=2)
    ax.set_xlabel('logged_problem_size log(N)')
    ax.set_ylabel('logged_execution_time log(t/s)')
    # show the plot
    plt.show()
