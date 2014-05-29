# -*- coding: utf-8 -*-

from Tkinter import *
from enc import *

a = enc()


class App(enc):

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        Label(frame, text="Uso:\n", anchor=W, justify=LEFT).pack()
        Label(frame, text="1.- Ingrese palabra a encriptar..\n").pack()
        Label(frame, text="2.- Seleccione el tipo de encriptacion..\n").pack()
        Label(frame, text="3.- En caso de usar cesar se solicitara").pack()
        Label(frame, text=" que ingrese el N° de saltos que desea\n").pack()
        Label(frame, text="4.- Presione ""encriptar""\n").pack()
        Label(frame, text="5.- Para terminar programa presione Quit\n").pack()
        self.ent = Entry(frame)
        self.ent.pack()
        self.ent2 = Entry(frame)

        self.button = Button(compound=BOTTOM, text="Quit",
            command=frame.quit)
        self.button.pack(side=BOTTOM)

        self.button = Button(v1, compound=BOTTOM, text="Quit",
            command=frame.quit)
        self.button.pack(side=BOTTOM)

        self.button = Button(compound=BOTTOM, text="Cesar",
             command=self.cesarCant)
        self.button.pack(side=LEFT)

        self.hi_there = Button(compound=BOTTOM, text="Cenit_Polar",
             command=self.cenit)
        self.hi_there.pack(side=RIGHT)

    def cesarCant(self):
        self.ent2.pack()
        self.button = Button(text="Encriptar", command=self.cesar)
        self.button.pack()

    def cesar(self):
        res = self.ent.get()
        cant = int(self.ent2.get())
        print res, cant
        Label(v1, text="\nSe ha escogido cesar").pack()
        res2 = (a.cesar(res, cant))
        Label(v1, text="\n\nResultado de la encriptacion: \n\n").pack()
        Label(v1, text=str(res2)).pack()
        v1.deiconify()

    def cenit(self):
        res = self.ent.get()
        Label(v1, text="\nSe ha escogido cenit_polar").pack()
        res2 = (a.cenit_polar(res))
        Label(v1, text="\n\nResultado de la encriptacion: \n\n").pack()
        Label(v1, text=str(res2)).pack()
        v1.deiconify()

if __name__ == "__main__":

    root = Tk()
    root.title("Encriptador")
    root.geometry("300x400")
    Entry(root).pack
    v1 = Toplevel(root)
    v1.geometry("300x200")
    v1.withdraw()
    app = App(root)
    root.mainloop()