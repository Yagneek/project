# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:06:56 2019

@author: pyagn
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

len=100
theta=np.linspace(0,2*np.pi,len)
V=np.array(([3,0],[0,27]))
u=np.array([0,0])
F=-51
O=np.array([0,0])
l,m=LA.eig(V/-F)
A = np.array([np.sqrt(34),0])
B = np.array([0,np.sqrt(34)/3])
y = np.zeros((2,len))
a=1/l[0]**0.5
b=1/l[1]**0.5
print(a)
print(b)

y[0,:] = a*np.cos(theta)

y[1,:] = b*np.sin(theta)
P=np.array([(17/2)**0.5,(17/18)**0.5])
m=np.array([3/np.sqrt(10),-1/np.sqrt(10)])
len =50

x_P = np.zeros((2,len))

lam_1 = np.linspace(-5,5,len)

for i in range(len):

    temp1 = P + lam_1[i]*m
    x_P[:,i]= temp1.T
    
plt.plot(y[0,:],y[1,:],label='Ellipse at origin')
plt.plot(x_P[0,:],x_P[1,:],label='Required Tangent', color='red')
plt.plot(O[0], O[1], 'o')

plt.text(O[0] * (1 - 0.1), O[1] * (1 + 0.1) , 'O')
plt.plot(O[0], O[1], 'o')

P1=np.array([(51/4)**0.5,(17/36)**0.5])
m1=np.array([np.sqrt(3)/2,-1/2])

x_P1 = np.zeros((2,len))
lam_11 = np.linspace(-5,5,len)

for i in range(len):

    temp11 = P1 + lam_11[i]*m1

    x_P1[:,i]= temp11.T
P2=np.array([(17/4)**0.5,(17/12)**0.5])
m2=np.array([(3*np.sqrt(3))/(2*np.sqrt(7)),-1/(2*np.sqrt(7))])

x_P2 = np.zeros((2,len))
lam_22 = np.linspace(-5,7,len)

for i in range(len):

    temp22 = P2 + lam_22[i]*m2

    x_P2[:,i]= temp22.T

plt.plot(x_P1[0,:],x_P1[1,:],label='Random tangent 1', color='grey')
plt.plot(x_P2[0,:],x_P2[1,:],label='Random tangent 2', color='grey')

plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 - 0.1), P[1] * (1 + 0.1) , 'P')

plt.text(A[0] * (1 - 0.1), A[1] * (1 + 0.1) , 'A')
plt.plot(A[0], A[1], 'o')

plt.text(B[0] * (1 - 0.1), B[1] * (1 + 0.1) , 'B')
plt.plot(B[0], B[1], 'o')

plt.axis('equal')

plt.xlabel('$x$');plt.ylabel('$y$')

plt.legend(loc='best')

plt.grid()
plt.show()
