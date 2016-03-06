from math import tanh, cosh
from Tools import *
from Log import write_log


def y_couter(net):
    if net >= 0:
        return 1
    else:
        return 0


def w_delta_logistic(x, n, b, X, w, w0):
    return x * n * b * af_logistic_derivative(net(X, w, w0))


def af_logistic(net):
    return (tanh(net) + 1) / 2


def af_logistic_derivative(net):
    return (pow((1 / cosh(net)), 2) / 2)


def education_logistic(X, w, w0, x0, k):
    F = list()
    Y = list()
    for i in range(0, len(X)):
        F.append(main_function(X[i][0], X[i][1], X[i][2], X[i][3]))
    for i in range(0, len(X)):
        x = X[i]
        Y.append(y_couter(net(X[i], w, w0)))
        b = F[i] - Y[i]
        w0 += w_delta_logistic(x0, 0.3, b, x, w, w0)
        for i in range(0, len(w)):
            w[i] += w_delta_logistic(x[i], 0.3, b, x, w, w0)

    E = fault_counter(F, Y)
    write_log("output_1.txt", F, Y, E, k, w, w0)
    return E, w, w0
