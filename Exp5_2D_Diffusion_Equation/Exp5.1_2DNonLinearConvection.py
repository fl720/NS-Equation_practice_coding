#coding:utf-8
import sys
import numpy as np
import time
np.set_printoptions(threshold=sys.maxsize)
from matplotlib  import pyplot as plt 
# plt.ion()

# du/dt + u * du/dx + v * du/dy = 0
# dv/dt + u * dv/dx + v * dv/dy = 0

x_cells = 256
y_cells = 256

interval = 3.0
dx = interval/(x_cells -1)
dy = interval/(y_cells -1)
x = np.linspace(- interval/2, interval/2,x_cells)
y = np.linspace(- interval/2 ,interval/2,y_cells)

step = 256
dt = 0.1 * dx

# 3D - tensor
# coupled partial diff eq
u = np.ones( [step, x_cells, y_cells])
v = np.ones( [step, x_cells, y_cells])

u[0][ int(1/dx) : int(2/dx) ,  int(1/dy) : int(2/dy)] = 2
v[0][ int(1/dx) : int(2/dx) ,  int(1/dy) : int(2/dy)] = 2
        
xx , yy = np.meshgrid( x ,y )
xx = np.transpose(xx)
yy = np.transpose(yy)

print(xx.shape)
print(yy.shape)
print(u[0].shape)

t0 = time.time()

# du/dt + u * du/dx + v * du/dy = 0
# dv/dt + u * dv/dx + v * dv/dy = 0

for k in range(step - 1) :
    # print(u[k])
    u[k+1][1:,1: ] = u[k][1:,1:] - u[k][1: ,1:] * dt/dx * ( u[k][1: , 1:] - u[k][:-1 , 1:]) - v[k][1: , 1:] * dt/dy * ( u[k][1: , 1:] - u[k][1: , :-1])
    v[k+1][1:,1: ] = v[k][1:,1:] - u[k][1: ,1:] * dt/dx * ( v[k][1: , 1:] - v[k][:-1 , 1:]) - v[k][1: , 1:] * dt/dy * ( v[k][1: , 1:] - v[k][1: , :-1])

    # plt.cla()
    # ax = plt.axes(projection = '3d')
    # ax.plot_surface(xx,yy,u[k], cmap='viridis')
    # plt.pause(1./1024)

t1 = time.time()

print( t1 - t0 )
    
# plt.ioff()
ax = plt.axes(projection = '3d')
ax.plot_surface(xx,yy,u[-1], cmap='viridis')
plt.show()
    
            







