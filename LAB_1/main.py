from math import tanh, cosh


def main_function(x1, x2, x3, x4):
    if (x1+x2+x3)*(x2+x3+x4):
        return 1
    else:
        return 0


def fault_counter(F, Y):
    E = 0
    for i in range (0, len(F)):
        if Y[i]!=F[i]:
            E += 1
    return E


def w_delta_threshold(x, n, b):
    return x*n*b



def w_delta_logistic(x, n, b, X, w, w0):
    return x*n*b*af_logistic_derivative(net(X,w,w0))


def net(x, w, w0):
    net = 0
    for i in range(0,len(x)):
        net += w[i]*x[i]+w0
    return net


def af_threshold(net):
    if net >= 0:
        return 1
    else:
        return 0


def af_logistic(net):
    return (tanh(net)+1)/2


def af_logistic_derivative(net):
    return (pow( (1/cosh(net) ), 2) / 2)


def read_file(file_path):
    file = open(file_path)
    input_data = list()
    for line in file:
        if line[0] == '#':
            continue
        else:
            new_line = list()
            line = line[::2]
            for number in line:
                try:
                    new_line.append(int(number))
                except:
                    continue
            input_data.append(new_line)
    return input_data


def write_log(file_path, F, Y, E, k, w, w0):
    file = open(file_path, 'a')
    file.write("k = " + str(k) + '\n')
    file.write("w = " + str(w) + '\t')
    file.write("w0 = " + str(w0) + '\n')
    file.write("F = " + str(F) + '\n')
    file.write("Y = " + str(Y) + '\n')
    file.write("E = " + str(E) + '\n')
    file.write("\n\n")


def education_threshold(X, w, w0, x0, k):
    F = list()
    Y = list()
    for i in range(0, len(X)):
        F.append(main_function(X[i][0],X[i][1],X[i][2],X[i][3]))
    for i in range(0,len(X)):
        x = X[i]
        Y.append(af_threshold(net(X[i], w, w0)))
        b = F[i]-Y[i]
        w0 += w_delta_threshold(x0, 0.3, b)
        for i in range (0, len(w)):
            w[i] += w_delta_threshold(x[i], 0.3, b)

    E = fault_counter(F,Y)
    write_log("output.txt", F, Y, E, k, w, w0)
    return E, w, w0


def education_logistic(X, w, w0, x0, k):
    F = list()
    Y = list()
    for i in range(0, len(X)):
        F.append(main_function(X[i][0],X[i][1],X[i][2],X[i][3]))
    for i in range(0,len(X)):
        x = X[i]
        Y.append(af_threshold(net(X[i], w, w0)))
        b = F[i]-Y[i]
        w0 += w_delta_logistic(x0, 0.3, b, x, w, w0)
        for i in range (0, len(w)):
            w[i] += w_delta_logistic(x[i], 0.3, b, x, w, w0)

    E = fault_counter(F, Y)
    write_log("output_1.txt", F, Y, E, k, w, w0)
    return E, w, w0


def main():
    w = [0,0,0,0]
    w0 = 0
    x0 = 1
    E = 1
    k = 0
    X = read_file("input.txt")
    while E != 0:
        E, w, w0 = education_threshold(X, w, w0, x0, k)
        print E, w, w0
        k += 1
    w = [0,0,0,0]
    w0 = 0
    x0 = 1
    E = 1
    k = 0
    while E != 0:
        E, w, w0 = education_logistic(X, w, w0, x0, k)
        print E, w, w0
        k += 1
if __name__ == "__main__":
    main()