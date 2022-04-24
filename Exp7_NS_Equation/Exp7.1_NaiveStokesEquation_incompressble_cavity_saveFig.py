#coding:utf-8

import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import cm

'''

Navie Stokes Euation with incompressble fluid:

--------------------------

    du/dt + udu/dt + vdu/dy = -1/rho * dp/dx + viscosity * laplacian u
    dv/dt + udv/dt + vdv/dy = -1/rho * dp/dx + viscosity * laplacian v
    ddp/ddx + ddp/ddy = -rho * ( (du/dx)**2 + 2* du/dy * dv/dx + (dv/dy)**2 )
    
With Initial Conditions:

    u = 0

    v = 0

    p = 0

With Boundary Conditions:

    u = 1 at y == 2
    u = 0 at other boundary

    v = 0 at boundary

    dp / dx = 0 at (x = 0 or x = 2)

    { dp / dy = 0 at (y = 0 or y = 2) }
    or
    {       p = 0 at (y = 0 or y = 2) }

'''
x = 256
y = 256
x_interval = 0.002 
y_interval = 0.002
dx = x_interval/(x-1) 
dy = y_interval/(y-1)
dx2 = dx**2
dy2 = dy**2 

t_step = 4000
dt = 0.001 * dx

step = 4

# air
# rho = 1.225
# vis = 1.6*1e-5

# water at 20 degree
rho = 1000.0
vis = 1 * 1e-3

# ketchup at 30 degree 
# rho = 1500
# vis = 0.1

p = np.zeros([x,y])
u = np.zeros([x,y])
v = np.zeros([x,y])

u[:,-1] = 1
# u[:,0] = 1
# v[0,:] = -1
# v[0, :] = -1

u_next = u.copy()
v_next = v.copy()
p_next = p.copy()

X = np.linspace(0, x_interval, x)
Y = np.linspace(0, y_interval, y)
X_grid,Y_grid = np.meshgrid(X, Y)
X_grid = np.transpose(X_grid)
Y_grid = np.transpose(Y_grid)

def myPlot(u, v, p, X_grid, Y_grid):
    
    plt.contourf(X_grid,Y_grid,p)
    # plt.colorbar()
    plt.quiver(X_grid[::step,::step], Y_grid[::step,::step] , u[::step,::step] , v[::step,::step] )
    
def get_p(p, rho, dx, dt ,u ,v ):
    e = 1e-5
    p_tmp = p.copy()
    p_tmp[:,-1] = 0 # p = 0 at y = upperbound
    # p_tmp[:,0] = 0 # p = 0 at y = lowerbound

    flag = True
    while flag:

        D = ( u[2: , 1:-1] - u[:-2,1:-1] + v[1:-1 ,2:] - v[1:-1, :-2]) / (2*dx*dt) - ((u[2:,1:-1] - u[:-2 , 1:-1]) / (2*dx))**2 - ((v[1:-1, 2:] - v[1:-1,:-2]) / (2*dx))**2 - (u[1:-1 , 2:] - u[1:-1,:-2])  * ( v[2: , 1:-1] - v[:-2 , 1:-1]) / (2*dx2)
        
        p_tmp[ 1:-1 , 1:-1 ] = ( (p[2: ,1:-1] + p[:-2 , 1:-1] + p[1:-1 , 2:] + p[1:-1 , :-2]) ) / 4 - rho * dx2 / 4 * D
        
        # p_tmp[:, -1] = p_tmp[:,-2] # dp/dy = 0 at y = upperbound
        p_tmp[:, 0] = p_tmp[:,1] # dp/dy = 0 at y = lowerbound
        p_tmp[-1,:] = p_tmp[-2,:] # dp/dx = 0 at x = upperbound
        p_tmp[0, :] = p_tmp[1,:] # dp/dx = 0 at x = lowerbound
        
        flag = np.sum(np.abs(p_tmp - p)) > e * np.sum(np.abs(p))
        p = p_tmp.copy()

    return p_tmp

myPlot(u, v, p, X_grid, Y_grid) 
plt.savefig("start.png")

for i in range(t_step) :

    if i % 100 == 0:
        print(i)
    
    u_next[1:-1, 1:-1] = u[1:-1, 1:-1] \
        - dt / dx * u[1:-1, 1:-1] * (u[1:-1, 1:-1] - u[0:-2, 1:-1]) \
        - dt / dy * v[1:-1, 1:-1] * (u[1:-1, 1:-1] - u[1:-1, 0:-2]) \
        + vis * dt / dx2 * (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[0:-2, 1:-1]) \
        + vis * dt / dy2 * (u[1:-1,2:] - 2 * u[1:-1, 1:-1] + u[1:-1, 0:-2]) \
        - dt * (p[2:,1:-1] - p[:-2,1:-1]) / (2*rho*dx)

    v_next[1:-1, 1:-1] = v[1:-1, 1:-1] \
        - dt / dx * u[1:-1, 1:-1] * (v[1:-1, 1:-1] - v[0:-2, 1:-1]) \
        - dt / dy * v[1:-1, 1:-1] * (v[1:-1, 1:-1] - v[1:-1, 0:-2]) \
        + vis * dt / dx2 * (v[2:, 1:-1] - 2 * v[1:-1, 1:-1] + v[0:-2, 1:-1]) \
        + vis * dt / dy2 * (v[1:-1, 2:] - 2 * v[1:-1, 1:-1] + v[1:-1, 0:-2]) \
        - dt * (p[1:-1,2:] - p[1:-1,:-2]) / (2*rho*dy)

    p_next = get_p(p, rho, dx, dt ,u ,v )

    u = u_next.copy()

    v = v_next.copy()

    p = p_next.copy()

    # myPlot(u, v, p, X_grid, Y_grid)

plt.contourf(X_grid,Y_grid,p, alpha = 0.5, cmap = cm.viridis)
plt.colorbar()
plt.quiver(X_grid[::step,::step], Y_grid[::step,::step] , u[::step,::step] , v[::step,::step] )
plt.savefig("end.png")