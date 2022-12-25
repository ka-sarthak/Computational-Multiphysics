import numpy as np
from f_homogenous import dfhdphi
from solver import AC1D_fd_fe
import time
import os

os.makedirs('./sim_data', exist_ok=True)

# system parameters
l_l = 0
l_r = 1
t_final = 4

# constants
lambda0 = 0.001	# go for finer resolution
tau0 	= 0.1
a0 		= 0.01
b0 		= 0.01
ht 		= b0*tau0
hx 		= lambda0

# boundary condition
bc = "periodic"	# periodic, noflux, periodic-noflux

# grid
nx = int((l_r-l_l)/hx)
nt = int(t_final/ht)
X = np.linspace(l_l, l_r, nx)
T = np.linspace(0, t_final, nt)

# initialization
phi0 = np.zeros((nx,nt+1))
# phi0[:,0] = np.sin(3*X-np.pi/2)+2*np.exp(-(X**2)/0.02) 	# small hill in the center grows to become phase 1
# phi0[:,0] = np.sin(3*X-np.pi/2)+np.exp(-(X**2)/0.02)	# small hill in the center dies to become phase -1
# phi0[:,0] = 0.53*X + 0.47*np.sin((-1.5*np.pi)*X)		# crests become phase 1 and troughs become phase -1
# phi0[:,0] = np.sin(X)		# crests become phase 1 and troughs become phase -1
phi0[:,0] = np.exp(-((X-0.65)**2)/0.01)+np.exp(-((X-0.35)**2)/0.01)

# solving the temporal evolution of concentration field
start = time.time()
phi = AC1D_fd_fe(phi0,dfhdphi,a0,b0,nx,nt,bc)
end = time.time()
print(f"Simulation completed in: {end-start} sec.")
plot_data = {"X":X,"T":T,"phi":phi}
np.save('./sim_data/1D_AC.npy', plot_data)