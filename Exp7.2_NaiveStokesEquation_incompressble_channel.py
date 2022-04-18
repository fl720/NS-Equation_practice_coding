#coding:utf-8

import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import cm

'''
Navie Stokes Euation with incompressble fluid:

--------------------------

    du/dt + udu/dt + vdu/dy = -1/rho * dp/dx + viscosity * laplacian u + F
    dv/dt + udv/dt + vdv/dy = -1/rho * dp/dx + viscosity * laplacian v
    ddp/ddx + ddp/ddy = -rho * ( (du/dx)**2 + 2* du/dy * dv/dx + (dv/dy)**2 )

    where F = 1
    
With Initial Conditions:

    u = 0

    v = 0

    p = 0

With Boundary Conditions:

    u = 0 at (y = 0 or y = 2)
    v = 0 at (y = 0 or y = 2)
    dp / dy = 0 at (y = 0 or y = 2)

and periodic Boundary Conditions:
    u @ x = 0 == u @ x = 2
    v @ x = 0 == v @ x = 2
    p @ x = 0 == p @ x = 2

'''

x = 64
y = 64
x_interval = 0.002 
y_interval = 0.002
dx = x_interval/(x-1) 
dy = y_interval/(y-1)
dx2 = dx**2
dy2 = dy**2 

# air
# rho = 1.225
# vis = 1.6*1e-5

# water at 20 degree
rho = 1000.0
vis = 1 * 1e-3
F = 1

# ketchup at 30 degree 
# rho = 1500
# vis = 0.1

t_step = 512 * 16
dt = 1 * vis * dx

u = np.zeros([x,y])
v = np.zeros([x,y])
p = np.ones([x,y])

u_next = u.copy()
v_next = v.copy()

X = np.linspace(0, x_interval, x)
Y = np.linspace(0, y_interval, y)
X_grid,Y_grid = np.meshgrid(X, Y)
X_grid = np.transpose(X_grid)
Y_grid = np.transpose(Y_grid)
step = 2

def myPlot(u, v, p, X_grid, Y_grid):
    
    plt.cla()
    
    plt.contourf(X_grid,Y_grid,p)
    # plt.colorbar()
    plt.quiver(X_grid[::step,::step], Y_grid[::step,::step] , u[::step,::step] , v[::step,::step] )
    
    plt.pause(dt)
    # plt.show()
    
def get_p(p, rho, dx, dt ,u ,v ):
    e = 1e-4
    p_tmp = np.empty_like(p)

    flag = True
    while flag:

        D = ( u[2: , 1:-1] - u[:-2,1:-1] + v[1:-1 ,2:] - v[1:-1, :-2]) / (2*dx*dt) - ((u[2:,1:-1] - u[:-2 , 1:-1]) / (2*dx))**2 - ((v[1:-1, 2:] - v[1:-1,:-2]) / (2*dx))**2 - (u[1:-1 , 2:] - u[1:-1,:-2])  * ( v[2: , 1:-1] - v[:-2 , 1:-1]) / (2*dx2)
        p_tmp[ 1:-1 , 1:-1 ] = ( (p[2: ,1:-1] + p[:-2 , 1:-1] + p[1:-1 , 2:] + p[1:-1 , :-2]) ) / 4 - rho * dx2 / 4 * D

        # boundary condition
        D0 = ( u[1, 1:-1] - u[-2,1:-1] + v[0 ,2:] - v[0, :-2]) / (2*dx*dt) - ((u[1,1:-1] - u[-2 , 1:-1]) / (2*dx))**2 - ((v[0, 2:] - v[0,:-2]) / (2*dx))**2 - (u[0 , 2:] - u[0,:-2])  * ( v[1 , 1:-1] - v[-2 , 1:-1]) / (2*dx2)
        p_tmp[0, 1:-1] = ( (p[1, 1:-1] + p[-2, 1:-1] + p[0, 2:] + p[0 , :-2]) ) / 4 - rho * dx2 / 4 * D0
        p_tmp[-1, :] = p_tmp[0, :]

        p_tmp[:, -1] = p_tmp[:,-2]
        p_tmp[:, 0] = p_tmp[:,1]

        p = p_tmp.copy()

        flag = np.sum(np.abs(p_tmp - p)) > e * np.sum(np.abs(p))

    return p_tmp

