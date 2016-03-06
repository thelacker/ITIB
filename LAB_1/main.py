from Log import read_file
from Af_threshold import education_threshold
from Af_logistic import education_logistic


def main():
    w = [0, 0, 0, 0]
    w0 = 0
    x0 = 1
    E = 1
    k = 0
    X = read_file("input.txt")
    while E != 0:
        E, w, w0 = education_threshold(X, w, w0, x0, k)
        print E, w, w0
        k += 1
    w = [0, 0, 0, 0]
    w0 = 0
    x0 = 1
    E = 1
    k = 0
    while E != 0:
        E, w, w0 = education_logistic(X, w, w0, x0, k)
        print E, w, w0
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
