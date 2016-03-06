# This module works with files - writing and reading logs

# this function provides the reading of the xi table from file
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


# this function provides the log file writing process
def write_log(file_path, F, Y, E, k, w, w0):
    file = open(file_path, 'a')
    file.write("k = " + str(k) + '\n')
    file.write("F = " + str(F) + '\n')
    file.write("Y = " + str(Y) + '\n')
    file.write("E = " + str(E) + '\n')
    file.write("\n\n")
    file.write("w = " + str(w) + '\t')
    file.write("w0 = " + str(w0) + '\n')
