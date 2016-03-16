import matplotlib.pyplot as plt


def error_plot(E, k, label = "Plot"):
    plt.plot(k, E)
    plt.xlabel('Era (k)')
    plt.ylabel('Error (E)')
    print k[-1]
    plt.axis([0, k[-1]+1, 0, max(E)+1])
    plt.title(label)
    plt.grid(True)
    plt.savefig("plt_{0}.png".format(label))
    plt.show()
