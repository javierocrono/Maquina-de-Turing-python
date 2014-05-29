# -*- coding: utf-8 -*-

from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="quit", fg="red",
            command = frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

if __name__ == "__main__":

    root = Tk()
    app = App(root)
    root.mainloop()


# Evaluaciones del ramo
# trabajos practicos y controles de lectura 30%
# 2 pruebas teoricas 20% c/u
# trabajo final 30%
# no hay examen
# nota minima de aprobacion 4,5
# asistencia 80%