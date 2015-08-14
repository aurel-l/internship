import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs, ys, zs = zip(
  *[
    (x, y, z)
    for x in np.arange(0, 1, 0.1)
    for y in np.arange(3, 4.6, 0.2)
    for z in np.arange(0, 0.3, 0.05)
  ]
)

ax.scatter(xs, ys, zs, c='b', marker='.')

ax.set_xlabel('migrationProb')
ax.set_ylabel('poissonMean')
ax.set_zlabel('marriageModifier')

plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 5000
xs = np.random.uniform(0, 1, n)
ys = np.random.uniform(3, 4.6, n)
zs = np.random.uniform(0, 0.3, n)

ax.scatter(xs, ys, zs, c='b', marker='.')

ax.set_xlabel('migrationProb')
ax.set_ylabel('poissonMean')
ax.set_zlabel('marriageModifier')

plt.show()

