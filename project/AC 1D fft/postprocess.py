import numpy as np
import matplotlib.pyplot as plt
import os

case  = '1D_AC_no_elastic_scaled_k'
os.makedirs('sim_plots',exist_ok=True)
plot_data = np.load(f'./sim_data/{case}.npy', allow_pickle=True)
X = plot_data[()]["X"]
T = plot_data[()]["T"]
phi = plot_data[()]["phi"]
nt = len(T)

case_elas  = '1D_AC_elastic_scaled_k'
os.makedirs('sim_plots',exist_ok=True)
plot_data = np.load(f'./sim_data/{case}.npy', allow_pickle=True)
X = plot_data[()]["X"]
T = plot_data[()]["T"]
phi_elas = plot_data[()]["phi"]
nt = len(T)

print(phi.shape)
print(np.min(phi-phi_elas))

# plotting
plt.figure()
# for t in np.arange(0,len(T),1):
#     plt.plot(X[:],phi[t,:],label= f"t={format(T[t],'0.2f')}")
plt.plot(X[:],phi[0,:],label= f"t={format(T[0],'0.2f')}")
plt.plot(X[:],phi[int(nt/4),:],label= f"t={format(T[int(nt/4)],'0.2f')}")
plt.plot(X[:],phi[int(nt/2),:],label= f"t={format(T[int(nt/2)],'0.2f')}")
plt.plot(X[:],phi[int(3*nt/4),:],label= f"t={format(T[int(3*nt/4)],'0.2f')}")
plt.plot(X[:],phi[-1,:],label= f"t={format(T[-1],'0.2f')}")
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.savefig(f"./sim_plots/{case}.png", transparent=True, bbox_inches='tight')
plt.close()
