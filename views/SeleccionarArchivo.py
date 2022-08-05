from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from data.Data import Data


class SeleccionarArchivo():

    window = None

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("700x110")
        self.window.title("Gestionar Cursos")
        self.initUI()

    def launchFileExplorer(self):
        path = filedialog.askopenfilename(
            initialdir="./", title="Seleccionar achivo", filetypes=[("Text files", "*.lfp")])

        self.entryPath.delete(0, END)
        self.entryPath.insert(0, path)

    def loadFile(self):
        try:
            path = self.entryPath.get()

            if len(path) <= 0:
                messagebox.showwarning(
                    title="Aviso", message="Debe introducir una ruta")
                return

            file = open(path, 'r')
            text = file.read()

            Data.cleanData()
            dataObject = Data(text)
            # print(Data.warningMessages)

            if len(dataObject.warningMessagesList) > 0:
                messagebox.showwarning(
                    title="Advertencia", message=Data.warningMessages)

            if len(dataObject.headerErrors) > 0 or len(dataObject.globalrowErrors) > 0:
                messagebox.showerror(
                    title="Error", message=Data.errorMessages)
            else:
                messagebox.showinfo(
                    title="Informacion cargada", message="Informacion cargada")

        except FileNotFoundError:
            messagebox.showwarning(
                title="Error", message="Ruta incorrecta")
            return

    def initUI(self):

        textFont = ("Helvetica", 14, "bold")
        buttonFont = ("Helvetica", 12, "bold")

        Label(self.window, text="Ruta: ",
              font=textFont).grid(row=0, column=0)

        self.entryPath = Entry(
            self.window, width=80)
        self.entryPath.grid(row=0, column=1)

        Button(self.window, font=buttonFont, text="Cargar",
               pady=5, padx=10, bg="#198754", command=self.loadFile).grid(row=1, column=0, padx=5)
        Button(self.window, font=buttonFont, text="Abrir Explorador",
               pady=5, padx=10, bg="#0DCAF0", command=self.launchFileExplorer).grid(row=1, column=1, padx=5)
        Button(self.window, font=buttonFont, text="Regresar",
               pady=5, padx=10, bg="#0D6EFD", command=self.window.destroy).grid(row=1, column=2, padx=5)
