from tkinter import *
from data.Data import Data

from views.GestionarCurso import GestionarCurso
from views.SeleccionarArchivo import SeleccionarArchivo


class MenuInicio():

    masterWindow = Tk()

    def __init__(self):
        self.masterWindow.geometry("400x350")
        self.masterWindow.title("Menú de inicio")
        self.initUI()
        self.masterWindow.mainloop()

    def goToGestionarCurso(self):
        newWindow = GestionarCurso(self.masterWindow)
        newWindow.window.grab_set()

    def goToSeleccionarArchivo(self):
        newWindow = SeleccionarArchivo(self.masterWindow)
        newWindow.window.grab_set()

    def prueba(self):
        print(Data.data)

    def initUI(self):

        titleFont = ("Helvetica", 12, "bold")
        buttonFont = ("Helvetica", 10, "bold")

        # Información
        Label(self.masterWindow,
              text="Laboratorio Lenguajes Formales y de Programación", pady=5, font=titleFont).grid(row=0, column=0, pady=10)
        Label(self.masterWindow, text="Nombre: Damián Ignacio Peña Afre",
              pady=5).grid(row=1, column=0, pady=5)
        Label(self.masterWindow, text="Carné: 202110568",
              pady=5).grid(row=2, column=0, pady=5)

        # Separador
        Label(self.masterWindow, text="Opciones:",
              pady=5, font=titleFont).grid(row=3, column=0, pady=5)

        # Botones
        Button(self.masterWindow, text="Cargar archivo",
               pady=5, padx=10, bg="#0D6EFD", fg="white", font=buttonFont, command=self.goToSeleccionarArchivo).grid(row=4, column=0, pady=5)

        Button(self.masterWindow, text="Gestionar cursos",
               pady=5, padx=10, bg="#0D6EFD", fg="white", font=buttonFont, command=self.goToGestionarCurso).grid(row=5, column=0, pady=5)

        Button(self.masterWindow, text="Conteo creditos",
               pady=5, padx=10, bg="#0D6EFD", fg="white", font=buttonFont).grid(row=6, column=0, pady=5)

        Button(self.masterWindow, text="Salir",
               pady=5, padx=10, bg="#DC3545", fg="white", font=buttonFont, command=self.masterWindow.destroy).grid(row=7, column=0, pady=5)
