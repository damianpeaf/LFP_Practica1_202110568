from tkinter import *
from tkinter import messagebox

from data.Data import Data


class BuscarCurso():

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("240x240")
        self.window.config(bg='#1B1F3B')
        self.window.title("Buscar Curso")
        self.initUI()

    def handleSearch(self):

        codigo = self.searchCodigoEntry.get()
        results = Data.searchByCode(codigo)

        if not results['row']:
            self.rowToEdit = None
            self.codigoEntry.delete(0, END)
            self.codigoEntry.insert(0, "")
            messagebox.showwarning(title="Advertencia",
                                   message="No se ha encontrado el curso")
            return

        row = results['row']
        self.rowToEdit = row

        prerrequisitos = ""
        if row.prerrequisitos:
            prerrequisitos = '; '.join(str(e) for e in row.prerrequisitos)

        self.codigoEntry.delete(0, END)
        self.codigoEntry.insert(0, str(row.codigo))

        self.nombreEntry.delete(0, END)
        self.nombreEntry.insert(0, str(row.nombre))

        self.prerrequisitoEntry.delete(0, END)
        self.prerrequisitoEntry.insert(0, prerrequisitos)

        self.semestreEntry.delete(0, END)
        self.semestreEntry.insert(0, str(row.semestre))

        self.opcionalidadEntry.delete(0, END)
        self.opcionalidadEntry.insert(0, str(row.obligatorio['number']))

        self.creditosEntry.delete(0, END)
        self.creditosEntry.insert(0, str(row.creditos))

        self.estadoEntry.delete(0, END)
        self.estadoEntry.insert(0, str(row.estado['number']))

    def initUI(self):

        self.rowToEdit = None

        Label(self.window, text="Codigo", bg='#1B1F3B',
              fg="white").grid(column=0, row=0)
        self.codigoEntry = Entry(self.window)
        self.codigoEntry.grid(column=1, row=0)

        Label(self.window, text="Nombre", bg='#1B1F3B',
              fg="white").grid(column=0, row=1)
        self.nombreEntry = Entry(self.window)
        self.nombreEntry.grid(column=1, row=1)

        Label(self.window, text="prerrequisito", bg='#1B1F3B',
              fg="white").grid(column=0, row=2)
        self.prerrequisitoEntry = Entry(self.window)
        self.prerrequisitoEntry.grid(column=1, row=2)

        Label(self.window, text="semestre", bg='#1B1F3B',
              fg="white").grid(column=0, row=3)
        self.semestreEntry = Entry(self.window)
        self.semestreEntry.grid(column=1, row=3)

        Label(self.window, text="opcionalidad", bg='#1B1F3B',
              fg="white").grid(column=0, row=4)
        self.opcionalidadEntry = Entry(self.window)
        self.opcionalidadEntry.grid(column=1, row=4)

        Label(self.window, text="creditos", bg='#1B1F3B',
              fg="white").grid(column=0, row=5)
        self.creditosEntry = Entry(self.window)
        self.creditosEntry.grid(column=1, row=5)

        Label(self.window, text="estado", bg='#1B1F3B',
              fg="white").grid(column=0, row=6)
        self.estadoEntry = Entry(self.window)
        self.estadoEntry.grid(column=1, row=6)

        Button(self.window,
               text="Regresar",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               command=self.window.destroy).grid(column=1, row=7)

        Label(self.window, text="Codigo", bg='#1B1F3B',
              fg="white").grid(column=0, row=8)

        self.searchCodigoEntry = Entry(self.window)
        self.searchCodigoEntry.grid(column=1, row=8)

        Button(self.window,
               text="Buscar",
               pady=5,
               padx=10,
               bg="#0DCAF0",
               command=self.handleSearch).grid(column=1, row=9)
