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

def dydt_cos(t, y):
    return math.cos(math.radians(t))


def step_ieuler(f, tk, yk, h, args=None):
	if args is None:
		args = []

	# impoved euler numerical for only one step 
	f0 = f(tk,yk,*args)
	f1 = f(tk+h, yk+h*f0,*args)
	yk2 = float(yk + h*((f0+f1)/2))
	
	return yk2


def step_rk4(f, tk, yk, h, args=None):
	if args is None:
		args = []

	# runge kutta solution for a single step - four functions to be interchanged
	f0 = f(tk,yk,*args)
	f1 = f(tk+(h/2), yk+((h*f0)/2),*args)
	f2 = f(tk+(h/2),yk+((h*f1)/2),*args)
	f3 = f(tk+h, yk+h*f2,*args)

	yk2 = float(yk + h*((f0+2*f1+2*f2+f3)/6))
	
	return yk2

def solve_explicit_rk(f, t0, t1, y0, h, method='rk4', args=None):
	""" 
	required to compute numerical solutions for arbitary array size
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
			y[i] = step_rk4(f,t[i-1],y[i-1],h,*args) # has to link to steps size h
	else:
		for i in range(1,tspan): # how many points to iter
			y[i] = step_ieuler(f,t[i-1],y[i-1],h,*args)

	return t,y


def dndt_quota(t, n, r, k, f0):
	"""
	t = time/years
	n = fish population
	r = constant birth rate
	k = constant carrying capacity
	f0 = annual intake of fish

	fixed number of fish taken from population each year - to meet 'quota'
	
	non-sustainable - even if population declined - quota remains the same.

	"""
	return r*n*(1-(n/k))-f0 # fish taken from population -> quota per year



def dndt_kaitiakitanga(t, n, r, k, f0, fr):

	"""
	fish quotation - <= f0 // n*fr
	"""

	if (fr*n) > f0:
		return dndt_quota(t, n, r, k, f0)
	else:
		return dndt_quota(t, n, r, k, fr*n)

def dndt_rahui(t, n, r, k, f0, x):

	"""
	t = time/years
	n = fish population
	r = constant birth rate
	k = constant carrying capacity
	f0 = annual intake of fish

	fixed number of fish taken from population each year - to meet 'quota'
		quota - always fraction of current population

	10k fish - quota (nominal)
	annual - 13%

	50k fish  -> 50k*0.13 = 6500 < 10k -> less than nominal
	if population ->100k
		100k*0.13 = 13k > 10k -> greater than nominal -> capped at 10k

	
	periodic - permitted for x years -> move out of area for x years -> resumes x years
	rahui - operations move out area for x years -> 'after' x years of operation

	"""

	fish_q = dndt_quota(t, n, r, k, f0)
	divs = t/x

	for i in range(divs): # 50 years -> 2 yr rahui -> 0-24 (len=25)
		if i % 2 == 0:
			return fish_q

	
