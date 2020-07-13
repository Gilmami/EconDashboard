import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.getcwd() + "/server")

from models import solow

points = solow()

line = list()
for i in range(0, len(points.k0)):
    line.append(i)
fig = plt.figure(0)
fig = plt.plot(points.k0, line)
plt.show()
