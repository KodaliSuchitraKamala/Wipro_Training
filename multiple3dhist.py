import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(42)
data1 = np.random.randint(1, 100, 50)
data2 = np.random.randint(1, 100, 50)
data3 = np.random.randint(1, 100, 50)
bins = 10
count1, bin_edges = np.histogram(data1, bins = bins, range = (0, 100))
count2, _ = np.histogram(data2, bins = bins, range = (0, 100))
count3, _ = np.histogram(data3, bins = bins, range = (0, 100))
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111, projection = '3d')
dx = dy = (bin_edges[1] - bin_edges[0]) * 0.8
x1 = bin_centers - dx
x2 = bin_centers
x3 = bin_centers - dx
y1 = np.zeros_like(x1)
y2 = np.zeros_like(x2) * 1.5
y3 = np. zeros_like(x3) * 3
ax.bar3d(x1, y1, np.zeros_like(count1), dx, dy, count1, color = '#FF0000', alpha = 0.8, label = 'Dataset 1')
ax.bar3d(x2, y2, np.zeros_like(count2), dx, dy, count2, color = '#00FF00', alpha = 0.8, label = 'Dataset 2')
ax.bar3d(x3, y3, np.zeros_like(count3), dx, dy, count3, color = '#0000FF', alpha = 0.8, label = 'Dataset 3')
ax.set_xlabel('Values')
ax.set_ylabel('Freqenecy')
ax.set_title('Multiple Histograms overalapping')
ax.set_yticks([0, 1.5, 3])
ax.set_yticklabels(['Dataset 1', 'Dataset 2', 'Dataset 3'])
plt.legend()
plt.show()