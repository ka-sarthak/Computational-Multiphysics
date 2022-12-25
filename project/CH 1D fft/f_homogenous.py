def fh1(c):
	return 0.5*c*c*(1-c)*(1-c) 

def dfh1dc(c):
	return 1*(c*(1-c)**2 - (1-c)*c*c)

def fh2(c):
	return 0.25*(1-c*c)*(1-c*c)

def dfh2dc(c):
	return -c*(1-c*c)