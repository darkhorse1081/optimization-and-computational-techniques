# ENGSCI233: Lab - Numerical Errors

# PURPOSE:
# To IMPLEMENT LU factorisation with partial pivoting and solve matrix equation.

# SUBMISSION:
# - YOU MUST submit this file.

# TO DO:
# - READ all the comments in a function before modifying it
# - COMPLETE the functions lu_factor(), lu_forward_sub() and lu_backward_sub()
# - TEST each function is working correctly by writing test functions in test_errlab.py
# - DO NOT modify the other function(s)

# imports
import numpy as np
from copy import copy


# this function is complete
def lu_read(filename):
	"""
	This function will read in matrix data from an external file that adheres to an appropriate format. It will then
	return both the coefficient matrix A and vector of constants b for a system of linear equations, Ax=b.
	"""
	with open(filename, 'r') as fp:
		# Row dimension
		nums = fp.readline().strip()
		row = int(nums)
		
		A = []
		for i in range(row):
			nums = fp.readline().rstrip().split()
			A.append([float(num) for num in nums])
		A = np.array(A)
		
		b = []
		nums = fp.readline().rstrip().split()
		b.append([float(num) for num in nums])
		b = np.array(b)
		
	return A, b.T

	
# **this function is incomplete**
def lu_factor(A, pivot=False):
		
	# get dimensions of square matrix 
	n = np.shape(A)[0] 	
	
	# create initial row swap vector: p = [0, 1, 2, ... n]
	p = np.arange(n) 		

	# loop over each row in the matrix
	# **hint** what is the pivot index, row and column?
	for i in range(n):		
		
		# Step 2: Row swaps for partial pivoting
		#    DO NOT attempt until Steps 0 and 1 below are confirmed to be working.
		if pivot:
			# **hint** Pseudocode the key steps below (locating pivots, row swaps etc).
			# **note** When swapping rows, use the copy() command, i.e., temp = copy(A[2,:])
				
			# **delete the command below when code has been written**
			pass
			

		# Step 0: Get the pivot value
		#pivot_value = ???
		
		# Step 1: Perform the row reduction operations 
		# - make sure to modify A in place
		# **hint** Pseudocode the key steps first (loop over which rows? subtract how much from what?)				 	
		 
	return A, p

	
# **this function is incomplete**
def lu_forward_sub(L, b, p=None):
	
	# check shape of L consistent with shape of b (for matrix multiplication L^T*b)
	assert np.shape(L)[0] == len(b), 'incompatible dimensions of L and b'
	
	# Step 0: Get matrix dimension										
	# **hint** See how this is done in lu_factor()
		
	# Step 2: Perform partial pivoting row swaps on RHS
	if p is not None:
		# **hint** Pseudocode the key steps below	
		# **note** When swapping values, use the copy() command, i.e., temp = copy(y[i])				
				
		# **delete the command below when code has been written**
		pass
	
	# Step 1: Perform forward substitution operations
	# - make sure to modify b in place
	# **hint** Pseudocode the key steps below (loops, dot products etc.)   	
		
	return b

	
# **this function is incomplete**
def lu_backward_sub(U, y):
	
	# check shape consistency
	assert np.shape(U)[0] == len(y), 'incompatible dimensions of U and y'
	
	# Perform backward substitution operations
			
	# Return 
	# **delete the pass command below when code has been written**
	pass
