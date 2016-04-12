def y_calculation(n, k, W, x, prenet):
    if n == 0:
        return x[k]
    try:
        net = prenet[str([n, k])]
    except:
        net = net_calculation(n, k, W, x)
        prenet.update({str([n, k]): net})
    if net > 0:
        return 1
    elif net < 0:
        return -1
    else:
        return net_calculation(n - 1, k, W, x)


def net_calculation(n, k, W, x):
    res = 0
    for j in range(0, 42):
        if j == k:
            continue
        else:
            res += W[j][k] * y_calculation(n - 1, j, W, x)
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


x1 = [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1,
      -1, -1, -1, -1, 1, 1, 1, 1, 1, 1]

x2 = [1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1,
      -1, -1, -1, 1, -1, -1, -1, -1, -1, 1]

x3 = [1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1,
      -1, -1, -1, 1, 1, 1, 1, 1, 1, 1]
#    [1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1]


X = list()
X.append(x1)
X.append(x2)
X.append(x3)

x = [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1,
     -1,
     -1, -1, -1, 1, 1, 1, 1, 1, 1, 1]

W = w_matrix_calculation(X)
y = list()
prenet = {}

for i in range(0, 42):
    y.append(y_calculation(42, i, W, x, prenet))

print y
