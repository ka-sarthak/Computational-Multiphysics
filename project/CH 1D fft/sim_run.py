import numpy as np
from f_homogenous import dfh1dc
from solver import CH1D_fft_fe
import time
import os

os.makedirs('./sim_data', exist_ok=True)

# system parameters
l_l = -1
l_r = 1
t_final = 0.0001

# constants
lambda0 = 1e-3		# material length scale = sqrt(2*psi_G0/psi_H0)
tau0 	= 1e-8			# time length scale = lambda^2/(m0 * psi_H0)
a0 		= 0.01				# time scaling, ration between numerical time scale and material time scale
ht 		= a0*tau0
hx 		= lambda0	# length scaling is set to 1, that is numerical length scale is equal to material length scale

# elastic constants
C0 = 1
C1 = 100
Ch = 50
E0 = 0
E1 = 0
Ebar = 1 

# grid
nx = int((l_r-l_l)/hx)
nt = int(t_final/ht)
X = np.linspace(l_l, l_r, nx)
T = np.linspace(0, t_final, nt)

# initialization
c = np.ones(nx)*0.2
c[int(0.3*nx):int(0.7*nx)] += 0.5
# c += np.exp(-((X)**2)/0.01)
# c = np.exp(-((X-0.5)**2)/0.01)
# c = np.exp(-((X-0.65)**2)/0.01)+np.exp(-((X-0.35)**2)/0.01)
# c = -np.ones(nx)
# c[int(nx/2-200):int(nx/2+200)] = 1
c_plot = np.zeros((2,nx))
c_plot[0,:] = c
# solving the temporal evolution of concentration field
start = time.time()
c = CH1D_fft_fe(c,dfh1dc,a0,nt,ht,C0,C1,Ch,E0,E1,Ebar,verbose=True)
end = time.time()
print(f"Simulation completed in: {end-start} sec.")

# saving plotting data
c_plot[1,:] = c
plot_data = {"X":X,"T":T,"c":c_plot}
np.save('./sim_data/1D_CH_no_elastic.npy', plot_data)