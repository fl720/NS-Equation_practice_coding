#coding:utf-8
import sys
import numpy as np
import time
np.set_printoptions(threshold=sys.maxsize)
from matplotlib  import pyplot as plt 
# plt.ion()

# du/dt + c_x * du/dx + c_y * du/dy = 0

c_x = 1
c_y = 1

x_cells = 1024
y_cells = 1024

interval = 3.0
dx = interval/(x_cells -1)
dy = interval/(y_cells -1)
x = np.linspace(- interval/2, interval/2,x_cells)
y = np.linspace(- interval/2 ,interval/2,y_cells)

step = 256
dt = 0.5 * dx

# 3D - tensor
u = np.ones( [step, x_cells, y_cells])

# for i in range( int((x_cells-1)/ interval ) , int((x_cells-1) * 2 / interval ) )  :
#     for j in range( int((y_cells-1)/ interval ) , int((y_cells-1) * 2 / interval ) )  :
#         u[0][i][j] = 2

u[0][ int(1/dx) : int(2/dx) ,  int(1/dy) : int(2/dy)] = 2
# print(u[0])
        
xx , yy = np.meshgrid( x ,y )
xx = np.transpose(xx)
yy = np.transpose(yy)

ax = plt.axes(projection = '3d')
ax.plot_surface(xx,yy,u[0], cmap='viridis')
plt.show()

print(xx.shape)
print(yy.shape)
print(u[0].shape)

t0 = time.time()

# u[ 2 ] won't be updated since u[ 1 ] is unchanged!
# u[ 1: , 1: , 1:] = u[ :-1 , 1:,1:] - c_x * dt/dx * ( u[:-1 , 1: , 1:] - u[ :-1 , :-1 , 1:]) - c_y * dt/dy * ( u[ :-1 , 1: , 1:] - u[ :-1 , 1: , :-1])

for k in range(step - 1) :
    # print(u[k])
        u[k+1][1:,1:] = u[k][1:,1:] - c_x * dt/dx * ( u[k][1: , 1:] - u[k][:-1 , 1:]) - c_y * dt/dy * ( u[k][1: , 1:] - u[k][1: , :-1])

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
    
            




