from tkinter import *
from tkinter import ttk

from data.Data import Data


class ListarCursos():

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("825x800")
        self.window.title("Listar Cursos")
        self.initUI()

    def initUI(self):
        self.table = ttk.Treeview(self.window, height=35)
        self.table['columns'] = ('codigo', 'nombre', 'prerrequisitos',
                                 'opcionalidad', 'semestre', 'creditos', 'estado')

        self.table.column('#0', width=0, stretch=NO)
        self.table.column("codigo", anchor=CENTER, width=80)
        self.table.column("nombre", anchor=CENTER, width=160)
        self.table.column("prerrequisitos", anchor=CENTER, width=80)
        self.table.column("opcionalidad", anchor=CENTER, width=160)
        self.table.column("semestre", anchor=CENTER, width=80)
        self.table.column("creditos", anchor=CENTER, width=80)
        self.table.column("estado", anchor=CENTER, width=160)

        self.table.heading("#0", text="", anchor=CENTER)
        self.table.heading("codigo", text="Código", anchor=CENTER)
        self.table.heading("nombre", text="Nombre", anchor=CENTER)
        self.table.heading(
            "prerrequisitos", text="Prerrequisitos", anchor=CENTER)
        self.table.heading("opcionalidad", text="Opcionalidad", anchor=CENTER)
        self.table.heading("semestre", text="Semestre", anchor=CENTER)
        self.table.heading("creditos", text="Créditos", anchor=CENTER)
        self.table.heading("estado", text="Estado", anchor=CENTER)

        self.loadData()
        self.table.pack(fill=BOTH)

        Button(self.window, text="Regresar",
               pady=5, padx=10, bg="#0D6EFD", command=self.window.destroy).pack()

    def loadData(self):
        for row in Data.data:
            codigo = str(row.codigo)
            nombre = row.nombre

            prerrequisitos = " "

            if row.prerrequisitos:
                prerrequisitos = '; '.join(str(e) for e in row.prerrequisitos)

            obligatorio = str(
                row.obligatorio['number']) + ": " + row.obligatorio['name']
            semestre = str(row.semestre)
            creditos = str(row.creditos)

            estado = str(
                row.estado['number']) + ": " + row.estado['name']

            rowNumber = row.rowNumber - 1
            self.table.insert(parent='', index='end', iid=rowNumber, text='', values=(
                codigo, nombre, prerrequisitos, obligatorio, semestre, creditos, estado))
