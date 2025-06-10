# ENGSCI233: Lab - Iteration and Stability

# PURPOSE:
# To IMPLEMENT explicit Runge-Kutta ODE solution methods.

# imports
import numpy as np
import math


def dydt1(t, y):
    return t - y

def dydt2(t, y, a, b):
    return a * t - b * y

def step_ieuler(f, tk, yk, h, args=None):
	if args is None:
		args = []

	# impoved euler numerical for only one step 
	f0 = f(tk,yk,*args)
	f1 = f(tk+h, yk+h*f0,*args)
	yk2 = yk + h*((f0+f1)/2)
	
	return yk2


def step_rk4(f, tk, yk, h, args=None):
	if args is None:
		args = []

	# runge kutta solution for a single step - four functions to be interchanged
	f0 = f(tk,yk,*args)
	f1 = f(tk+(h/2), yk+((h*f0)/2),*args)
	f2 = f(tk+(h/2),yk+((h*f1)/2),*args)
	f3 = f(tk+h, yk+h*f2,*args)

	yk2 = yk + h*((f0+2*f1+2*f2+f3)/6)
	
	return yk2

def solve_explicit_rk(f, t0, t1, y0, h, method='rk4', args=None):
	"""	Compute solution of initial value ODE problem using explicit RK method.

		Parameters
		----------
		f : callable
			Derivative function.
		t0 : float
			Initial value of independent variable.
		t1 : float
			Final value of independent variable.
		y0 : float
			Initial value of solution.
		h : float
			Step size.
		method : str
			String specifying RK method, either 'rk4' or 'ieuler'. Default is 'rk4'.
		args : iterable
			Optional parameters to pass into derivative function.

		Returns
		-------
		t : array-like
			Independent variable at solution.
		y : array-like
			Solution.

		Notes
		-----
		Assumes that order of inputs to f is f(t, y, *args).
	"""
	if args is None:
		args = []
	
	tspan = math.ceil((t1 - t0)/h)+1 # 5
	factor = (t1 - t0)/h # 
	t = np.fromiter((t0 if i == 0 else h*factor
			    if i == tspan-1 else t0+h*i 
			    for i in range(tspan)),dtype=float) # y array populated with t values

	y = np.zeros(len(t))
	y[0] = y0

	if method == 'rk4':
		for i in range(1,tspan): # how many points to iter 0-4
			y[i] = step_rk4(f,t0,y0,t[i]-t0,*args) # has to link to steps size h
	else:
		for i in range(1,tspan): # how many points to iter
			y[i] = (step_ieuler(f,t0,y0,h,*args)+(h*(i-1)))

	return t,y

	# problem with h incrmenet step - tspan in range cannot be float



def dndt_quota(t, n, r, k, f0):
	pass


def dndt_kaitiakitanga(t, n, r, k, f0, fr):
	pass


def dndt_rahui(t, n, r, k, f0, x):
	pass
