
def AC1D_fd_fe(phi,dfhdphi,a0,b0,nx,nt,bc="noflux"):
	'''
		By adding boundary condition, we are putting constraints directly into the system of equation. 
		Number of equations to be solved becomes less when BC are specified. 
		This is possible because of simpler 1D system and absence of multi-physics situation. 
		When equation system is complex, we can use active constraints in the optimization for BC, e.g., using Langrange multipliers. 
	'''
	t=1
	while True:
		if bc == "periodic":
			phi[0,t] = phi[0,t-1] + a0*(phi[1,t-1]-2*phi[0,t-1]+phi[-1,t-1]) - b0*dfhdphi(phi[0,t-1])
			for x in range(1,nx-1):
				phi[x,t] = phi[x,t-1] + a0*(phi[x+1,t-1]-2*phi[x,t-1]+phi[x-1,t]) - b0*dfhdphi(phi[x,t-1])
			phi[-1,t] = phi[-1,t-1] + a0*(phi[0,t]-2*phi[-1,t-1]+phi[-2,t]) - b0*dfhdphi(phi[-1,t-1])
		elif bc == "noflux":
			# forward Euler for no-flux at left boundary -> phi_1 - phi_0 = 0
			phi[0,t] = phi[0,t-1] + a0*(phi[1,t-1]-phi[0,t-1]) - b0*dfhdphi(phi[0,t-1])
			
			# internal domain
			for x in range(1,nx-1):
				phi[x,t] = phi[x,t-1] + a0*(phi[x+1,t-1]-2*phi[x,t-1]+phi[x-1,t]) - b0*dfhdphi(phi[x,t-1])
			
			# forward Euler for no-flux at right boundary -> phi_n - phi_n-1 = 0
			phi[-1,t] = phi[-2,t]#phi[-1,t-1] + a0*(-phi[-1,t-1]+phi[-2,t]) - b0*dfhdphi(phi[-1,t-1])

		elif bc == "periodic-noflux":
			phi[0,t] = phi[0,t-1] + a0*(phi[1,t-1]-phi[0,t-1]) - b0*dfhdphi(phi[0,t-1])
			
			# internal domain
			for x in range(1,nx-1):
				phi[x,t] = phi[x,t-1] + a0*(phi[x+1,t-1]-2*phi[x,t-1]+phi[x-1,t]) - b0*dfhdphi(phi[x,t-1])
			
			phi[-1,t] = phi[0,t]
		else:
			print(f"Error: Unknown boundary condition {bc}")
			exit()
		
		print(f"Time step: {t}/{nt}")
		t += 1
		if t>nt:	break

	return phi