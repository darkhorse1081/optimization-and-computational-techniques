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

dir_path = os.path.dirname(os.path.realpath(__file__))
tm, pm1 = np.genfromtxt(open(dir_path + '/' + 'PW1.dat'), delimiter=',', skip_header=1).T
tq, pm2 = np.genfromtxt(open(dir_path + '/' + 'PW2.dat'), delimiter=',', skip_header=1).T
ty, iy = np.genfromtxt(open(dir_path + '/' + 'IW1.dat'), delimiter=',', skip_header=1).T


# first interpolation for tq (PW1) data so we do across same ammount of points for all datasets
# comparison for xi will be used to obtain final spline

tm_xj = np.linspace(tm[0],tm[-1],len(tm))
pw1_yj = interpolate_to_cumulative(tm,pm1,tq_xj)

# first interpolation for tq (PW2) data

tq_xj = np.linspace(tm[0],tm[-1],len(tm))
pw2_yj = interpolate_to_cumulative(tq,pm2,tq_xj)

# interpolation for ty (IW1) data

tq_xj = np.linspace(tm[0],tm[-1],len(tm))
pw2_yj = interpolate_to_cumulative(tq,pm2,tq_xj)


# net mass change and cumulative of the interpolated data
# net mass chnage will be processed from when injection takes effect first - only 1993.5 onwards






# interpolation points -- linespacing -- times (years) this is based on missing data in IW1
# original xi is tq array

# after full interpolation - only for cumulative mass

def cumulative_mass(int_input, int_extract):

      cummulated_final = np.zeros(len(int_input))

      for i in range(len(int_input)):
            if i == len(int_input)-1:
                  cummulated_final[i] = int_input[i]
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




# x = 5
# y = 2



# EXERCISE: Analysis of Net Mass Changes.
#
# Earthquakes are sometimes associated with oil and gas production (taking mass out of the 
# ground) and injection (putting it back in) operations.
# 
# It has been suggested that injection of water at one particular site, which started midway through  
# 1993, has been responsible for a spate of recent earthquakes there. These are the data that were 
# plotted in the first exercise of sdlab_practice.py. The operator of the field has claimed they 
# cannot be responsible, because injection had been ongoing for almost 10 years before any earthquakes
# occurred.
#
# It has been proposed the earthquakes may be related to NET MASS CHANGES in the field. Therefore,
# it is necessary to understand how this quantity has evolved over time.
#
# Although data from the two production wells (mass extractors) - PW1 and PW2 - are reported regularly,
# data reporting from the injection well, IW1, is more irregular. In addition, the operator only 
# reports MASS RATES, not CUMULATIVE production or injection MASS.
#
# TO solve this problem, you will need to use both INTERPOLATION and INTEGRATION.


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
