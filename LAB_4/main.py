from Tkinter import *
from math import pow, sqrt
from random import randint

from numpy import median


class Clasterisation:
    def __init__(self):
        # drawing stage
        self.dimension = 2
        self.colors = ['black', 'green', 'blue', 'red', 'white', 'grey']

        self.clusters = list()
        self.centers = list()

        self.flush()

        # dots
        self.dots = list()

        # the main window
        self.window = Tk()
        self.window.title('Lab 4')
        self.window.geometry('1000x900+100+100')
        self.window.resizable(False, False)
        self.drawing_area = Canvas(self.window, width=1000, height=690)
        self.drawing_area.pack()
        self.drawing_area.bind("<ButtonPress-1>", self.draw_dots)
        self.btn = Button(self.window, bd=7, text='Euclidean', width=30, height=1, font='arial 24')
        self.btn.bind("<Button-1>", self.euclidean)
        self.btn.place(x=10, y=700, width=470)
        self.btn2 = Button(self.window, bd=7, text='Manhattan', width=30, height=1, font='arial 24')
        self.btn2.bind("<Button-1>", self.manhattan)
        self.btn2.place(x=510, y=700, width=470)
        self.btn3 = Button(self.window, bd=7, text='Generate dots', width=30, height=1, font='arial 24')
        self.btn3.bind("<Button-1>", self.generate_dots)
        self.btn3.place(x=10, y=800, width=970)

    def generate_dots(self, event):
        for i in range(randint(40, 50)):
            x = randint(10, 970)
            y = randint(10, 650)
            self.drawing_area.create_oval(x, y, x + 7, y + 7, width=1, fill=self.colors[0])
            self.dots.append([x, y])

    def draw_dots(self, event):
        event.widget.create_oval(event.x, event.y, event.x + 7, event.y + 7, width=1, fill=self.colors[0])
        self.dots.append([event.x, event.y])

    def euclidean(self, event):
        self.proceed('E')

    def proceed(self, method):
        old_centers = list()
        old_clusters = list()
        for i in range(self.dimension):
            self.centers.append(self.dots[randint(0, int(len(self.dots)) - 1)])
        self.classify(method=method)
        self.centers = list()
        old_centers.append(self.centers)
        old_clusters.append(self.clusters)
        while True:
            print self.centers
            print self.clusters
            self.find_center()
            if old_centers.pop() == self.centers or old_clusters.pop() == self.clusters:
                break
            self.classify(method=method)
            old_centers.append(self.centers)
            old_clusters.append(self.clusters)
            self.centers = list()

        for i in range(self.dimension):
            for dot in self.clusters[i]:
                self.drawing_area.create_oval(dot[0], dot[1], dot[0] + 7, dot[1] + 7, width=1, fill=self.colors[i + 1])

        self.flush()

    def flush(self, center=True):
        if center is True:
            self.centers = list()
        self.clusters = list()
        for i in range(self.dimension):
            self.clusters.append([])

    def find_center(self):
        for i in range(self.dimension):
            x = [item[0] for item in self.clusters[i]]
            y = [item[1] for item in self.clusters[i]]
            self.centers.append([median(x), median(y)])

    def classify(self, method):
        self.flush(False)
        values = list()
        for dot in self.dots:
            for i in range(len(self.centers)):
                if method == 'E':
                    values.append(self.metric_euclidean(dot, self.centers[i]))
                if method == 'M':
                    values.append(self.metric_manhattan(dot, self.centers[i]))
            self.clusters[values.index(min(values))].append(dot)
            values = list()

    def manhattan(self, event):
        self.proceed('M')

    def metric_euclidean(self, p1, p2):
        return sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2))

    def metric_manhattan(self, p1, p2):
        return abs((p1[0] - p2[0])) + abs((p1[1] - p2[1]))

    def run(self):
        self.window.mainloop()


while True:
    try:
        window = Clasterisation()
        window.run()
        break
    except:
        continue
