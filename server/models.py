# This will be more of proof of concept to figure out if keying in the model and allowing users
# to play around with the variables to get the model on different steady states. we will see. :)

# pretty sure I'm doing this wrong. Need to reference my notes on Recursive dynamic programming.
def solow(K_0,L_0,a,b,d,g,s):
    Y = a * (K_0 ^ b) * (L_0 ^ (1 - b))
    K_1 = (1 + s - d) * K_0
    L_1 = (1 + g) * L_0

    return


if __name__ == "__main__":
    pass