import numpy as np
from f_homogenous import dfh1dc
from solver import CH1D_fd_fe
import time
import os

case = "1D_spin_noflux"

os.makedirs('./sim_data', exist_ok=True)

# system parameters
l_l = -1.
l_r =  1.
t_final = 0.01

# constants
lambda0 = 1e-3	# go for finer resolution 0.001
tau0 = 1e-5	# 0.00001 gives good results
a0 = 0.01		# a0 = (ht/tau0)/(hx/lambda0)^2
b0 = 1			# b0 = (hx/lambda0)^2
hx = lambda0
ht = (a0/(b0**2))*tau0

# grid
nx = int((l_r-l_l)/hx)+1
nt = int(t_final/ht)
X = np.linspace(l_l, l_r, nx)
T = np.linspace(0, t_final, nt)

# initialization
c = np.zeros((nx,nt))
c[:,0] = 0.5 + (np.random.rand(nx)-0.5)*0.01
# c[:,0] = 0.2
# c[int(0.3*nx):int(0.7*nx),0] += 0.5
# c[:,0] += np.exp(-((X)**2)/0.01)
# c[:,0] = c[:,0]/np.sum(c[:,0])	# normalize
print(c[:,0])

# solving the temporal evolution of concentration field
start = time.time()
c = CH1D_fd_fe(c,dfh1dc,a0,b0,nx,nt,bc="noflux")
end = time.time()
print(f"Simulation completed in: {end-start} sec.")
plot_data = {"X":X,"T":T,"c":c}
np.save(f'./sim_data/{case}.npy', plot_data)