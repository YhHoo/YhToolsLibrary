# This code create a scatter plot for function of z = f(x,y)
import matplotlib.pyplot as plt
import numpy as np


# function want to plot (change this)
def f_1_score(x, y):
    return (2 * x * y) / (x + y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# create 2D independent variable xy plane
x = y = np.arange(0.01, 0.99, 0.01)  # x, y from 0.01-0.99 (change this)
X, Y = np.meshgrid(x, y)
zs = np.array([f_1_score(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_zlabel('F 1 SCORE')

plt.show()
