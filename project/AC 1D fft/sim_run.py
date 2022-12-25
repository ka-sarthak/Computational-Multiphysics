import numpy as np
from f_homogenous import dfhdphi
from solver import AC1D_fft_fe
import time
import os

os.makedirs('./sim_data', exist_ok=True)

case = '1D_AC_no_elastic_scaled_k'
# system parameters
l_l = 0
l_r = 1
t_final = 40

# constants
lambda0 = 0.001		# material length scale = sqrt(2*phi_G0/phi_H0)
tau0 	= 100		# time length scale = 1/(m0 * phi_H0)
b0 		= 0.01		# time scaling, ration between numerical time scale and material time scale
ht 		= b0*tau0
hx 		= lambda0	# length scaling is set to 1, that is numerical length scale is equal to material length scale

# elastic constants
C0 = 10
C1 = 200
Ch = 100
E0 = 0
E1 = 0
Ebar = 1 

# grid
nx = int((l_r-l_l)/hx)
nt = int(t_final/ht)
X = np.linspace(l_l, l_r, nx)
T = np.linspace(0, t_final, nt)

# initialization
# phi = np.exp(-((X-0.5)**2)/0.01)
phi = np.exp(-((X-0.65)**2)/0.01)+np.exp(-((X-0.35)**2)/0.01)
# phi = -np.ones(nx)
# phi[int(nx/2-200):int(nx/2+200)] = 1

# solving the temporal evolution of concentration field
start = time.time()
phi_all = AC1D_fft_fe(phi,dfhdphi,nt,ht,lambda0,b0,C0,C1,Ch,E0,E1,Ebar,verbose=True)
end = time.time()
print(f"Simulation completed in: {end-start} sec.")

# saving plotting data
plot_data = {"X":X,"T":T,"phi":phi_all}
np.save(f'./sim_data/{case}.npy', plot_data)