from Tkinter import *

class App:

    def __init__(self, master):
        self.boton = Button(root, text="Que te parece la guia?", command=funcion)
        pass

    def say_hi(self,boton):
        self.boton = Tkinter.Button(root, text="Que te parece la guia?", command=funcion)
        self.boton.pack()


root = Tk()

app = App(root)
app.boton.pack()
root.mainloop()