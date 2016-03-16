# This module provides the whole program with the nessary methods

# the main F bool function values counter
def bool_function(x1, x2, x3, x4):
    if (x1 + x2 + x3) * (x2 + x3 + x4):
        return 1
    else:
        return 0


# the full error between F and Y counter
def fault_counter(F, Y):
    E = 0
    for i in range(0, len(F)):
        if Y[i] != F[i]:
            E += 1
    return E


# net function
def net(x, w, w0):
    net = 0
    for i in range(0, len(x)):
        net += w[i] * x[i] + w0
    return net
