import numpy as np

x = np.array([
    [51, 55],
    [14, 19],
    [0, 4]
])

print(x)
print(x[0])
print(x[0, 1])

X = x.flatten()
print(X)
print(X[np.array([0, 2, 4])])

print(X>5)