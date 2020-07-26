# now to get into proper formulation of the model to actually get the correct graph.

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

def update(val):
    updmodel = models.solow(k_0=k0_slide.get(), l_0=l0_slide.get(), a_0=a0_slide.get(),
                            alpha=alpha_slide.get(), d=delta_slide.get(), g=g_slide.get(),
                            n=n_slide.get(), s=s_slide.get())
    kseq = list()
    for i in range(0, len(updmodel.k0)):
        k = updmodel.k0[i]/updmodel.l[i]
        kseq.append(k)

    yseq = list()
    for i in range(0, len(updmodel.k0)):
        y = updmodel.y[i]/updmodel.l[i]
        yseq.append(y)

    dep_line = list()
    for i in range(0, len(updmodel.k0)):
        dep_k0 = (n_slide.get() + delta_slide.get()) * i
        dep_line.append(dep_k0)


    axes.cla()
    axes.plot(updmodel.t, yseq, color="r")
    axes.plot(updmodel.t, dep_line, color="b")
    axes.set_title("Graph of Model")
    axes.set_ylabel("Output")
    axes.set_xlabel("Capital")
    # axes.set_xlim([1, 20])
    # axes.set_ylim([1, 100])
    canvas.draw_idle()

# set up sliders for all the parameter values of the solow model.


k0_slide = Scale(master=root, from_=1000, to=1, label="K0".translate(subscript), command=update)
k0_slide.set(1)
k0_slide.grid(column=0, row=1)

l0_slide = Scale(master=root, from_=1000, to=1, label="L0".translate(subscript), command=update)
l0_slide.set(1)
l0_slide.grid(column=1, row=1)

a0_slide = Scale(master=root, from_=1, to=.001, resolution=.001, label="a", command=update)
a0_slide.set(.7)
a0_slide.grid(column=3, row=1)

alpha_slide = Scale(master=root, from_=1, to=0, resolution=.001, label="alpha", command=update)
alpha_slide.set(.7)
alpha_slide.grid(column=4, row=1)

delta_slide = Scale(master=root, from_=1, to=0, resolution=.001, label="d", command=update)
delta_slide.set(.05)
delta_slide.grid(column=5, row=1)

g_slide = Scale(master=root, from_=1, to=0, resolution=.001, label="g", command=update)
g_slide.set(.03)
g_slide.grid(column=6, row=1)

n_slide = Scale(master=root, from_=1, to=0, resolution=.001, label="n", command=update)
n_slide.set(.02)
n_slide.grid(column=7, row=1)

s_slide = Scale(master=root, from_=1, to=0, resolution=.001, label="s", command=update)
s_slide.set(.1)
s_slide.grid(column=8, row=1)

# initialize and create the graph for the model with parameter values (ideally) set by sliders
figure = plt.Figure(figsize=(6, 5), dpi=100)
axes = figure.add_subplot(1, 1, 1)


canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=0, columnspan=8)

# i'm not sure this should be here like this, but IDK what to do about updating through
# dang sliders. I'll do more reading and try to figure it out later.

usrmodel = models.solow(k_0=k0_slide.get(), l_0=l0_slide.get(), a_0=a0_slide.get(),
                        alpha=alpha_slide.get(), d=delta_slide.get(), g=g_slide.get(),
                        n=n_slide.get(), s=s_slide.get())

root.mainloop()
