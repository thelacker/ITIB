from math import exp


def f_counter(net):
    F = list()
    for element in net:
        F.append(1.0 / (1 + exp(-element)))
    return F


def f_derivative_counter(net):
    F = list()
    f = f_counter(net)
    for element in f:
        F.append(element * (1 - element))
    return F


def get_input(file_name="input.txt"):
    f = open(file_name)
    input_data = list()
    for line in f:
        if line[0] == '#':
            continue
        else:
            input_data.append(line)
    for i in range(0, len(input_data)):
        input_data[i] = input_data[i].split(',')
    X = list()
    for x in input_data[0]:
        X.append(int(x))
    T = list()
    for t in input_data[1]:
        T.append(int(t))
    V = list()
    for i in range(0, int(input_data[2][1])):
        V.append([])
        for j in range(0, int(input_data[2][0]) + 1):
            V[i].append(0)
    W = list()
    for i in range(0, int(input_data[2][1]) + 1):
        W.append([])
        for j in range(1, int(input_data[2][2]) + 1):
            W[i].append(0)
    return X, T, V, W


def z_in_couter(V, X):
    z_in = list()
    for j in range(0, len(V)):
        z = 0
        for i in range(0, len(X)):
            z += X[i] * V[j][i]
        z += V[j][0]
        z_in.append(z)
    return z_in


def y_in_couter(W, Z):
    y_in = list()
    for j in range(0, len(W)):
        y = 0
        for i in range(0, len(Z)):
            y += Z[i] * W[j][i + 1]
        y += W[j][0]
        y_in.append(y)
    return y_in


def error_counter(T, Y):
    sigma = list()
    for k in range(0, len(T)):
        sigma.append(T[k] - Y[k] * f_derivative_counter(Y)[k])
    return sigma


def W_delta(W, E, Z):
    for j in range(0, len(W)):
        for k in range(0, len(E)):
            if j == 0:
                W[j][k] += E[k]
            else:
                W[j][k] += E[k] * Z[j - 1]


def V_delta(V, E, W):
    for j in range(0, len(V)):
        for k in range(0, len(V[0])):
            if k == 0:
                V[j][k] += E[k]
            else:
                V[j][k] += E[k - 1] * W[j][k - 1]



X, T, V, W = get_input()
Z = f_counter(z_in_couter(V, X))
Y = f_counter(y_in_couter(W, Z))
E = error_counter(T, Y)
print E
W_delta(W, E, Z)
V_delta(V, E, W)
print W
print V
