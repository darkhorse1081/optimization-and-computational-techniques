# Examples of using the np.dot command

# imports
import numpy as np

# set sample arrays
a = np.array([[1, 2, 3, 4]])
b = np.array([[1, 1, 1, 1]]).T
c = np.array([[1, 0, 1, 0], [1, 1, 0, 0]])
d = np.array([[-1, 1], [1, -1]])

# display array order/shape/dimension information
print(a.shape, b.shape, c.shape, d.shape)

# perform various commands with np.dot
print(np.dot(a, b))
print(np.dot(b, a))
print(np.dot(a, c))
print(np.dot(a, c.T))
print(np.dot(d, c))
print(np.dot(c, d))
print(np.dot(c.T, d))
