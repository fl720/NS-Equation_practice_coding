#coding:utf-8

'''
Burgers Euqtion
du/dt + u * du/dx + v * du/dy = nu * ddu/ddx + nu * ddu/ddy
dv/dt + u * dv/dx + v * dv/dy = nu * ddv/ddx + nu * ddv/ddy
'''

import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt

###variable declarations
x = 64
y = 64
interval = 4.0
dx = interval / (x - 1)
dy = interval / (y - 1)
sigma = .0001
nu = 0.01
nt = 1024 * 16
dt = sigma * dx * dy / nu

u = np.ones((x, y))
v = np.ones((x, y))
u_next = np.ones((x, y)) 
v_next = np.ones((x, y))

x_axis = np.linspace(0, interval, x)
y_axis = np.linspace(0, interval, y)
X, Y = np.meshgrid(x_axis, y_axis)
X = np.transpose(X)
Y = np.transpose(Y)

###Assign initial conditions
for i in range(x):
    for j in range(y):
        if ((i - x/2) * dx)**2 + ((j - y/2)*dy)**2 <= 1:
            u[i][j] = 2 
            v[i][j] = 2 

### plot Initial Condition
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, u[:], cmap=cm.viridis, rstride=1, cstride=1)
#ax.plot_surface(X, Y, v[:], cmap=cm.viridis, rstride=1, cstride=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$');
plt.show();

from sys import getsizeof
print(getsizeof(u)/1024)

## main loop of iteration
for n in range(nt + 1):

    u_next[1:-1, 1:-1] = (u[1:-1, 1:-1] -
                     dt / dx * u[1:-1, 1:-1] * 
                     (u[1:-1, 1:-1] - u[0:-2, 1:-1]) - 
                     dt / dy * v[1:-1, 1:-1] * 
                     (u[1:-1, 1:-1] - u[1:-1, 0:-2]) + 
                     nu * dt / dx**2 * 
                     (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[0:-2, 1:-1]) + 
                     nu * dt / dy**2 * 
                     (u[1:-1,2:] - 2 * u[1:-1, 1:-1] + u[1:-1, 0:-2]) )
    
    v_next[1:-1, 1:-1] = (v[1:-1, 1:-1] - 
                     dt / dx * u[1:-1, 1:-1] *
                     (v[1:-1, 1:-1] - v[0:-2, 1:-1]) -
                     dt / dy * v[1:-1, 1:-1] * 
                    (v[1:-1, 1:-1] - v[1:-1, 0:-2]) + 
                     nu * dt / dx**2 * 
                     (v[2:, 1:-1] - 2 * v[1:-1, 1:-1] + v[0:-2, 1:-1]) +
                     nu * dt / dy**2 *
                     (v[1:-1, 2:] - 2 * v[1:-1, 1:-1] + v[1:-1, 0:-2]))
     
    u_next[0, :] = 1
    u_next[-1, :] = 1
    u_next[:, 0] = 1
    u_next[:, -1] = 1
    
    v_next[0, :] = 1
    v_next[-1, :] = 1
    v_next[:, 0] = 1
    v_next[:, -1] = 1

    u = u_next.copy()
    v = v_next.copy()

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=1, cstride=1)
#ax.plot_surface(X, Y, v, cmap=cm.viridis, rstride=1, cstride=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$');
plt.show();