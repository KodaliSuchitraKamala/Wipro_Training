from sklearn.linear_model import ElasticNet, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(42)
x, y = make_regression(n_samples=100, n_features=10, n_informative=5, noise=15, random_state=42)
x = x - np.mean(x, axis=0)
y = y - np.mean(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
elastic_net = ElasticNet(alpha=1.0, l1_ratio=0.5, random_state=42)
ridge = Ridge(alpha=1.0, random_state=42)
lasso = Lasso(alpha=0.1, random_state=42)
elastic_net.fit(x_train, y_train)
ridge.fit(x_train, y_train)
lasso.fit(x_train, y_train)
y_pred_en = elastic_net.predict(x_test)
y_pred_ridge = ridge.predict(x_test)
y_pred_lasso = lasso.predict(x_test)
print("ElasticNet Coefficients:", elastic_net.coef_)
print("ElasticNet MSE:", mean_squared_error(y_test, y_pred_en))
print("\nRidge Coefficients:", ridge.coef_)
print("Ridge MSE:", mean_squared_error(y_test, y_pred_ridge))
print("\nLasso Coefficients:", lasso.coef_)
print("Lasso MSE:", mean_squared_error(y_test, y_pred_lasso))
x1_test = x_test[:, 0]
x2_test = x_test[:, 1]
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1_test, x2_test, y_test, color='#0000FF', label='Actual', alpha=0.6)
ax.scatter(x1_test, x2_test, y_pred_en, color='#FF0000', label='ElasticNet Pred', alpha=0.6)
ax.scatter(x1_test, x2_test, y_pred_ridge, color='#00AA00', label='Ridge Pred', alpha=0.6)
ax.scatter(x1_test, x2_test, y_pred_lasso, color='#AA00AA', label='Lasso Pred', alpha=0.6)
x1_range = np.linspace(x1_test.min(), x1_test.max(), 20)
x2_range = np.linspace(x2_test.min(), x2_test.max(), 20)
x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)
x_grid = np.zeros((x1_grid.size, x.shape[1]))
x_grid[:, 0] = x1_grid.ravel()
x_grid[:, 1] = x2_grid.ravel()
for i in range(2, x.shape[1]):
    x_grid[:, i] = np.mean(x_test[:, i])
y_grid = elastic_net.predict(x_grid)
y_grid = y_grid.reshape(x1_grid.shape)
ax.plot_surface(x1_grid, x2_grid, y_grid, color='#00FF00', alpha=0.3, rstride=1, cstride=1)
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_title("ElasticNet, Ridge, and Lasso Comparison")
ax.legend()
plt.show()
