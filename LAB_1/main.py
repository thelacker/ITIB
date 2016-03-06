from math import tanh, cosh


def main_function(x1, x2, x3, x4):
    if (x1+x2+x3)*(x2+x3+x4):
        return 1
    else:
        return 0


def fault_counter(t, y):
    return t - y


def w_delta_threshold(x, n, b):
    return x*n*b



def w_delta_logistic():
    pass


def w_counter(w, w_delta):
    return w + w_delta


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


def main():
    w = [0,0,0,0]
    w0 = 0
    X = read_file("input.txt")
    F = list()
    Y = list()
    for i in range (0, len(X)):
        F.append(main_function(X[i][0],X[i][1],X[i][2],X[i][3]))
    for i in range (0,len(X)):
        Y.append(af_threshold(net(X[i], w, w0)))
    print Y 

if __name__ == "__main__":
    main()