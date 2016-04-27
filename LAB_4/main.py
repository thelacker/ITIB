from Tkinter import *
from math import pow, sqrt
from random import randint

from numpy import median


class Clasterisation:
    def __init__(self, dimension=2):
        # drawing stage
        self.dimension = dimension
        self.colors = ['black', 'green', 'blue', 'red', 'magenta', 'grey', 'cyan']

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

        # the area where are the dots
        self.drawing_area = Canvas(self.window, width=980, height=690, bd=7, cursor='dot')
        self.drawing_area.place(x=15, y=25, width=970)
        self.drawing_area.bind("<ButtonPress-1>", self.draw_dots)

        # buttons
        self.btn_euc = Button(self.window, bd=7, text='Euclidean', width=30, height=1, font='arial 10')
        self.btn_euc.bind("<Button-1>", self.euclidean)
        self.btn_euc.place(x=10, y=800, width=90)
        self.btn_man = Button(self.window, bd=7, text='Manhattan', width=30, height=1, font='arial 10')
        self.btn_man.bind("<Button-1>", self.manhattan)
        self.btn_man.place(x=10, y=850, width=90)
        self.btn_gener = Button(self.window, bd=7, text='Generate dots', width=30, height=1, font='arial 10')
        self.btn_gener.bind("<Button-1>", self.generate_dots)
        self.btn_gener.place(x=10, y=750, width=180)
        self.btn_res = Button(self.window, bd=7, text='Reset', width=30, height=6, font='arial 10')
        self.btn_res.bind("<Button-1>", self.reset)
        self.btn_res.place(x=200, y=750, width=80)

        # entry dimentions
        self.entry = Entry(self.window, width=180, font='arial 37', bd=7)
        self.entry.place(x=110, y=800, width=80)

        self.T = Text(self.window, height=4, width=50)
        self.T.place(x=290, y=750, width=700)

    def generate_dots(self, event):
        self.dimension = int(self.entry.get())
        for i in range(self.dimension):
            dot_list = [randint(200, 740), randint(200, 440)]
            for l in range(randint((int(60 / self.dimension)), int(70 / self.dimension))):
                new_dots = [dot_list[j] + randint(1, int(300 / self.dimension)) for j in range(2)]
                x = int(new_dots[0])
                y = int(new_dots[1])
                self.drawing_area.create_oval(x, y, x + 7, y + 7, width=1, fill=self.colors[0])
                self.dots.append([x, y])

    def draw_dots(self, event):
        event.widget.create_oval(event.x, event.y, event.x + 7, event.y + 7, width=1, fill=self.colors[0])
        self.dots.append([event.x, event.y])

    def euclidean(self, event):
        self.dimension = int(self.entry.get())
        if not self.dots:
            pass
        else:
            self.proceed('E')

    def manhattan(self, event):
        self.dimension = int(self.entry.get())
        if not self.dots:
            pass
        else:
            self.proceed('M')

    def proceed(self, method):
        old_centers = list()
        old_clusters = list()

        for i in range(self.dimension):
            self.centers.append(self.dots[randint(0, int(len(self.dots)) - 1)])

        to_write = "Step 1:\n" + "Centers:\n" + str(self.centers) + "\nClusters:\n" + str(self.clusters) + "\n\n"
        self.T.insert(END, to_write)

        self.classify(method=method)
        self.centers = []

        old_centers.append(self.centers)
        old_clusters.append(self.clusters)

        while True:
            print 1
            self.find_center()
            self.classify(method=method)

            to_write = "Next Step:\n" + "Centers:\n" + str(self.centers) + "\nClusters:\n" + str(self.clusters) + "\n\n"
            self.T.insert(END, to_write)

            if old_centers.pop() == self.centers:
                break

            old_centers.append(self.centers)
            old_clusters.append(self.clusters)
            self.centers = []

        for i in range(self.dimension):
            for dot in self.clusters[i]:
                self.drawing_area.create_oval(dot[0], dot[1], dot[0] + 7, dot[1] + 7, width=1, fill=self.colors[i + 1])

        self.flush()

    def flush(self, center=True):
        if center is True:
            self.centers = []
        self.clusters = []
        for i in range(self.dimension):
            self.clusters.append([])

    def find_center(self):
        self.centers = []
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

    def metric_euclidean(self, p1, p2):
        return sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2))

    def metric_manhattan(self, p1, p2):
        return abs((p1[0] - p2[0])) + abs((p1[1] - p2[1]))

    def reset(self, event):
        self.drawing_area.delete("all")
        self.flush()
        self.dots = list()

    def run(self):
        self.window.mainloop()


window = Clasterisation()
window.run()
