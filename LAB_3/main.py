def y_calculation(n, k, W):
    if n == 0:
        pass
    net = net_calculation(n, k, W)
    if net > 0:
        return 1
    elif net < 0:
        return -1
    else:
        return net_calculation(n - 1, k, W)


def net_calculation(n, k, W):
    res = 0
    for j in range(0, 42):
        if j == k:
            continue
        else:
            res += W[j][k] * y_calculation(n - 1, k, W)
    return res


def w_calculation(j, K, X):
    if j == K:
        return 0
    else:
        res = 0
        for l in range(0, 3):
            res += X[l][j] * X[l][K]
        return res


def w_matrix_calculation(X):
    W = list()
    line = list()
    for K in range(0, len(X[0])):
        for j in range(0, len(X[0])):
            line.append(w_calculation(j, K, X))
        W.append(line)
        line = list()
    return W
