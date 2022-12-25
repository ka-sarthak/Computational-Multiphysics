import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('sim_plots',exist_ok=True)
plot_data = np.load('./sim_data/1D_CH_no_elastic.npy', allow_pickle=True)
X = plot_data[()]["X"]
T = plot_data[()]["T"]
c = plot_data[()]["c"]
nt = len(T)

print(T)
print(c.shape)

# plotting
plt.figure()
# for t in np.arange(0,len(T),1):
#     plt.plot(X[:],c[t,:],label= f"t={format(T[t],'0.2f')}")
plt.plot(X[:],c[0,:],label= f"t={format(T[0],'0.6f')}")
# plt.plot(X[:],c[int(nt/4),:],label= f"t={format(T[int(nt/4)],'0.2f')}")
# plt.plot(X[:],c[int(nt/2),:],label= f"t={format(T[int(nt/2)],'0.2f')}")
# plt.plot(X[:],c[int(3*nt/4),:],label= f"t={format(T[int(3*nt/4)],'0.2f')}")
plt.plot(X[:],c[-1,:],label= f"t={format(T[-1],'0.6f')}")
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.savefig(f"./sim_plots/1D_CH_no_elasticity.png", transparent=True, bbox_inches='tight')
plt.close()
