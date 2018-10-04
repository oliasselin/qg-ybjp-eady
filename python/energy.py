import numpy as np
#import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt

run='storm/test5'

timestep=0.001
L_scale=1600000/(2*np.pi)
U_scale=0.1/(2*np.pi)
eddy_days=(L_scale/U_scale)/(3600*24)

path = '/scratch/05518/oasselin/'+run+'/output/we.dat'
energy = np.loadtxt(path)
time_days=energy[:,0]*eddy_days
png_filename='energy.png'

#plt.plot(time_days,energy[:,1]/energy[0,1],label='WKE')
#plt.plot(time_days,energy[:,2]/energy[0,1],label='WPE')
#plt.xlabel('Time (days)')
#plt.ylabel('Energy')
#plt.title('Wave kinetic and potential energy evolution')
#plt.xlim((0,100))
#plt.ylim((0,1))
#plt.show() 

fig, ax = plt.subplots(1)
plt.plot(time_days,energy[:,1]/energy[0,1],label='WKE')
plt.plot(time_days,energy[:,2]/energy[0,1],label='WPE')
plt.title('Wave kinetic and potential energy evolution')
ax.set_xlim([0,100])
ax.set_ylim([0,1])
ax.set_xlabel('Time (days)')
ax.set_ylabel('Energy')
ax.legend()
fig.savefig(png_filename)
plt.show()
#plt.close(fig)
