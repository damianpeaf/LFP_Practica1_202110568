from tkinter import *
from tkinter import messagebox

from data.Data import Data


class AgregarCursos():

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("400x240")
        self.window.title("Agregar Cursos")
        self.initUI()

    def sendForm(self):
        codigo = self.codigoEntry.get()
        nombre = self.nombreEntry.get()
        prerrequisito = self.prerrequisitoEntry.get()
        semestre = self.semestreEntry.get()
        opcionalidad = self.opcionalidadEntry.get()
        creditos = self.creditosEntry.get()
        estado = self.estadoEntry.get()

        rowWithCommas = codigo + ","+nombre+","+prerrequisito + \
            "," + opcionalidad+","+semestre+","+creditos+","+estado

        newRow = Data.createRow(rowWithCommas, len(Data.data)+1)

        if newRow:
            Data.addRowToData(newRow)
        Data.generateErrorsAndWarning()

        if len(Data.warningMessagesList) > 0:
            messagebox.showwarning(title="Advertencia",
                                   message=Data.warningMessages)

        if len(Data.headerErrors) > 0 or len(Data.globalrowErrors) > 0:
            messagebox.showerror(title="Error", message=Data.errorMessages)
        else:
            messagebox.showinfo(title="Informacion cargada",
                                message="Informacion cargada")

        Data.cleanErrors()

    def initUI(self):
        Label(self.window, text="Codigo").grid(column=0, row=0)
        self.codigoEntry = Entry(self.window)
        self.codigoEntry.grid(column=1, row=0)

        Label(self.window, text="Nombre").grid(column=0, row=1)
        self.nombreEntry = Entry(self.window)
        self.nombreEntry.grid(column=1, row=1)

        Label(self.window, text="prerrequisito").grid(column=0, row=2)
        self.prerrequisitoEntry = Entry(self.window)
        self.prerrequisitoEntry.grid(column=1, row=2)

        Label(self.window, text="semestre").grid(column=0, row=3)
        self.semestreEntry = Entry(self.window)
        self.semestreEntry.grid(column=1, row=3)

        Label(self.window, text="opcionalidad").grid(column=0, row=4)
        self.opcionalidadEntry = Entry(self.window)
        self.opcionalidadEntry.grid(column=1, row=4)

        Label(self.window, text="creditos").grid(column=0, row=5)
        self.creditosEntry = Entry(self.window)
        self.creditosEntry.grid(column=1, row=5)

        Label(self.window, text="estado").grid(column=0, row=6)
        self.estadoEntry = Entry(self.window)
        self.estadoEntry.grid(column=1, row=6)

        Button(self.window, text="Cargar", pady=5,
               padx=10, bg="#198754", command=self.sendForm).grid(column=0, row=7)

        Button(self.window, text="Regresar", pady=5, padx=10, bg="#0D6EFD",
               command=self.window.destroy).grid(column=1, row=7)
