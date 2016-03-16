from Log import read_file
from Af_RBF import education_RBF
from Graph import *

def main():
    # reading the function table
    X = read_file("input.txt")
    v = [0, 0, 0, 0]

    # error is not 0 for the first iteation
    # making a list of the errors for the graph
    E = 1
    E_array = list()

    # era counter
    k = 0

    i_list = [0, 1, 2, 8]
    # i_list = range(16)
    # while error is not 0 changing the wi array
    while E != 0:
        # educating the neural network and writing the result to log file
        E, v = education_RBF(X, v, k, i_list)

        # appending the error to the array for the graph
        E_array.append(E)

        # next era
        k += 1
        if k > 200:
            print "NON"
            return 1
    # showing the plot
    error_plot(E_array, range(0, k), "Lab 2")

if __name__ == "__main__":
    main()