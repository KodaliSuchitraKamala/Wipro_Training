import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(20)
x = np.random.rand(50) * 100
y = np.random.rand(50) * 100
z = np.random.rand(50) * 100
sizes = np.random.randint(50, 500, 50)
fig = plt.figure()
colors = np.random.randint(0, 100, 50)
ax = fig.add_subplot(111, projection = '3d')
scatter = ax.scatter(x, y, z, c=colors, s = sizes, cmap = 'hot', edgecolors = '#000000', alpha = 0.7)
fig.colorbar(scatter,ax= ax, label = 'Color Scale')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
plt.title("3-D Random Scatter Plot")
plt.grid()
plt.show()