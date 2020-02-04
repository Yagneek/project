from sklearn.datasets import make_regression
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

X, y, coefficients = make_regression(
    n_samples=50,
    n_features=1,
    n_informative=1,
    n_targets=1,
    noise=5,
    coef=True,
    random_state=1
)

alpha = 0
n, m = X.shape
I = np.identity(m)

w = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X) + alpha * I), X.T), y)
ols_w = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)

plt.scatter(X, y)
plt.plot(X, w*X, c='red')
plt.show()



