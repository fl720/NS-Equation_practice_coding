# coding:utf-8
# du/dt + c * du/dx = 0

import numpy as np
from matplotlib import pyplot 

pyplot.ion() # interactive mode on

n = 81 # cell number
interval = 2.0 
dx = interval / (n - 1)

nt = 64
dt = 0.0125 # dt is the amount of time each timestep covers (delta t)

c  = 1 # assume wavespeed of c = 1

# set u0

u = np.zeros( [nt + 1, n] )
# Initial Condition 1
for i in range(0, int(n/2)):
    u[0][i] = i * dx  
for i in range( (int(n/2)) , n ):
    u[0][i] = 2 - i * dx
# Initial Condition 2
# u[0][ int((n-1)/4) : int(3*(n-1)/4)] = 1

# pyplot.plot( np.linspace(0,interval,n), u[0] ) # draw line
pyplot.scatter( np.linspace(0,interval,n), u[0] ) # draw scatter chart

for k in range(1, nt + 1):
    for j in range( 1 , n ):
        u[k][j] = u[k-1][j] - u[k-1][j] * dt/dx *(u[k-1][ j ] - u[k-1][ j - 1 ] )
    # for j in range( n - 1 ):
    #     u[k][j] = u[k-1][j] - c * dt *(u[k-1][ j+1 ] - u[k-1][ j] ) / dx
    print(u[k])

    # pyplot.cla() # clear axis
    pyplot.clf() # clear figure
    pyplot.plot( np.linspace(0,interval,n), u[k] )
    pyplot.pause(dt)
    # pyplot.scatter( np.linspace(0,interval,n), u[k] )

pyplot.ioff() # interactive mode on
pyplot.show() # show image 

print(1)
