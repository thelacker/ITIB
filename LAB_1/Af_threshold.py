# This module includes all the methods for the threshold activation function

from Tools import *
from Log import write_log


# counting the delta w for the next step
def w_delta_threshold(x, n, b):
    return x * n * b


# the activation function
def af_threshold(net):
    if net >= 0:
        return 1
    else:
        return 0


# education process
def education_threshold(X, w, w0, x0, k):
    # lists od F and Y values
    F = list()
    Y = list()

    # counting the F function
    for i in range(0, len(X)):
        F.append(bool_function(X[i][0], X[i][1], X[i][2], X[i][3]))

    # counting the Y function on k era with specified w array
    for i in range(0, len(X)):
        x = X[i]
        Y.append(af_threshold(net(X[i], w, w0)))

        # step mistake is counted
        b = F[i] - Y[i]

        # all the w are recounted by the delta rule
        w0 += w_delta_threshold(x0, 0.3, b)
        for i in range(0, len(w)):
            w[i] += w_delta_threshold(x[i], 0.3, b)

    # the full mistake is counted
    E = fault_counter(F, Y)

    # writing the result to log file
    write_log("output.txt", F, Y, E, k, w, w0)
    return E, w, w0
