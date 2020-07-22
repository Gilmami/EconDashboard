# This will be more of proof of concept to figure out if keying in the model and allowing users
# to play around with the variables to get the model on different steady states. we will see. :)

# pretty sure I'm doing this wrong. Need to reference my notes on Recursive dynamic programming.
class model:
    def __init__(self, k0, k1, y, l, a, t):
        self.k0 = k0
        self.k1 = k1
        self.y = y
        self.l = l
        self.a = a
        self.t = t
        self.vars = [i for i in dir(self) if not callable(i) if not i.startswith("__")]


def solow(k_0=1, l_0=1, a_0=1, alpha=0.5, d=0.04, g=0.03, n=0.02, s=0.1, duration=100):
    # k_0 is initial capital, l_0 is initial labor, a_0 is initial labor tech, g is growth of pop.
    # n is development of technology, s is savings rate.
    y_0 = ((k_0 ** alpha) * ((a_0 * l_0) ** (1 - alpha)))
    k1points = list()
    k0points = list()
    lpoints = list()
    ypoints = list()
    apoints = list()
    t = list()

    for i in range(0, duration):
        k_1 = (1 + s - d) * y_0
        l_1 = (1 + g) * l_0
        a_1 = (1 + n) * a_0
        y_1 = ((k_1 ** alpha) * ((a_1 * l_1) ** (1 - alpha)))
        k1points.append(k_1)
        k0points.append(k_0)
        lpoints.append(l_0)
        ypoints.append(y_0)
        apoints.append(a_0)
        t.append(i)
        k_0 = k_1
        l_0 = l_1
        y_0 = y_1
        a_0 = a_1

    return model(k0points, k1points, ypoints, lpoints, apoints, t)
# I don't think this is right, it's giving me some messed up graphs. I'll make sure my formulation is
# correct next time I work on this.

if __name__ == "__main__":
    solow()