import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import os

os.makedirs('sim_plots',exist_ok=True)
plot_data = np.load('./sim_data/1D_AC.npy', allow_pickle=True)
X = plot_data[()]["X"]
T = plot_data[()]["T"]
phi = plot_data[()]["phi"]
nt = len(T)

print(phi.shape)

# plotting
plt.figure()
# for t in np.arange(0,len(T),1):
#     plt.plot(X[:],phi[t,:],label= f"t={format(T[t],'0.2f')}")
plt.plot(X[:],phi[:,0],label= f"t={format(T[0],'0.2f')}")
plt.plot(X[:],phi[:,int(nt/4)],label= f"t={format(T[int(nt/4)],'0.2f')}")
plt.plot(X[:],phi[:,int(nt/2)],label= f"t={format(T[int(nt/2)],'0.2f')}")
plt.plot(X[:],phi[:,int(3*nt/4)],label= f"t={format(T[int(3*nt/4)],'0.2f')}")
plt.plot(X[:],phi[:,-1],label= f"t={format(T[-1],'0.2f')}")
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.savefig(f"./sim_plots/1D_AC.png", transparent=True, bbox_inches='tight')
plt.close()

# # plotting heatmap
# plt.figure(figsize=(6,6))
# plt.imshow(phi[:,:])
# plt.set_cmap('seismic')
# plt.colorbar()
# plt.tick_params(left=False,
#                 bottom=False,
#                 labelleft=False,
#                 labelbottom=False)
# plt.savefig("./sim_plots/1D_AC_heatmap.png", dpi=400, transparent=True, bbox_inches='tight')
# plt.close()

# # plotting surface
# t,x = np.meshgrid(T,X)
# fig = plt.figure()
# axes = fig.gca(projection ='3d')
# axes.plot_surface(x, t, phi, cmap=cm.summer, shade=True, lightsource="hillshade")
# plt.savefig("./sim_plots/1D_AC_surface.png", dpi=400, transparent=True, bbox_inches='tight')
# # plt.close()
# plt.show()