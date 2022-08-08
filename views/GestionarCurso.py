from tkinter import *
from views.AgregarCursos import AgregarCursos
from views.EditarCursos import EditarCursos
from views.EliminarCurso import EliminarCurso
from views.ListarCursos import ListarCursos


class GestionarCurso():

    window = None

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("400x250")
        self.window.title("Gestionar Cursos")
        self.initUI()

    def goToListarCursos(self):
        newWindow = ListarCursos(self.window)
        newWindow.window.grab_set()

    def goToAgregarCursos(self):
        newWindow = AgregarCursos(self.window)
        newWindow.window.grab_set()

    def goToEditarCursos(self):
        newWindow = EditarCursos(self.window)
        newWindow.window.grab_set()

    def goToEliminarCursos(self):
        newWindow = EliminarCurso(self.window)
        newWindow.window.grab_set()

    def initUI(self):

        buttonFont = ("Helvetica", 12, "bold")
        titleFont = ("Helvetica", 16, "bold")

        Label(self.window, text="Opciones:",
              pady=5, font=titleFont).pack(expand=1, fill=BOTH)

        Button(self.window, text="Listar cursos",
               pady=5, padx=10, bg="#0DCAF0", fg="white", font=buttonFont, command=self.goToListarCursos).pack(expand=1, fill=BOTH)

        Button(self.window, text="Agregar cursos",
               pady=5, padx=10, bg="#198754", fg="white", font=buttonFont, command=self.goToAgregarCursos).pack(expand=1, fill=BOTH)

        Button(self.window, text="Editar cursos",
               pady=5, padx=10, bg="#FFC107", fg="white", font=buttonFont, command=self.goToEditarCursos).pack(expand=1, fill=BOTH)

        Button(self.window, text="Eliminar cursos",
               pady=5, padx=10, bg="#DC3545", fg="white", font=buttonFont, command=self.goToEliminarCursos).pack(expand=1, fill=BOTH)

        Button(self.window, text="Regresar a menu principal",
               pady=5, padx=10, bg="#0D6EFD", fg="white", font=buttonFont, command=self.window.destroy).pack(expand=1, fill=BOTH)
