import numpy as np

x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print(np.where(x > 6))

y = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
print(np.where(y >= 0.5, 1, 0))

print(np.where(x > 2, 1, 0))