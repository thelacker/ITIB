# This program is emulating an one-cell neural network

from Log import read_file
from Af_threshold import education_threshold
from Af_logistic import education_logistic


# Main function stats the process of eduation based on a wi null array
def main():
    # start point
    w = [0, 0, 0, 0]
    w0 = 0
    x0 = 1

    # error is not 0 for the first iteation
    E = 1

    # era counter
    k = 0

    # reading the function table
    X = read_file("input.txt")

    # while error is not 0 changing the wi array
    while E != 0:
        # educating the neural network and writing the result to log file
        E, w, w0 = education_threshold(X, w, w0, x0, k)
        k += 1

    # now the logistic activation function is working
    # start point
    w = [0, 0, 0, 0]
    w0 = 0
    E = 1
    k = 0

    # while error is not 0 changing the wi array
    while E != 0:
        # educating the neural network and writing the result to log file
        E, w, w0 = education_logistic(X, w, w0, x0, k)
        k += 1

    """
    w = [0,0,0,0]
    w0 = 0
    x0 = 1
    E = 1
    k = 0
    while E != 0:
        E, w, w0 = education_small_sample(X, w, w0, x0, k)
        print E, w, w0
        k += 1
    """


if __name__ == "__main__":
    main()
