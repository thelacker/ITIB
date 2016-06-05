from Tkinter import *
from math import pow, sqrt
from random import randint

from numpy import average


class Clasterisation:
    def euclidean(self, event):
        if not self.dots:
            pass
        else:
            self.proceed('E')

    def metric_euclidean(self, p1, p2):
        return sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2))

    def chebyshev(self, event):
        if not self.dots:
            pass
        else:
            self.proceed('M')

    def metric_chebyshev(self, p1, p2):
        return max([abs((p1[0] - p2[0])), abs((p1[1] - p2[1]))])

    def draw_dots(self, event):
        event.widget.create_oval(event.x, event.y, event.x + 10, event.y + 10, width=1, fill=self.colors[0])
        self.dots.append([event.x, event.y])

    def run(self):
        self.window.mainloop()

    def proceed(self, method):
        old_centers = list()
        old_clusters = list()

        for i in range(self.dimension):
            self.centers.append(self.dots[randint(0, int(len(self.dots)) - 1)])

        self.classify(method=method)
        self.centers = []

        old_centers.append(self.centers)
        old_clusters.append(self.clusters)

        while True:
            self.find_center()
            self.classify(method=method)

            if old_centers.pop() == self.centers:
                for dot in self.centers:
                    self.drawing_area.create_oval(dot[0], dot[1], dot[0] + 15, dot[1] + 15, width=1, fill='green')
                break

            old_centers.append(self.centers)
            old_clusters.append(self.clusters)
            self.centers = []

        for i in range(self.dimension):
            for dot in self.clusters[i]:
                color = self.colors[i + 1]
                self.drawing_area.create_oval(dot[0], dot[1], dot[0] + 7, dot[1] + 7, width=1, fill=color)

        self.flush()

    def find_center(self):
        self.centers = []
        for i in range(self.dimension):
            x = [item[0] for item in self.clusters[i]]
            y = [item[1] for item in self.clusters[i]]
            self.centers.append([average(x), average(y)])

    def flush(self, center=True):
        if center is True:
            self.centers = []
        self.clusters = []
        for i in range(self.dimension):
            self.clusters.append([])

    def classify(self, method):
        self.flush(False)
        values = list()
        for dot in self.dots:
            for i in range(len(self.centers)):
                if method == 'E':
                    values.append(self.metric_euclidean(dot, self.centers[i]))
                if method == 'M':
                    values.append(self.metric_chebyshev(dot, self.centers[i]))
            self.clusters[values.index(min(values))].append(dot)
            values = list()

    def reset(self, event):
        self.drawing_area.delete("all")
        self.flush()
        self.dots = list()

    def __init__(self, dimension=2):
        # drawing stage
        self.dimension = dimension
        self.colors = ['black', '#E210F5', '#F59E10', '#0213FC', '#FCEB02']

        self.clusters = list()
        self.centers = list()

        self.flush()

        # dots
        self.dots = list()

        # the main window
        self.window = Tk()
        self.window.title('Lab 4')
        self.window.geometry('1000x900+50+50')
        self.window.resizable(False, False)

        # the area where are the dots
        self.drawing_area = Canvas(self.window, width=980, height=690, bd=7)
        self.drawing_area.place(x=15, y=210, width=960)
        self.drawing_area.bind("<ButtonPress-1>", self.draw_dots)

        # buttons
        self.btn_euc = Button(self.window, text='Euclid', width=30, height=2, font='arial 12', bd=10)
        self.btn_euc.bind("<Button-1>", self.euclidean)
        self.btn_euc.place(x=10, y=80, width=350)
        self.btn_man = Button(self.window, text='Chebyshev', width=30, height=2, font='arial 12', bd=10)
        self.btn_man.bind("<Button-1>", self.chebyshev)
        self.btn_man.place(x=10, y=10, width=350)
        self.btn_res = Button(self.window, text='New', width=30, height=5, font='arial 12', bd=10)
        self.btn_res.bind("<Button-1>", self.reset)
        self.btn_res.place(x=380, y=10, width=600)


window = Clasterisation(dimension=3)
window.run()
