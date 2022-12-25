
import numpy as np

def mech_equi(phi,C0,C1,Ch,E0,E1,Ebar,tol=1e-5,max_iter=1000,verbose=False):
	'''
		phi : phase field (composition, ordered paramter)
		C0 	: stiffness of phase 0 
		C1 	: stiffness of phase 1 
		Ch	: constant reference stiffness
		E0	: misfit strain in phase 0 (strain encapsulates phase material behaviour in terms of misfit strain: 
										eg, how much a phase will expand during phase change)
		E1	: misfit strain in phase 1
		Ebar: constant homogenenous strain
	'''

	nx = len(phi)
	k = np.fft.fftfreq(nx)
	k[0] = 1e-9  	# setting the zero frequency mode to <<1 but non-zero to avoid division by 0
					# we will also set the coefficients of this mode to 0 before performing inverse FT
					# this is because we are working with u_particular, i.e., solving for the perturbations
					# in displacement with respect to an underlying u_homogeneous. 
	
	CE = calc_stiffness(phi,C0,C1)
	ER = calc_misfit_strain(phi,E0,E1)
	ER = np.zeros(nx)
	T0 = CE*(Ebar-ER)

	Gh_ft = 1/(Ch*k*k)
	up_ft = np.zeros(nx,dtype=complex)

	iter = 0
	while True:
		up_ft[0] = 0
		Ep = np.fft.ifft(up_ft*k*1j)

		T = T0 + CE*Ep

		T_ft= np.fft.fft(T)
		delta_up_ft = Gh_ft*T_ft*(k*1j)

		up_ft += delta_up_ft

		if (np.max(np.real(delta_up_ft[1:]))<tol or iter>=max_iter):
			break
		iter+=1

	# computing elastic energy and its gradient with respect to phi
	Ep_ft = -up_ft*k*1j
	Ep_ft[0] = 0
	Ep = np.fft.ifft(Ep_ft)
	
	fE = 0.5 * (Ep-ER) * CE * (Ep-ER)
	fE_ft = np.fft.fft(fE)
	dfEdphi_ft = - fE_ft*k*1j
	dfEdphi_ft[0] = 0
	dfEdphi = np.fft.ifft(dfEdphi_ft)

	up_ft[0] = 0
	up = np.fft.ifft(up_ft)

	if verbose==True:
		delta_up_ft[0] = 0
		delta_up = np.fft.ifft(delta_up_ft)
		if iter == max_iter:
			print(f"Mechanical equilibrium stopped at max iteration: {iter}")
		else:
			print(f"Mechanical equilibrium achieved in {iter} iterations.")
		print(f"Maximum value in delta_u_p = {np.max(np.real(delta_up))}")
	
	return up, Ep, dfEdphi


def calc_stiffness(phi,C0,C1):	
	# normalize phi and perform linear interpolation
	phi = (phi-np.min(phi))/(np.max(phi)-np.min(phi))
	C = (C1-C0)*phi + C0
	return C

def calc_misfit_strain(phi,E0,E1):
	# normalize phi and perform linear interpolation
	phi = (phi-np.min(phi))/(np.max(phi)-np.min(phi))
	E = (E1-E0)*phi + E0
	return E
