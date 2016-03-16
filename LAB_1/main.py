# This program is emulating an one-cell neural network

from Log import read_file
from Af_threshold import education_threshold
from Af_logistic import education_logistic, education_small_sample
from Graph import *

# Main function stats the process of eduation based on a wi null array
def main():
    # start point
    w = [0, 0, 0, 0]
    w0 = 0
    x0 = 1

    # error is not 0 for the first iteation
    # making a list of the errors for the graph
    E = 1
    E_array = list()

    # era counter
    k = 0

    # reading the function table
    X = read_file("input.txt")

    # while error is not 0 changing the wi array
    while E != 0:
        # educating the neural network and writing the result to log file
        E, w, w0 = education_threshold(X, w, w0, x0, k)

        # appending the error to the array for the graph
        E_array.append(E)

        # next era
        k += 1

    # showing the plot
    error_plot(E_array, range(0, k), "Simple f(net) function")

    # now the logistic activation function is working
    # start point
    w = [0, 0, 0, 0]
    w0 = 0
    E = 1
    E_array = list()
    k = 0

    # while error is not 0 changing the wi array
    while E != 0:
        # educating the neural network and writing the result to log file
        E, w, w0 = education_logistic(X, w, w0, x0, k)

        # appending the error to the array for the graph
        E_array.append(E)

        # next era
        k += 1

    # showing the plot
    error_plot(E_array, range(0, k), "Logistic f(net) function")


    # now the logistic activation function is working
    # start point
    w = [0, 0, 0, 0]
    w0 = 0
    E = 1
    E_array = list()
    k = 0
    i_list = [0,1,2,4,8,9,10,12]
    # while error is not 0 changing the wi array
    while E != 0:
        # educating the neural network and writing the result to log file
        E, w, w0 = education_small_sample(X, w, w0, x0, k, i_list)

        # appending the error to the array for the graph
        E_array.append(E)

        # next era
        k += 1
        if k > 20:
            return 0
    # showing the plot
    error_plot(E_array, range(0, k), "Small set with logistic f(net) function")

if __name__ == "__main__":
    main()
