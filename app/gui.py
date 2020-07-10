from tkinter import *

subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

window = Tk()
window.title("Model Calibration")

k0_slide = Scale(master = window, from_= 1000, to = 0, label = "K0".translate(subscript))
k0_slide.set(1)
k0_slide.pack()

l0_slide = Scale(master = window, from_= 1000, to = 0, label = "L0".translate(subscript))
l0_slide.set(1)
l0_slide.pack()

alpha_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "a")
alpha_slide.set(.7)
alpha_slide.pack()

delta_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "d")
delta_slide.set(.05)
delta_slide.pack()

g_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "g")
g_slide.set(.03)
g_slide.pack()

n_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "n")
n_slide.set(.02)
n_slide.pack()

s_slide = Scale(master = window, from_= 1, to = 0, resolution = .01, label = "s")
s_slide.set(.1)
s_slide.pack()

window.mainloop()
