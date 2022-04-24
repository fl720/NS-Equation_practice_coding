#coding:utf-8
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
from matplotlib  import pyplot as plt 
plt.ion()

# du/dt + c_x * du/dx + c_y * du/dy = 0

c_x = 1
c_y = 1

x_cells =  256
y_cells =  256

interval = 3.0
dx = interval/(x_cells -1)
dy = interval/(y_cells -1)
x = np.linspace(- interval/2, interval/2,x_cells)
y = np.linspace(- interval/2 ,interval/2,y_cells)

step = 8
dt = 0.5 * dx

# 3D - tensor
u = np.ones( [step, x_cells, y_cells])

for i in range( int((x_cells-1)/ interval ) , int((x_cells-1) * 2 / interval ) )  :
    for j in range( int((y_cells-1)/ interval ) , int((y_cells-1) * 2 / interval ) )  :
        u[0][i][j] = 2
        
xx , yy = np.meshgrid( x ,y )
xx = np.transpose(xx)
yy = np.transpose(yy)

print(xx.shape)
print(yy.shape)
print(u[0].shape)

for k in range(step - 1) :
    for i in range( 1, x_cells ) :
        for j in range( 1, y_cells ) :
            u[k+1][i][j] = u[k][i][j] - c_x * dt/dx * ( u[k][i][j] - u[k][i-1][j] ) - c_y * dt/dy * ( u[k][i][j] - u[k][i][j-1] )

    plt.cla()
    ax = plt.axes(projection = '3d')
    ax.plot_surface(xx,yy,u[k], cmap='viridis')
    plt.pause(1./1024)

    # print(u[k])
    
plt.ioff()
plt.show()
    
            




