# This module provides the whole program with the necessary methods

from math import exp


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
def net(x, v):
    net = 0
    for i in range(1, 4):
        net += v[i] * fi_counter(x, i) + v[0]
    return net

# fi counter
def fi_counter(x, J):
    fi = 0

    # fi_j is always 1
    if J == 0:
        return 1
    else:
        # searching for the core of fi
        c = find_C(J)

        # counting fi result
        for i in range(4):
            fi += (x[i] - c[i])**2
        fi = exp(-fi)
        return fi


# cores of fi cells
def find_C(J):
    if J == 1:
        return [0, 0, 0, 0]
    if J == 2:
        return [0, 0, 0, 1]
    if J == 3:
        return [1, 0, 0, 0]
