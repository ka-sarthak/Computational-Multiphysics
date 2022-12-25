from tabnanny import verbose
import numpy as np 
import matplotlib.pyplot as plt
from utilities import mech_equi

# constants
l = 1.0 	# assuming l to be 1.0
X = np.linspace(0,l,101)
C0 = 1
C1 = 100
Ch = 50
E0 = 0
E1 = 0
Ebar = 1


# initializing phi
# centered gaussian
phi = np.exp(-((X-0.5)**2)/0.01)
# square well
# phi = -np.ones(len(X))
# phi[25:76] = 1

# find u after solving for mechanical equilibrium
tol = 1e-1
while True:
	print(tol)
	if tol<1e-13:
		break
	up,Ep,_ = mech_equi(phi,C0,C1,Ch,E0,E1,Ebar,tol=tol,max_iter=10000000,verbose=True)
	tol/=10

# fig,ax = plt.subplots(1,3, figsize=(20,6))
# ax[0].plot(X,phi)
# ax[1].plot(X,np.real(up)/(Ebar*l))
# ax[2].plot(X,np.real(Ep)/Ebar)
# ax[0].set_title(r"$\phi$", fontsize=24)
# ax[1].set_title(r"$\frac{u_p}{\overline{E} l_x}$", fontsize=24)
# ax[2].set_title(r"$\frac{\tilde{E}}{\overline{E}}$", fontsize=24)
# ax[0].set_xlabel("x", fontsize=18)
# ax[1].set_xlabel("x", fontsize=18)
# ax[2].set_xlabel("x", fontsize=18)
# plt.savefig("test_mech_equi.png", transparent=True)