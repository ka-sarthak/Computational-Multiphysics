import numpy as np
import matplotlib.pyplot as plt
import os

case = "1D_spin_noflux"

os.makedirs('sim_plots',exist_ok=True)
plot_data = np.load(f'./sim_data/{case}.npy', allow_pickle=True)
X = plot_data[()]["X"]
T = plot_data[()]["T"]
c = plot_data[()]["c"]
nt = len(T)

print(c.shape)

# checking mass conservation
summed = np.sum(c,axis=0)
print("Mass conservation data (summed up concentrations): ")
plt.plot(T,summed)
plt.savefig(f"./sim_plots/{case}_mass_conservation.png")
print(f"Loss of {100*(summed[0]-summed[-1])/summed[0]}% mass.")


# plotting

plt.figure()
plt.plot(X[:],c[:,0],label= f"t={format(T[0],'0.3f')}")
plt.plot(X[:],c[:,int(nt/3)],label= f"t={format(T[int(nt/3)],'0.3f')}",color='black')
plt.plot(X[:],c[:,int(2*nt/3)],label= f"t={format(T[int(2*nt/3)],'0.3f')}",color='yellow')
# plt.plot(X[:],c[:,int(3*nt/4)],label= f"t={format(T[int(3*nt/4)],'0.3f')}")
plt.plot(X[:],c[:,-1],label= f"t={format(T[-1],'0.3f')}",color='red')
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.savefig(f"./sim_plots/{case}.png", transparent=True, bbox_inches='tight')
plt.close()

# plt.figure()
# imdata = c[:,:]
# print(imdata.shape)
# plt.imshow(imdata)
# plt.savefig(f"./sim_plots/1D_CH_spin.png", transparent=True, bbox_inches='tight')
# plt.close()