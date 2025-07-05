# rk4 iteration

# PURPOSE:
# To INVESTIGATE the fisheries management scenario in Task 2

# imports
from functions_itlab import *
from matplotlib import pyplot as plt

if __name__ == "__main__":

     t0 = 0
     t1 = 49
     h = 1
     t = (t1-t0)+1

     kaitia_fr = 0.13
     rahui = 2

     k = 1000000
     n = 750000 
     f0 = 130000
     r = 0.5
	

     tsoln1, ysoln1 = solve_explicit_rk(dndt_quota,t0,t1,n,h,'rk4',[r,k,f0]) # initial population n input
     tsoln2, ysoln2 = solve_explicit_rk(dndt_kaitiakitanga,t0,t1,n,h,'rk4',[r,k,f0,kaitia_fr])
     tsoln3, ysoln3 = solve_explicit_rk(dndt_rahui,t0,t1,n,h,'rk4',[r,k,f0,rahui]) # --

     f, ax1 = plt.subplots(nrows=1, ncols=1) # -- wont be doing twin plots

     # for every cumulative mass we count from first time after injection first began so [0] + 1
     ax1.plot(tsoln1, ysoln1, 'k-', label='Quota')
     ax1.plot(tsoln2, ysoln2, 'b-', label='Kaitiakitanga')
     ax1.plot(tsoln3, ysoln3, 'g', label='Rahui')

     # overall graph and plot features such as titles, axis, lables, plot, etc - also includes y axis limits
     ax1.set_ylim([0,k])
     ax1.legend(loc=2)
     ax1.set_ylabel('fish population/-[millions]')
     ax1.set_xlabel('timespan/-[yrs]')
     ax1.set_title('Fish Yield Quota Methods')

     plt.show()

