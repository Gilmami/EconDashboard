# This will be more of proof of concept to figure out if keying in the model and allowing users
# to play around with the variables to get the model on different steady states. we will see. :)

# pretty sure I'm doing this wrong. Need to reference my notes on Recursive dynamic programming.
class model:
    def __init__(self, k0, k1, y, l, a):
        self.k0 = k0
        self.k1 = k1
        self.y = y
        self.l = l
        self.a = a



def solow(K_0 = 1, L_0 = 1, A_0 = 1, alpha = 0.5, d = 0.05, g = 0.03, n = 0.02, s = 0.1, duration = 100):
    k_0 = K_0
    l_0 = L_0
    a_0 = A_0
    y_0 = (k_0 ** alpha) * ((A_0 * l_0) ** (1 - alpha))
    k1points = list()
    k0points = list()
    lpoints = list()
    ypoints = list()
    apoints = list()

    for i in range(1, 1 + duration):
        k_1 = (1 + s - d) * y_0
        l_1 = (1 + g) * l_0
        a_1 = (1 +n) * a_0
        y_1 = (k_1 ** alpha) * ((a_1 * l_1) ** (1 - alpha))
        k1points.append(k_1)
        k0points.append(k_0)
        lpoints.append(l_0)
        ypoints.append(y_0)
        apoints.append(a_0)
        k_0 = k_1
        l_0 = l_1
        y_0 = y_1
        a_0 = a_1

    return model(k0points, k1points, ypoints, lpoints, apoints)


if __name__ == "__main__":
    solow()