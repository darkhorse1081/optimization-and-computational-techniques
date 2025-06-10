# ENGSCI233: Lab - Iteration and Stability

# PURPOSE:
# To IMPLEMENT explicit Runge-Kutta ODE solution methods.

# imports
import numpy as np


def dydt1(t, y):
    return t - y

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
	
	tspan = (t1 - t0)/h
	t = np.fromiter((i+h for i in range(t0,t1+1)),dtype=int) # y array populated with t values
	y = np.zeros(len(t))


	if method == 'rk4':
		for i in range(tspan): # how many points to iter
			y[i] = step_rk4(f(t0,y0,*args),t0,y0,h,*args)
	else:
		for i in range(tspan): # how many points to iter
			y[i] = step_ieuler(f(t0,y0,*args),t0,y0,h,*args)

	return t,y


def dndt_quota(t, n, r, k, f0):
	pass


def dndt_kaitiakitanga(t, n, r, k, f0, fr):
	pass


def dndt_rahui(t, n, r, k, f0, x):
	pass
