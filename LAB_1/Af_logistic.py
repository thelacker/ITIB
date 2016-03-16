# This module includes all the methods for the logistic activation function

from math import tanh, cosh
from Tools import *
from Log import write_log


# the main y function
def y_counter(net):
    if net >= 0:
        return 1
    else:
        return 0


# counting the delta w for the next step
def w_delta_logistic(x, n, b, X, w, w0):
    return x * n * b * af_logistic_derivative(net(X, w, w0))


# the activation function
def af_logistic(net):
    return (tanh(net) + 1) / 2


# the derivative of the activation function
def af_logistic_derivative(net):
    return (pow((1 / cosh(net)), 2) / 2)


# education process
def education_logistic(X, w, w0, x0, k):
    # lists od F and Y values
    F = list()
    Y = list()

    # counting the F function
    for i in range(0, len(X)):
        F.append(bool_function(X[i][0], X[i][1], X[i][2], X[i][3]))

    # counting the Y function on k era with specified w array
    for i in range(0, len(X)):
        x = X[i]
        Y.append(y_counter(net(X[i], w, w0)))

        # step mistake is counted
        b = F[i] - Y[i]

        # all the w are recounted by the delta rule
        w0 += w_delta_logistic(x0, 0.3, b, x, w, w0)
        for i in range(0, len(w)):
            w[i] += w_delta_logistic(x[i], 0.3, b, x, w, w0)

    # the full mistake is counted
    E = fault_counter(F, Y)

    # writing the result to log file
    write_log("output_1.txt", F, Y, E, k, w, w0)
    return E, w, w0


# education process
def education_small_sample(X, w, w0, x0, k):
    # lists od F and Y values
    F = list()
    Y = list()
    i_list = []
    # counting the F function
    for i in range(0, i_list):
        F.append(bool_function(X[i][0], X[i][1], X[i][2], X[i][3]))

    # counting the Y function on k era with specified w array
    for i in range(0, i_list):
        x = X[i]
        Y.append(y_counter(net(X[i], w, w0)))

        # step mistake is counted
        b = F[i] - Y[i]

        # all the w are recounted by the delta rule
        w0 += w_delta_logistic(x0, 0.3, b, x, w, w0)
        for i in range(0, len(w)):
            w[i] += w_delta_logistic(x[i], 0.3, b, x, w, w0)

    # counting the F function
    for i in range(0, len(X)):
        F.append(bool_function(X[i][0], X[i][1], X[i][2], X[i][3]))
    # counting the Y function on k era with specified w array
    for i in range(0, len(X)):
        Y.append(y_counter(net(X[i], w, w0)))

    # the full mistake is counted
    E = fault_counter(F, Y)

    # writing the result to log file
    write_log("output_2.txt", F, Y, E, k, w, w0)
    return E, w, w0