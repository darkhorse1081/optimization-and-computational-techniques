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
import os 


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

	
# by default pivot is false
def lu_factor(A, pivot=False):
		
	n = np.shape(A)[0] 	# -- 4
	p = np.arange(n) # -- [0,1,2,3] create initial row swap vector: p = [0, 1, 2, ... n]

	U = A.copy()
	L = 0*A
	for i in range(n): # - diag 1s in lower - matrix 0s prior
		L[i][i] = 1

	for i in range(n): # 0->3 -- iteration update deicdes the pivot
		
		# Step 2: Row swaps for partial pivoting
		if pivot:
			# **hint** Pseudocode the key steps below (locating pivots, row swaps etc).
			# **note** When swapping rows, use the copy() command, i.e., temp = copy(A[2,:])
			
			update = np.argmax(U[1:][0])
			temp = copy(U[update])
				
			# **delete the command below when code has been written**

		if i != p[-1]: # p[-1] -> if last value ignore next iteration 
			for m in range(i+1,p[-1]+1): # -> populate matrix by row - L pivot fixed
				L[m][i] = U[m][i]/U[i][i] 

			for i2 in range(i+1,p[-1]+1): # upper target quadrant for calc -- rows
				for j2 in range(p[-1]+1):
					U[i2][j2] =  U[i2][j2] - (L[i2][i]*U[i][j2])
		else:
			break	

	U_copy = U.copy()
	# replace 0s in U with 
	for k1 in range(n-1): # - [0,1,2]
		for z1 in range(k1+1, n): # -> 0-3.1-3.2-3
			U[z1][k1] = L[z1][k1]

	A = U
	return A, p, L, U_copy

	
# **this function is incomplete**
def lu_forward_sub(L, b, p=None): # Ly = b
	
	# check shape of L consistent with shape of b (for matrix multiplication L^T*b)
	n = np.shape(L)[0] 
	assert np.shape(L)[0] == len(b)
		
	# Step 2: Perform partial pivoting row swaps on RHS
	if p is not None:
		# **hint** Pseudocode the key steps below	
		# **note** When swapping values, use the copy() command, i.e., temp = copy(y[i])				
				
		# **delete the command below when code has been written**
		pass

	y = np.zeros(n)
	n2 = 0
	for i in range(n): # 0->3
		if i == 0:
			y[i] = b[i]
		else:
			n2 = n2 + 1
			y[i] = (b[i]-(np.dot(L[i][:n2],y[:n2])))/L[i][i]

	b = y		
	return b


	
# **this function is incomplete**
def lu_backward_sub(U, y):
	
	# check shape consistency
	n = np.shape(U)[0] 
	assert np.shape(U)[0] == len(y)

	
	# Perform backward substitution operations
	x = np.zeros(n)
	n4 = n-1
	for i in range(n-1,(n-n)-1,-1):
		if i == n-1:
			x[i] = y[i]/U[i][i]
		else:
			n4 = n4 - 1
			x[i] = (y[i]-(np.dot(U[i][n-1:n4:-1],x[n-1:n4:-1])))/U[i][i]

	return x
	
