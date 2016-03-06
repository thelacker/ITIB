from Tools import *
from Log import write_log

def w_delta_threshold(x, n, b):
    return x * n * b


def af_threshold(net):
    if net >= 0:
        return 1
    else:
        return 0


def education_threshold(X, w, w0, x0, k):
    F = list()
    Y = list()
    for i in range(0, len(X)):
        F.append(main_function(X[i][0], X[i][1], X[i][2], X[i][3]))
    for i in range(0, len(X)):
        x = X[i]
        Y.append(af_threshold(net(X[i], w, w0)))
        b = F[i] - Y[i]
        w0 += w_delta_threshold(x0, 0.3, b)
        for i in range(0, len(w)):
            w[i] += w_delta_threshold(x[i], 0.3, b)

    E = fault_counter(F, Y)
    write_log("output.txt", F, Y, E, k, w, w0)
    return E, w, w0
