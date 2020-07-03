# This will be more of proof of concept to figure out if keying in the model and allowing users
# to play around with the variables to get the model on different steady states. we will see. :)

# pretty sure I'm doing this wrong. Need to reference my notes on Recursive dynamic programming.


def solow(K_0, L_0, a, b, d, g, s, duration):
    k_0 = K_0
    l_0 = L_0
    y_0 = a * (k_0 ** b) * (l_0 ** (1 - b))
    points = list()

    for i in range(1, duration):
        k_1 = (1 + s - d) * y_0
        l_1 = (1 + g) * l_0
        y_1 = a * (k_1 ** b) * (l_1 ** (1 - b))
        points.append([k_1, k_0])
        k_0 = k_1
        l_0 = l_1
        y_0 = y_1
    return points


if __name__ == "__main__":
    solow(1,1,1,.5,.1,.05,.15,10)