#coding:utf-8
import numpy as np
from matplotlib import pyplot
# pyplot.ion()

# du/dt = v * ddu/ddx

n = 128
interval = 3.0
dx = interval / (n-1)

x_axis = np.linspace(0 , 3 , n)

nt = 1024
dt = 1./4096

KinematicViscousity = 1

initialPosi = np.zeros( [ nt + 1 , n] )
initialUpper = 2 
initialLower = 1 

for i in range( int( 1/dx * initialLower), int( 1/dx * initialUpper) + 1 ) :
    initialPosi[0][i] = 1 

# pyplot.plot(x_axis , initialPosi[0] )

for j in range( nt ) :
    if j%100 == 0:
        print(j)
    for i in range( 1 , n - 1 ) :
        initialPosi[j+1][i] = initialPosi[j][i] + KinematicViscousity * dt/dx**2 * (initialPosi[j][i+1] - 2 * initialPosi[j][i] + initialPosi[j][i-1])
    # initialPosi[j+1][0] = initialPosi[j][0] + KinematicViscousity * dt/dx**2 * (initialPosi[j][2] - 2 * initialPosi[j][1] + initialPosi[j][0])
    # initialPosi[j+1][n - 1] = initialPosi[j][n - 1] + KinematicViscousity * dt/dx**2 * (initialPosi[j][n - 1] - 2 * initialPosi[j][n - 2] + initialPosi[j][n - 3])

    # pyplot.cla()
    # pyplot.ylim((0,1))
    # pyplot.plot(x_axis , initialPosi[j])
    # pyplot.pause(dt/10000)

# pyplot.ioff()
pyplot.ylim((0,1))
pyplot.plot(x_axis , initialPosi[nt] )
pyplot.show()

