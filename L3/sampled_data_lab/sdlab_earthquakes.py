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

def cumulative_mass(int_input, int_extract):

      cummulated_final = np.zeros(len(int_input)-1)
      for i in range(len(int_input)-1):
            cummulated_final[i] = ((int_extract[i]+int_extract[i+1])/2)*(int_input[i]-int_input[i+1])

      return cummulated_final

def interpolate_to_cumulative(xi,yi,xj):

      yj = np.zeros(len(xj))
      A = spline_coefficient_matrix(xi)
      b = spline_rhs(xi,yi)
      ak = solve(A,b)
      yj = spline_interpolate(xj,xi,ak)
      yj = cumulative_mass(xj,yj)

      return yj

if __name__ == "__main__":

      dir_path = os.path.dirname(os.path.realpath(__file__))
      tm, pm1 = np.genfromtxt(open(dir_path + '/' + 'PW1.dat'), delimiter=',', skip_header=1).T
      tq, pm2 = np.genfromtxt(open(dir_path + '/' + 'PW2.dat'), delimiter=',', skip_header=1).T
      ty, iy = np.genfromtxt(open(dir_path + '/' + 'IW1.dat'), delimiter=',', skip_header=1).T


      # first interpolation for tq (PW1) data so we do across same ammount of points for all datasets
      # comparison for xi will be used to obtain final spline

      tm_xj = np.linspace(tm[0],tm[-1],len(tm))
      pm1_yj = interpolate_to_cumulative(tm,pm1,tm_xj)

      # first interpolation for tq (PW2) data - how to match with pw1

      tq_xj = np.linspace(tm[0],tm[-1],len(tm))
      pm2_yj = interpolate_to_cumulative(tq,pm2,tq_xj)

      # interpolation for ty (IW1) data - how to extrapolate

      ty_xj = np.linspace(ty[0],ty[-1],len(tm))
      iy2_yj = interpolate_to_cumulative(ty,iy,ty_xj)

      # interpolation for ty (IW1) data - how to extrapolate

      netMassExtract = np.zeros(len(ty_xj)-1)
      for i in range(len(ty_xj)-1):
            netMassExtract[i] = (tm_xj[i]+tq_xj[i])-ty_xj[i] # cumulative net mass

      f, ax1 = plt.subplots(nrows=1, ncols=1)
      ax2 = ax1.twinx()  # twinned plots are a powerful way to juxtapose data - plots in opposite direction

      # data plotted and labeled with marker colours such as black blue and red on the graph
      # remember plot points
      # x axis in interpolated xj predcitions
      # y axis is interpolated output xj

      # for every cumulative mass we count from first time after injection first began so [0] + 1
      ax1.plot(tm_xj, pm1_yj, 'k-', label='PW1')
      ax1.plot(tq_xj, pm2_yj, 'b-', label='PW2')
      ax2.plot(ty_xj, iy2_yj, 'navy-', label='IW1')
      ax2.plot(ty_xj, netMassExtract, 'dimgrey-', label='Net-Mass')

      # indicators in the form of arrow accompanied by text to display values - position is also dictated by coordinates
      ax1.arrow(2003.5, 15, 0., -0.75, length_includes_head=True, head_width=0.2, head_length=0.1, color='k')
      ax1.text(2003., 14.65, 'M 3.5', ha='right', va='center', size=10, color='k')
      ax1.arrow(2004.5, 15, 0., -0.75, length_includes_head=True, head_width=0.2, head_length=0.1, color='k')
      ax1.text(2004.5, 15.2, 'M 4.0', ha='center', va='bottom', size=10, color='k')
      ax1.arrow(2005., 15, 0., -0.75, length_includes_head=True, head_width=0.2, head_length=0.1, color='k')
      ax1.text(2005.5, 14.65, 'M 4.3', ha='left', va='center', size=10, color='k')

      # overall graph and plot features such as titles, axis, lables, plot, etc - also includes y axis limits
      ax2.set_ylim([0, 40])
      ax1.legend(loc=2)
      ax1.set_ylim([0, 20])
      ax1.set_ylabel('interpolated cumulative production mass [kg]')
      ax2.set_ylabel('interpolated cumulative injection mass [kg]')
      ax2.set_xlabel('time [yr]')
      ax2.set_title('Cumulative Net Mass of production and injection at field X')

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
