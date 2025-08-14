import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
rng = np.random.default_rng(42)
n_per_cluster = [450, 400, 350, 300]
means = np.array([[0, 0, 0], [6.5, 6.5, 5.5],
                  [-6, 6.5, -6]])
covs = [
    np.array([[1.2, 0.2, 0.0],
              [0.2, 1.0, 0.1],
              [0.0, 0.1, 0.8]]),
    np.array([[1.5, 0.3, 0.1], 
              [0.3, 1.8, 0.2],
              [0.1, 0.2, 1.0]]),
    np.array([[0.9, -0.2, 0.],
              [-0.2, 1.3, 0.1],
              [0.0, 0.1, 1.1]]),
    np.array([[1.1, 0.0, -0.1],
              [0.0, 1.0, 0.0],
              [-0.1, 0.0, 1.4]])
]
clusters = [rng.multivariate_normal(m, c, size = n) for n, m, c in zip(n_per_cluster, means, covs)]
x = np.vstack(clusters)
x = x[rng.permutation(len(x))]
k = 4
kmeans = KMeans(n_clusters = k, n_init = 10, random_state = 42)
labels = kmeans.fit_predict(x)
sil = silhouette_score(x, labels)
print(f"silhoutte score: {sil:.3f}")
sizes = pd.Series(labels).value_counts().sort_index()
summary_df = pd.DataFrame({'cluster_id': sizes.index, 'n_points': sizes.values})
summary_df['fraction'] = (summary_df['n_points'] / len(x)).round()
summary_df['centroid_x'] = np.round(kmeans.cluster_centers_[:, 0], 3)
summary_df['centroid_y'] = np.round(kmeans.cluster_centers_[:, 1], 3)
summary_df['centroid_z'] = np.round(kmeans.cluster_centers_[:, 2], 3)
print("\n Cluster Summary: ", summary_df)
fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x[:, 0], x[:, 1], x[:, 2], c = labels, s = 10)
ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 2], marker = '*', s = 200, edgecolor = 'black')
plt.tight_layout()
plt.show()