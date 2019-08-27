from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt


import numpy as np
fig = plt.figure()

ax = fig.add_subplot(111,projection='3d', aspect='equal')


len = 100

k = np.linspace(-12,15,len)

xx, yy = np.meshgrid(k,k)
n = np.array([1,-1,-1]).reshape((3,1))

c = 9
z = ((c-n[0]*xx-n[1]*yy)*1.0)/(n[2])
P = np.array([3,-2,-4]).reshape((3,1))

l = np.array([2,-1,3]).reshape((3,1))


l_p = np.zeros((3,len))

lam = np.linspace(-5,6,len)

for i in range(len):

    temp1 = P + lam[i]*l

    l_p[:,i]= temp1.T

ax.plot_surface(xx, yy, z, color='yellow',alpha=0.8)
plt.plot(l_p[0,:],l_p[1,:],l_p[2,:],label="Given Line", color='red')

ax.scatter(P[0], P[1], P[2], color='blue')
ax.text(2.9, -1.9, -2, 'P', color='blue')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend()
plt.grid()
plt.show()
