#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import time

# plt.ion()

'''
Laplace Euqtion :

ddp/ddx + ddp/ddy = 0

with B.C.s:

p(0, y) = 0
p(2, y) = y
dp / dy = 0 at y = 0 or 1

'''
# variables defination
x = 257
y = 129
x_interval = 2.
y_interval = 1.
dx = x_interval/(x-1)
dx2 = dx**2
dy = y_interval/(y-1)
dy2 = dy**2

p = np.zeros([x,y]) # [256, 128]

x_axis = np.linspace(0,x_interval , x)
y_axis = np.linspace(0,y_interval , y)
X,Y = np.meshgrid(x_axis , y_axis)
X = np.transpose(X)
Y = np.transpose(Y)

# initial value setting
p[0, :] = 0 
p[-1,:] = np.linspace(0, y_interval, y) # p(2, y) = y

# ax = plt.axes(projection = "3d")
# ax.plot_surface(X,Y,p,cmap=cm.viridis)
# ax.set_xlabel('$x$')
# ax.set_ylabel('$y$');
# plt.show()

# Iteration
p_next = p.copy()
distance = 1
e = 1e-5 # 0.000001

t0 = time.time()

cnt = 0
while distance > e:
    cnt += 1
    # if cnt % 100 == 0:
    #     print(cnt, distance)
    #     plt.cla()
    #     ax = plt.axes(projection = "3d")
    #     ax.plot_surface(X,Y,p,cmap=cm.viridis)
    #     plt.pause(0.1)
    
    #p_next[ 1:-1 , 1:-1 ] = ( (p[2: ,1:-1] + p[:-2 , 1:-1]) *dy2 + (p[1:-1 , 2:] + p[1:-1 , :-2]) * dx2  ) / (2*(dx2 +dy2))
    p_next[ 1:-1 , 1:-1 ] = ( (p[2: ,1:-1] + p[:-2 , 1:-1] + p[1:-1 , 2:] + p[1:-1 , :-2]) ) / 4

    p_next[ :, 0]  = p_next[ : , 1] # dp / dy = 0 at y = 0 
    p_next[ :, -1] = p_next[ : , -2] # dp / dy = 0 at y = 1
    
    distance = np.sum(np.abs(p_next - p)) / np.sum(np.abs(p))

    p = p_next.copy()

print(cnt, distance)

t1 = time.time()

print(t1 - t0)

# plt.ioff()
ax = plt.axes(projection = "3d")
ax.plot_surface(X,Y,p,cmap=cm.viridis)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$');
plt.show()
