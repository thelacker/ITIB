from Af_RBF import education_RBF
from Graph import *
from Log import read_file


def main():
    # reading the function table
    # making an array of v
    X = read_file("input.txt")
    v = [0, 0, 0, 0, 0, 0]

    # error is not 0 for the first iteation
    # making a list of the errors for the graph
    E = 1
    E_array = list()

    # era counter
    k = 0

    # the min education
    i_list = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]
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