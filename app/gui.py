# So far this has all the elements I need/want, now I need to get them in a layout that makes sense
# and get the sliders to interact with the figures. We're on our way!
import os
import sys
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
sys.path.append(os.getcwd() + "/server")
import models

subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

window = Tk()
window.title("Model Calibration")

# set up sliders for all the parameter values of the solow model.
# k0_slide = Scale(master = window, from_= 1000, to = 0, label = "K0".translate(subscript))
# k0_slide.set(1)
# k0_slide.pack()
#
# l0_slide = Scale(master = window, from_= 1000, to = 0, label = "L0".translate(subscript))
# l0_slide.set(1)
# l0_slide.pack()
#
# alpha_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "a")
# alpha_slide.set(.7)
# alpha_slide.pack()
#
# delta_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "d")
# delta_slide.set(.05)
# delta_slide.pack()
#
# g_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "g")
# g_slide.set(.03)
# g_slide.pack()
#
# n_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "n")
# n_slide.set(.02)
# n_slide.pack()
#
# s_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "s")
# s_slide.set(.1)
# s_slide.pack()

# initialize and create the graph for the solow model with parameter values set by sliders
figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(1, 1, 1)

canvas = FigureCanvasTkAgg(figure, window)
canvas.get_tk_widget().grid(row=0, column=0)

kprime = np.diff(models.solow().k0)

ax.plot(models.solow().k0, models.solow().k1, color="#C41E3A")

window.mainloop()

