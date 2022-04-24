#coding:utf-8

from matplotlib import pyplot as plt
import numpy as np

# Z = [
#         [1,2,3],
#         [2,3,4],
#         [3,4,5],
#         [4,5,6]
#     ]
# Z = np.array(Z)
# z[x][y] , x ~ [0,2], y ~ [0,3]
# X = np.linspace(0,2,3) # [0,1,2]
# Y = np.linspace(0,3,4) # [0,1,2,3]
# XX, YY = np.meshgrid(X,Y)

x = np.linspace(-5,5,101)
y = np.arange(-5,5.1,0.1)
XX , YY = np.meshgrid(x,y) 
Z = 1 - XX**2 - YY**2 

ax3 = plt.axes(projection='3d')
ax3.scatter3D(XX, YY, Z, cmap='viridis')

plt.show()
