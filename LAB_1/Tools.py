def main_function(x1, x2, x3, x4):
    if (x1 + x2 + x3) * (x2 + x3 + x4):
        return 1
    else:
        return 0


def fault_counter(F, Y):
    E = 0
    for i in range(0, len(F)):
        if Y[i] != F[i]:
            E += 1
    return E


def net(x, w, w0):
    net = 0
    for i in range(0, len(x)):
        net += w[i] * x[i] + w0
    return net

"""
def education_small_sample(X, w, w0, x0, k):
    F = list()
    Y = list()
    for i in range(0, len(X)):
        F.append(main_function(X[i][0], X[i][1], X[i][2], X[i][3]))
    for i in range(0, len(X), 3):
        x = X[i]
        Y.append(af_threshold(net(X[i], w, w0)))
        b = F[i] - Y.pop()
        w0 += w_delta_logistic(x0, 0.3, b, x, w, w0)
        for i in range(0, len(w)):
            w[i] += w_delta_logistic(x[i], 0.3, b, x, w, w0)

    E = fault_counter(F, Y)
    write_log("output_2.txt", F, Y, E, k, w, w0)
    return E, w, w0
"""