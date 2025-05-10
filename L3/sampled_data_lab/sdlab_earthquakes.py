from matplotlib import pyplot as plt
import numpy as np
from numpy.linalg import solve
from sdlab_functions import *
import os 

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
      # xi index also impact yi index

      tm_xj = np.linspace(tq[0],tq[-1],len(tm))  
      pm1_yj = interpolate(tm,pm1,tm_xj)

      # first interpolation for tq (PW2) data - how to match with pw1
      # tq data interpolated with respect to tm

      tq_xj = np.linspace(tq[0],tq[-1],len(tm)) 
      pm2_yj = interpolate(tq,pm2,tq_xj)

      # interpolation for ty (IW1) data - how to extrapolate

      ty_xj = np.linspace(tq[0],tq[-1],len(tm)) 
      m = np.argmax(np.logical_and(ty[0] >= ty_xj[:-1], ty[0] <= ty_xj[1:]))
      n = np.argmax(np.logical_and(ty[-1] >= ty_xj[:-1], ty[-1] <= ty_xj[1:]))
      ty_xj2 = ty_xj[m:n+1] # new interpolate data
      iy2_yj = interpolate(ty,iy,ty_xj2) # dont want cumulative mass for raw data 

      # cumulative data only for net mass
      # interpolation for ty (IW1) data - how to extrapolate

      netMassExtract = np.zeros(len(ty_xj2)-1) # --

      ct = 0
      for i in range(m,n):
            netMassExtract[ct] = abs(((((pm1_yj[i]+pm1_yj[i+1])/2)*(tq_xj[i+1]-tq_xj[i]))+
                                 (((pm2_yj[i]+pm2_yj[i+1])/2)*(tq_xj[i+1]-tq_xj[i])))-(((iy2_yj[ct]+iy2_yj[ct+1])/2)*(tq_xj[i+1]-tq_xj[i])))
            ct = ct+1

      f, ax1 = plt.subplots(nrows=1, ncols=1)
      ax2 = ax1.twinx()  # twinned plots are a powerful way to juxtapose data - plots in opposite direction

      # for every cumulative mass we count from first time after injection first began so [0] + 1
      ax1.plot(tm_xj, pm1_yj, 'k-', label='PW1')
      ax1.plot(tq_xj, pm2_yj, 'b-', label='PW2')
      ax2.plot(ty_xj2, iy2_yj, 'g-', label='IW1')
      ax2.plot(ty_xj2[1:], netMassExtract, 'y-', label='Net-Mass')

      # overall graph and plot features such as titles, axis, lables, plot, etc - also includes y axis limits
      ax2.set_ylim([-0.2, 35])
      ax1.set_ylim([0, 12.5])
      ax1.legend(loc=2)
      ax2.legend(loc=0)
      ax1.set_ylabel('interpolated cumulative production mass [kg]')
      ax2.set_ylabel('interpolated cumulative injection mass [kg]')
      ax2.set_xlabel('time [yr]')
      ax2.set_title('Cumulative Net Mass of production and injection at field X')

      plt.show()
