from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "12")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 50
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        

        self.quartoContainer = Frame(master) #Aumenta ou diminui a altura!
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Parking Simulation")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Entrance", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 10
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=BOTTOM)


        self.senhaLabel = Label(self.terceiroContainer, text="Exit", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.exit = Entry(self.terceiroContainer)
        self.exit["width"] = 10
        self.exit["font"] = self.fontePadrao

        self.exit.pack(side=LEFT)

        self.calc = Button(self.quartoContainer)
        self.calc["text"] = "Calcular"
        self.calc["font"] = ("Arial", "8")
        self.calc["width"] = 12
        self.calc.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()




root = Tk()
Application(root)
root.mainloop()