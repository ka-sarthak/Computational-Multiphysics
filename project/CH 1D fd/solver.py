import numpy as np
from tqdm import tqdm

def CH1D_fd_fe(c,dfhdc,a0,b0,nx,nt,bc="noflux"):
	u = np.zeros((nx,nt))
	
	for t in tqdm(range(nt-1)):
		if bc == "periodic":
			c[0,t+1] = c[0,t] + a0*(u[1,t]-2*u[0,t]+u[-1,t])
			u[0,t+1] = dfhdc(c[0,t+1]) - b0*(c[1,t+1]-2*c[0,t+1]+c[-1,t+1])

			for x in range(1,nx-1):
				c[x,t+1] = c[x,t] + a0*(u[x+1,t]-2*u[x,t]+u[x-1,t])
				u[x,t+1] = dfhdc(c[x,t+1]) - b0*(c[x+1,t+1]-2*c[x,t+1]+c[x-1,t+1])

			c[-1,t+1] = c[-1,t] + a0*(u[0,t]-2*u[-1,t]+u[-2,t])
			u[-1,t+1] = dfhdc(c[-1,t+1]) - b0*(c[0,t+1]-2*c[-1,t+1]+c[-2,t+1])
		if bc == "noflux":
			c[0,t+1] = c[0,t] + a0*(u[1,t]-u[0,t])
			u[0,t+1] = dfhdc(c[0,t+1]) - b0*(c[1,t+1]-c[0,t+1])

			for x in range(1,nx-1):
				c[x,t+1] = c[x,t] + a0*(u[x+1,t]-2*u[x,t]+u[x-1,t])
				u[x,t+1] = dfhdc(c[x,t+1]) - b0*(c[x+1,t+1]-2*c[x,t+1]+c[x-1,t+1])

			c[-1,t+1] = c[-2,t+1]
			u[-1,t+1] = u[-2,t+1]

		if bc == "periodic-noflux":
			c[0,t+1] = c[0,t] + a0*(u[1,t]-u[0,t])
			u[0,t+1] = dfhdc(c[0,t+1]) - b0*(c[1,t+1]-c[0,t+1])

			for x in range(1,nx-1):
				c[x,t+1] = c[x,t] + a0*(u[x+1,t]-2*u[x,t]+u[x-1,t])
				u[x,t+1] = dfhdc(c[x,t]) - b0*(c[x+1,t+1]-2*c[x,t+1]+c[x-1,t+1])

			c[-1,t+1] = c[0,t+1]
			u[-1,t+1] = u[0,t+1]

	return c