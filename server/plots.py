import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.getcwd() + "/server")

from models import solow

points = solow()

difflist = list()
for i in range(0, len(points.k0)):
    diff = points.k0[i] - points.k1[i]
    difflist.append(diff)

fig = plt.figure(0)
fig = plt.plot(points.t, points.k1)
fig = plt.plot()

plt.show()
