"""
A simple example of an animated plot
"""
# pylint: skip-file

import matplotlib
matplotlib.use('Agg')
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
cset = ax.contour(X, Y, Z)
ax.clabel(cset, fontsize=9, inline=1)

fig.savefig('temp.png')