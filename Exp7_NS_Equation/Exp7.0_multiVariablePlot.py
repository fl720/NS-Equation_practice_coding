#coding:utf-8

from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
from numpy.core.function_base import linspace

cell = 128

x    = linspace(0, 2, cell)
y    = linspace(0, 2, cell)
X, Y = np.meshgrid(x,y)

P = X + Y ** 2
Vx = X
Vy = 2*Y

plt.contourf(X,Y,P, cmap = 'viridis')
plt.colorbar()

step = 30
plt.quiver(X[::step], Y[::step], Vx[::step], Vy[::step])

plt.xlabel('X')
plt.ylabel('Y')

plt.show()

