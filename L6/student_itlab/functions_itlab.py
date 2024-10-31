# ENGSCI233: Lab - Iteration and Stability

# PURPOSE:
# To IMPLEMENT explicit Runge-Kutta ODE solution methods.

# imports
import numpy as np


def step_ieuler(f, tk, yk, h, args=None):
	if args is None:
		args = []
	pass


def step_rk4(f, tk, yk, h, args=None):
	if args is None:
		args = []
	pass


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
	pass


def dndt_quota(t, n, r, k, f0):
	pass


def dndt_kaitiakitanga(t, n, r, k, f0, fr):
	pass


def dndt_rahui(t, n, r, k, f0, x):
	pass
