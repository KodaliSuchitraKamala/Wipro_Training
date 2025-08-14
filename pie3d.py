import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Wedge
from matplotlib.collections import PatchCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
labels = ['C', 'C++', 'JAVA', 'Python', 'Data Science']
prizes = [400, 450, 1100, 700, 1350]
colors = ['blue', 'grey', 'brown', 'magenta', 'green']
total = sum(prizes)
fracs = [p / total for p in prizes]
angles = [frac * 360 for frac in fracs]
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
radius = 1
height = 0.3
start_angle = 0
for i, angle in enumerate(angles):
    theta = np.linspace(np.deg2rad(start_angle), np.deg2rad(start_angle + angle), 30)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    verts_top = [(x[j], y[j], height) for j in range(len(x))]
    verts_bottom = [(x[j], y[j], 0) for j in range(len(x))]
    side_verts = []
    for j in range(len(x) - 1):
        side_verts.append([(x[j], y[j], 0), (x[j+1], y[j+1], 0), (x[j+1], y[j+1], height), (x[j], y[j], height)])
    top_face_with_center = [(0, 0, height)] + verts_top
    bottom_face_with_center = [(0, 0, 0)] + verts_bottom
    all_verts = side_verts + [top_face_with_center, bottom_face_with_center]
    ax.add_collection3d(Poly3DCollection(all_verts, facecolors=colors[i], alpha=0.8, edgecolor='black'))
    mid_angle = np.deg2rad(start_angle + angle / 2)
    ax.text(radius * 0.7 * np.cos(mid_angle), radius * 0.7 * np.sin(mid_angle), height + 0.05,
            f"{labels[i]}: Rs.{prizes[i]}", ha='center', va='bottom', fontsize=10,
            color='black')
    start_angle += angle
ax.set_box_aspect([1, 1, 0.5])
ax.axis('off')
plt.title("3D Pie Chart")
plt.show()