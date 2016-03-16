from Tools import bool_function, net, fault_counter, fi_counter
from Log import write_log


def y_counter(net):
    if net >= 0:
        return 1
    else:
        return 0


# counting the delta w for the next step
def v_delta(n, b, X, v, J):
    return n * b * fi_counter(X, J)


# education process
def education_RBF(X, v, k, i_list):
    # lists od F and Y values
    F = list()
    Y = list()

    # counting the F function
    for i in range(0, len(X)):
        F.append(bool_function(X[i][0], X[i][1], X[i][2], X[i][3]))

    # counting the Y function on k era with specified w array
    for i in i_list:
        x = X[i]

        # step mistake is counted
        b = bool_function(X[i][0], X[i][1], X[i][2], X[i][3]) - y_counter(net(X[i], v))

        # all the v are recounted by the delta rule
        for j in range(0, len(v)):
            v[j] += v_delta(0.3, b, x, v, j)

    # counting the Y function
    for i in range(0, len(X)):
         Y.append(y_counter(net(X[i], v)))

    # the full mistake is counted
    E = fault_counter(F, Y)

    # writing the result to log file
    write_log("output_1.txt", F, Y, E, k, v)
    return E, v