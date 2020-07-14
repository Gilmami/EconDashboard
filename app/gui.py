# Got a layout that makes sense. will need to do some tweaking, but better than nothing.
# Next to figure out how to make sliders interact with params. I'll try just putting something
# like, slider.get in for each argument of param in the graph, see what happens tomorrow.

import os
import sys
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
sys.path.append(os.getcwd() + "/server")
import models

subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

root = Tk()
frame = Frame(root)
root.title("Model Calibration")

# set up sliders for all the parameter values of the solow model.
k0_slide = Scale(master = root, from_= 1000, to = 0, label = "K0".translate(subscript))
k0_slide.set(1)
k0_slide.grid(column=0, row=1)

l0_slide = Scale(master = root, from_= 1000, to = 0, label = "L0".translate(subscript))
l0_slide.set(1)
l0_slide.grid(column=1, row=1)

alpha_slide = Scale(master = root, from_= 1, to = 0, resolution = .01, label = "a")
alpha_slide.set(.7)
alpha_slide.grid(column=3, row=1)

delta_slide = Scale(master = root, from_= 1, to = 0, resolution = .01, label = "d")
delta_slide.set(.05)
delta_slide.grid(column=4, row=1)

g_slide = Scale(master = root, from_= 1, to = 0, resolution = .01, label = "g")
g_slide.set(.03)
g_slide.grid(column=5, row=1)

n_slide = Scale(master = root, from_= 1, to = 0, resolution = .01, label = "n")
n_slide.set(.02)
n_slide.grid(column=6, row=1)

s_slide = Scale(master = root, from_= 1, to = 0, resolution = .01, label = "s")
s_slide.set(.1)
s_slide.grid(column=7, row=1)

# initialize and create the graph for the solow model with parameter values set by sliders
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(1, 1, 1)

canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=0, columnspan=8)

kprime = np.diff(models.solow().k0)

ax.plot(models.solow().k0, models.solow().k1, color="#C41E3A")

root.mainloop()

