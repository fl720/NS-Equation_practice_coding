#coding:utf-8
import numpy as np
from matplotlib import pyplot
import sympy 
from sympy.utilities import lambdify
pyplot.ion()# interactive on

# du/dt + u * du/dx = nu * ddu/ddx
# with u0 = -2 * nu/phi * dphi/dx 
# phi = exp(-x^2/(4*nu)) + exp(-(x-2pi)^2/(4*nu))

n = 128
interval = 2 * np.pi
dx = interval / (n-1)

x_axis = np.linspace(0 , interval , n)

KiVis = 0.0625

nt = 512
dt = dx * KiVis

u = np.zeros( [ nt + 1 , n] )

x = sympy.Symbol('x') 
phi = sympy.exp(-x**2/(4*KiVis)) + sympy.exp(-(x-2*np.pi)**2/(4*KiVis)) 
phi_dx = phi.diff(x)
u0 = -2 * KiVis/phi * phi_dx + 4
u0_func = lambdify((x), u0)

u[0] = [u0_func(it) for it in x_axis]
pyplot.plot(x_axis , u[0] )

for j in range( nt ) :
    if j%100 == 0:
        print(j)
    for i in range( 1 , n - 1 ) :
        u[j+1][i] = u[j][i] - u[j][i] * dt / dx *(u[j][i] - u[j][i-1]) + KiVis * dt / dx**2 *\
             (u[j][i+1] - 2 * u[j][i] + u[j][i-1])

        # Boundary Condition
        u[j+1][0] = u[j][-1] - u[j][-1] * dt / dx * (u[j][-1] - u[j][-2]) + KiVis * dt / dx**2 *\
                    (u[j][1] - 2 * u[j][-1] + u[j][-2])
        u[j+1][-1] = u[j+1][0]
        

    pyplot.cla()
    pyplot.plot(x_axis , u[j])
    pyplot.pause(dt * 0.1)

print('done.')

pyplot.ioff()
pyplot.show()