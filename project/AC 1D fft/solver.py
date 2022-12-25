import numpy as np
from utilities import mech_equi

def AC1D_fft_fe(phi,dfhdphi,nt,ht,lambda0,b0,C0=0,C1=0,Ch=0,E0=0,E1=0,Ebar=0,verbose=False):

	nx = len(phi)
	k = np.fft.fftfreq(nx)/lambda0

	elastic = True
	if C0==0 and C1==0 and Ch==0 and E0==0 and E1==0 and Ebar==0:
		elastic = False

	# elastic = False
	phi_all = np.zeros((nt+1,nx))
	phi_all[0,:] = phi

	t=1
	while True:
		if verbose == True:
			print(f"Time step: {t}/{nt}")

		if elastic==True:
			_,_,dfEdphi = mech_equi(phi,lambda0,C0,C1,Ch,E0,E1,Ebar,max_iter=100000,verbose=verbose)
			# print((dfhdphi(phi) - np.real(dfEdphi))/dfhdphi(phi))
			g = dfhdphi(phi) + np.real(dfEdphi)
			print(np.max(np.abs(dfhdphi(phi))))
			print(np.max(np.abs(np.real(dfEdphi))))
		else: 
			g = dfhdphi(phi)

		phi_ft = np.fft.fft(phi)
		g_ft = np.fft.fft(g)

		phi_ft = (phi_ft - b0*g_ft)/(1+b0*k*k)

		phi = np.real(np.fft.ifft(phi_ft))
		phi_all[t,:] = phi
		
		t += 1
		if t>nt:	break
		

	return phi_all


