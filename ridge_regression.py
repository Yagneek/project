from sklearn.datasets import make_regression
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

r_d, profit, coefficients = make_regression(
    n_samples=50,
    n_features=1,
    n_informative=1,
    n_targets=1,
    noise=5,
    coef=True,
    random_state=1
)

alpha = 0
n, m = r_d.shape
I = np.identity(m)

w = np.dot(np.dot(np.linalg.inv(np.dot(r_d.T, r_d) + alpha * I), r_d.T), profit)

plt.scatter(r_d, profit)
plt.plot(r_d, w*r_d, c='red')
plt.show()







