import numpy as np
from utilities import mech_equi
from tqdm import tqdm

def CH1D_fft_fe(c,dfhdc,a0,nt,ht,lambda0,C0=0,C1=0,Ch=0,E0=0,E1=0,Ebar=0,verbose=False):

	nx = len(c)
	k = np.fft.fftfreq(nx)/lambda0

	elastic = True
	if C0==0 and C1==0 and Ch==0 and E0==0 and E1==0 and Ebar==0:
		elastic = False

	elastic = False
	# c_all = np.zeros((nt+1,nx))
	# c_all[0,:] = c

	t=1
	# pbar = tqdm(total=nt, initial=t)
	while True:
		# pbar.update(1)
		if verbose == True:
			print(f"Time step: {t}/{nt}")

		if elastic==True:
			_,_,dfEdc = mech_equi(c,C0,C1,Ch,E0,E1,Ebar,max_iter=100000,verbose=verbose)
			g = dfhdc(c) + np.real(dfEdc)
		else: 
			g = dfhdc(c)

		c_ft = np.fft.fft(c)
		g_ft = np.fft.fft(g)

		c_ft = (c_ft - a0*k*k*g_ft)/(1+a0*k*k*k*k)

		c = np.fft.ifft(c_ft)
		# c_all[t,:] = np.real(c)
		
		t += 1
		if t>nt:	break
	# pbar.close()

	return np.real(c)


