# ENGSCI233: Lab - Sampled Data
# sdlab_earthquakes.py

from matplotlib import pyplot as plt  # MATPLOTLIB is THE plotting module for Python
import numpy as np
from numpy.linalg import solve
from sdlab_functions import *
import os 

# PURPOSE:
# To INVESTIGATE a dataset using interpolation and integration methods.

# PREPARATION:
# Complete the activities in sdlab_practice.py.

# SUBMISSION:
# - YOU MUST submit a plot of NET MASS CHANGE as a function of time (sdlab_earthquakes.png)
# - You MUST submit this file to complete the lab.

def cumulative_mass(xj, yj):

      cummulated_final = np.zeros(len(xj)-1)
      for i in range(len(xj)-1):
            cummulated_final[i] = ((yj[i]+yj[i+1])/2)*(xj[i+1]-xj[i])

      return cummulated_final

def interpolate(xi,yi,xj):

      yj = np.zeros(len(xj))
      A = spline_coefficient_matrix(xi)
      b = spline_rhs(xi,yi)
      ak = solve(A,b)
      yj = spline_interpolate(xj,xi,ak)

      return yj

if __name__ == "__main__":

      dir_path = os.path.dirname(os.path.realpath(__file__))
      tm, pm1 = np.genfromtxt(open(dir_path + '/' + 'PW1.dat'), delimiter=',', skip_header=1).T
      tq, pm2 = np.genfromtxt(open(dir_path + '/' + 'PW2.dat'), delimiter=',', skip_header=1).T
      ty, iy = np.genfromtxt(open(dir_path + '/' + 'IW1.dat'), delimiter=',', skip_header=1).T

      # interpolation occurs through comparison between predicted and known timestamps

      tm_xj = np.linspace(tq[0],tq[-1],len(tm))  
      pm1_yj = interpolate(tm,pm1,tm_xj)

      # first interpolation for tq (PW2) data - how to match with pw1
      # tq data interpolated with respect to tm

      tq_xj = np.linspace(tq[0],tq[-1],len(tm)) 
      pm2_yj = interpolate(tq,pm2,tq_xj)

      # interpolation for ty (IW1) data - how to extrapolate

      ty_xj = np.linspace(tq[0],tq[-1],len(tm)) 
      m = np.argmax(np.logical_and(ty[0] >= ty_xj[:-1], ty[0] < ty_xj[1:]))
      n = np.argmax(np.logical_and(ty[-1] >= ty_xj[:-1], ty[-1] < ty_xj[1:]))
      ty_xj2 = ty_xj[m:n+1] # new interpolate data
      iy2_yj = interpolate(ty,iy,ty_xj2) # dont want cumulative mass for raw data 

      # cumulative data only for net mass
      # interpolation for ty (IW1) data - how to extrapolate

      netMassExtract = np.zeros(len(ty_xj2)-1) # --

      for i in range(m,len(ty_xj2)-1):
            netMassExtract[i] = (((pm1_yj[i]+pm1_yj[i+1])/2)*(ty_xj2[i+1]-ty_xj2[i])+
                                 ((pm2_yj[i]+pm2_yj[i+1])/2)*(ty_xj2[i+1]-ty_xj2[i]))-(((iy2_yj[i]+iy2_yj[i+1])/2)*(ty_xj2[i+1]-ty_xj2[i]))
            

      f, ax1 = plt.subplots(nrows=1, ncols=1)
      ax2 = ax1.twinx()  # twinned plots are a powerful way to juxtapose data - plots in opposite direction

      # for every cumulative mass we count from first time after injection first began so [0] + 1
      ax1.plot(tm_xj, pm1_yj, 'k-', label='PW1')
      ax1.plot(tq_xj, pm2_yj, 'b-', label='PW2')
      ax2.plot(ty_xj2, iy2_yj, 'g-', label='IW1')
      ax2.plot(ty_xj2[1:], netMassExtract, 'y-', label='Net-Mass')

      # overall graph and plot features such as titles, axis, lables, plot, etc - also includes y axis limits
      ax2.set_ylim([0, 40])
      ax1.set_ylim([0, 20])
      ax1.legend(loc=2)
      ax2.legend(loc=0)
      ax1.set_ylabel('interpolated cumulative production mass [kg]')
      ax2.set_ylabel('interpolated cumulative injection mass [kg]')
      ax2.set_xlabel('time [yr]')
      ax2.set_title('Cumulative Net Mass of production and injection at field X')

      plt.show()

# net mass change and cumulative of the interpolated data
# net mass chnage will be processed from when injection takes effect first - only 1993.5 onwards

# my first measurement should be done on interpolated_xj[1] to inclusive final interpolated_xj[-1]

# interpolation points -- linespacing -- times (years) this is based on missing data in IW1
# original xi is tq array

# after full interpolation - only for cumulative mass

# TO DO:
# - In sdlab_functions.py, COMPLETE the functions SPLINE_COEFFICIENT_MATRIX, SPLINE_RHS, and
#   SPLINE_INTERPOLATE.
# - Write a Newton-Cotes integration function OR find and use a built-in Python function.
# - Produce a plot of NET MASS CHANGE as a function of time.
# - ANSWER the questions in sdlab_questions.txt


# HINTS:
# - To add or difference two quantities, they should be measured or interpolated at the same time.
# - You should consider a sensible strategy for the event that an interpolation point lies outside 
#   the range of data (extrapolation).
# - MASS RATE is a derivative (per unit time) and CUMULATIVE MASS is its integral. 
# - You will be assessed on the ability of your figure to convey information. Things that help:
#    o Sensible labels (and units) for the axes.
#    o A legend.
#    o Sensible use of lines versus markers.
#    o Juxtaposition of information in a way that highlights correlation.
# - The plotting exercise in PRACTICE TASK ONE is relevant here.
