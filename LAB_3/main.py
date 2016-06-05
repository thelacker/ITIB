def y_calculation(n, k, W, x, netDict):
    if n == 0:
        return x[k]
    try:
        net = netDict[str([n, k])]
    except:
        net = net_calculation(n, k, W, x, netDict)
        netDict.update({str([n, k]): net})
    if net > 0:
        return 1
    elif net < 0:
        return -1
    else:
        return net_calculation(n - 1, k, W, x, netDict)


def net_calculation(n, k, W, x, netDict):
    res = 0
    for j in range(0, 42):
        if j == k:
            continue
        else:
            res += W[j][k] * y_calculation(n - 1, j, W, x, netDict)
    return res


def w_calculation(j, K, X):
    if j == K:
        return 0
    else:
        res = 0
        for l in range(0, len(X)):
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


def read_input(filename="figures.txt"):
    f = open(filename)
    X = list()
    for line in f:
        line.replace(" ", '')
        newline = line.split(',')
        line = list()
        for digit in newline:
            line.append(int(digit))
        X.append(line)
    return X


def check_letter(y, X):
    try:
        return X.index(y) + 1
    except Exception as e:
        print str(e)
        return None


def define_letter(W, x):
    y = list()
    calculatedNetDict = {}
    pixels = 42
    for i in range(0, pixels):
        y.append(y_calculation(pixels, i, W, x, calculatedNetDict))
    return y


def hopfild(x, W, X):
    letter_old = define_letter(W, x)
    letter = check_letter(letter_old, X)

    if letter == 1:
        letter = 2
    elif letter == 2:
        letter = 4
    elif letter == 3:
        letter = 6
    else:
        letter = 'None'

    f = open("output.txt", 'a+')

    output_simbol = ""
    output_simbol += "  _ _ _ _ _ _ _ _ _\n"
    for i in range(7):
        output_simbol += "|"
        for j in range(6 * i, 6 * i + 6):
            if letter_old[j] == 1:
                output_simbol += " 1 "
            else:
                output_simbol += "   "
            print letter_old[j]
        output_simbol += "|"
        output_simbol += "\n"
    output_simbol += "| _ _ _ _ _ _ _ _ _|"
    f.writelines(output_simbol)
    f.write("\nThis is number " + str(letter) + "\n")


def main():
    x = list()
    f = open("x'.txt")
    old_x = f.read().split(',')
    for number in old_x:
        x.append(int(number))

    X = read_input()
    W = w_matrix_calculation(X)

    f = open("output.txt", 'w')
    f.write("\n\t\tFigures\n")
    f.close()
    hopfild(X[0], W, X)
    hopfild(X[1], W, X)
    hopfild(X[2], W, X)
    f = open("output.txt", 'a+')
    f.write("\n\t\tYour vector with errors\n")
    f.close()
    hopfild(x, W, X)



if __name__ == "__main__":
    main()
