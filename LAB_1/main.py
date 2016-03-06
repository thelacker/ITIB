def net(x, w, w0=0):
    net = 0
    for i in range(0,5):
        net += w[i]*x[i]+w0
    return net

def af_threshold:
    pass

def af_logistic:
    pass

def read_file(file_path):
    file = open(file_path)
    input_data = list()
    for line in file:
        if line[0] == '#':
            continue
        else:
            input_data.append(float(line))
    return input_data

def main():
    input_data = read_file("input.txt")
    print input_data

if __name__ == "__main__":
    main()