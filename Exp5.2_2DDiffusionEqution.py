#coding:utf-8

# du/dt  = nu * ddu/ddx + nu * ddu/ddy

import numpy as np
import time
from matplotlib import pyplot as plt
plt.ion()

x = 256
y = 256
interval = 4.0
dx = interval / (x-1)
dy = interval / (y-1)

x_axis = np.linspace(0 , interval , x)
y_axis = np.linspace(0 , interval , y)
xx, yy = np.meshgrid(x_axis, y_axis)
xx = np.transpose(xx)
yy = np.transpose(yy)

nt = 1024 * 4
dt = 1./256 * dx

DC = 1

u = np.ones( [ nt + 1 , x , y ] )
for i in range(x):
    for j in range(y):
        if ((i - x/2) * dx)**2 + ((j - y/2)*dy)**2 <= 1:
            u[0][i][j] = 2 

# u[0][int( 1/dx * 1): int( 1/dx * 2) + 1 , int( 1/dy * 1): int( 1/dy * 2) + 1 ] = 2 

t0 = time.time()

for k in range ( nt ) :
    if k % 64 == 0:
        plt.cla()
        ax3 = plt.axes(projection = '3d')
        ax3.set_zlim(1, 2)
        ax3.contour(xx, yy, u[k], offset = 1) # 等高线
        ax3.plot_surface(xx, yy, u[k], cmap='viridis')
        plt.pause(dt)

    u[k+1][1: -1, 1: -1] = u[k][1:-1 , 1:-1] + DC * dt *( (u[k][2:,1:-1] - 2* u[k][1:-1 , 1:-1] + u[k][:-2 , 1:-1])/dx**2 + (u[k][1:-1, 2:] -2* u[k][1:-1 , 1:-1] +u[k][1:-1, :-2])/dy**2 )
    
    # marginal cells
    # u[k+1][0, 1:-1] = u[k][0 , 1:-1] + DC * dt *( (u[k][2,1:-1] - 2* u[k][1 , 1:-1] + u[k][0 , 1:-1])/dx**2 + (u[k][0, 2:] -2* u[k][0 , 1:-1] +u[k][0, :-2])/dy**2 )
    # u[k+1][-1, 1:-1] = u[k][-1 , 1:-1] + DC * dt *( (u[k][-1,1:-1] - 2* u[k][-2 , 1:-1] + u[k][-3 , 1:-1])/dx**2 + (u[k][-1, 2:] -2* u[k][-1 , 1
    # :-1] +u[k][-1, :-2])/dy**2 )
    # u[k+1][1: -1, 0] = u[k][1:-1 , 0] + DC * dt *( (u[k][2:,0] - 2* u[k][1:-1 , 0] + u[k][:-2 , 0])/dx**2 + (u[k][1:-1, 2] -2* u[k][1:-1 , 1] +u[k][1:-1, 0])/dy**2 )
    # u[k+1][1: -1, -1] = u[k][1:-1 , -1] + DC * dt *( (u[k][2:, -1] - 2* u[k][1:-1 , -1] + u[k][:-2 , -1])/dx**2 + (u[k][1:-1, -1] -2* u[k][1:-1 , -2] +u[k][1:-1, -3])/dy**2 )

    # corner cells
    # u[k+1][0,0] = u[k][0,0] + DC * dt *( (u[k][2,0] - 2* u[k][1, 0] + u[k][0 , 0])/dx**2 + (u[k][0,2] -2* u[k][0,1] +u[k][0,0])/dy**2 )
    # u[k+1][-1,0] = u[k][-1,0] + DC * dt *( (u[k][-1,0] - 2* u[k][-2, 0] + u[k][-3 , 0])/dx**2 + (u[k][-1,2] -2* u[k][-1,1] +u[k][-1,0])/dy**2 )
    # u[k+1][-1,-1] = u[k][-1,-1] + DC * dt *( (u[k][-1,-1] - 2* u[k][-2, -1] + u[k][-3 , -1])/dx**2 + (u[k][-1,-3] -2* u[k][-1,-2] +u[k][-1,-1])/dy**2 )
    # u[k+1][0,-1] = u[k][0,-1] + DC * dt *( (u[k][2,-1] - 2* u[k][1, -1] + u[k][0 , -1])/dx**2 + (u[k][0,-3] -2* u[k][0,-2] +u[k][0,-1])/dy**2 )

t1 = time.time()

print(t1 - t0)

plt.ioff()
ax3 = plt.axes(projection = '3d')
ax3.plot_surface(xx, yy, u[k], rstride = 1, cstride = 1, cmap='viridis')
ax3.contour(xx, yy, u[k], offset = 1) # 等高线
plt.show()