plt.ion()
# myPlot(u, v, p, X_grid, Y_grid) 

for i in range(t_step) :

    p = get_p(p,rho,dx,dt,u,v)

    u_next[1:-1, 1:-1] = u[1:-1, 1:-1] \
        - dt / dx * u[1:-1, 1:-1] * (u[1:-1, 1:-1] - u[0:-2, 1:-1]) \
        - dt / dy * v[1:-1, 1:-1] * (u[1:-1, 1:-1] - u[1:-1, 0:-2]) \
        + vis * dt / dx2 * (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[0:-2, 1:-1]) \
        + vis * dt / dy2 * (u[1:-1,2:] - 2 * u[1:-1, 1:-1] + u[1:-1, 0:-2]) \
        - dt * (p[2:,1:-1] - p[:-2,1:-1]) / (2*rho*dx) \
        + F * dt

    v_next[1:-1, 1:-1] = v[1:-1, 1:-1] \
        - dt / dx * u[1:-1, 1:-1] * (v[1:-1, 1:-1] - v[0:-2, 1:-1]) \
        - dt / dy * v[1:-1, 1:-1] * (v[1:-1, 1:-1] - v[1:-1, 0:-2]) \
        + vis * dt / dx2 * (v[2:, 1:-1] - 2 * v[1:-1, 1:-1] + v[0:-2, 1:-1]) \
        + vis * dt / dy2 * (v[1:-1, 2:] - 2 * v[1:-1, 1:-1] + v[1:-1, 0:-2]) \
        - dt * (p[1:-1,2:] - p[1:-1,:-2]) / (2*rho*dy)

    u_next[ 0, 1:-1] = u[0,1:-1] \
        + vis * dt * ( (u[1,1:-1] - 2*u[0,1:-1] + u[-2,1:-1])/dx2 + (u[0,2:] - 2*u[0,1:-1]+u[0,:-2])/dy2 ) \
        - dt * (u[0,1:-1]*(u[0,1:-1] - u[-2,1:-1])/dx + v[0,1:-1] * (u[0,1:-1] - u[0,:-2]) / dy) \
        - dt * (p[1,1:-1] - p[-2,1:-1]) / (2 * rho * dx) \
        + F * dt
    
    u_next[-1, :] = u_next[0, :]
    
    v_next[ 0, 1:-1] = v[0,1:-1] \
        + vis * dt * ( (v[1,1:-1] - 2*v[0,1:-1] + v[-2,1:-1])/dx2 + (v[0,2:] - 2*v[0,1:-1]+v[0,:-2])/dy2 ) \
        - dt * (v[0,1:-1]*(v[0,1:-1] - v[-2,1:-1])/dx + u[0,1:-1] * (v[0,1:-1] - v[0,:-2]) / dy) \
        - dt * (p[0, 2:] - p[0,:-2]) / (2 * rho * dy)
    
    v_next[-1, :] = v_next[0, :]

    u_next[:, 0] = 0 
    u_next[:,-1] = 0
    v_next[:, 0] = 0
    v_next[:,-1] = 0 

    u = u_next.copy()
    v = v_next.copy()

    # myPlot(u, v, p, X_grid, Y_grid)
    
    
plt.ioff()

fig = plt.figure(figsize = (11,7), dpi=100)
plt.contourf(X_grid,Y_grid,p, alpha = 0.5, cmap = cm.viridis)
plt.colorbar()
plt.quiver(X_grid[::step,::step], Y_grid[::step,::step] , u[::step,::step] , v[::step,::step] )
plt.show()