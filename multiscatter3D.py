import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(42)
x1 = np.random.rand(50) * 100
y1 = np.random.rand(50) * 100
z1 = np.random.rand(50) * 100
sizes1 = np.random.randint(50, 500, 50)
colors1 = np.random.randint(0, 100, 50)
x2 = np.random.rand(50) * 100
y2 = np.random.rand(50) * 100
z2 = np.random.rand(50) * 100
sizes2 = np.random.randint(50, 500, 50)
colors2 = np.random.randint(0, 100, 50)
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111, projection = '3d')
scatter1 = ax.scatter(x1, y1, z1, c = colors1, s = sizes1, cmap = 'viridis',
                      edgecolors = '#000000', alpha = 0.7, marker = 'o', label = 'Dataset 1')
scatter2 = ax.scatter(x2, y2, z2, c = colors2, s = sizes2, cmap = 'plasma',
                      edgecolors = '#000000', alpha = 0.8, marker = '^', label = 'Dataset 2')
cbar1 = fig.colorbar(scatter1, ax = ax, shrink = 0.5, pad = 0.1)
cbar1.set_label("Viridis")
cbar2 = fig.colorbar(scatter2, ax = ax, shrink = 0.5, pad = 0.09)
cbar2.set_label("plasma")
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
plt.title("3-D Random Scatter Plot with 2 Datasets")
plt.grid()
plt.show()