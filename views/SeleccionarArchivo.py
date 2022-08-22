from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from data.Data import Data


class SeleccionarArchivo():

    window = None

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("700x110")
        self.window.title("Seleccionar archivo")
        self.window.config(bg='#1B1F3B')
        self.initUI()

    def launchFileExplorer(self):
        path = filedialog.askopenfilename(initialdir="./",
                                          title="Seleccionar achivo",
                                          filetypes=[("LFP files", "*.lfp"),
                                                     ("Csv files", "*.csv")])

        self.entryPath.delete(0, END)
        self.entryPath.insert(0, path)

    def loadFile(self):
        try:
            path = self.entryPath.get()

            if len(path) <= 0:
                messagebox.showwarning(title="Aviso",
                                       message="Debe introducir una ruta")
                return

            try:
                file = open(path, 'r', encoding="utf-8", errors='ignore')
                text = file.read()

                Data.cleanData()
                Data(text)
                file.close()

                if len(Data.warningMessagesList) > 0:
                    messagebox.showwarning(title="Advertencia",
                                           message=Data.warningMessages)

                if len(Data.headerErrors) > 0 or len(Data.globalrowErrors) > 0:
                    messagebox.showerror(title="Error",
                                         message=Data.errorMessages)
                else:
                    messagebox.showinfo(title="Informacion cargada",
                                        message="Informacion cargada")

                Data.cleanErrors()
            except:
                messagebox.showerror(title="Error",
                                     message="Error en la carga del archivo")

        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="Ruta incorrecta")
            return

    def initUI(self):

        textFont = ("Helvetica", 14, "bold")
        buttonFont = ("Helvetica", 12, "bold")

        Label(self.window,
              text="Ruta: ",
              font=textFont,
              fg='white',
              bg='#1B1F3B').grid(row=0, column=0)

        self.entryPath = Entry(self.window, width=80)
        self.entryPath.grid(row=0, column=1)

        Button(self.window,
               font=buttonFont,
               text="Cargar",
               pady=5,
               padx=10,
               bg="#198754",
               command=self.loadFile).grid(row=1, column=0, padx=5)
        Button(self.window,
               font=buttonFont,
               text="Abrir Explorador",
               pady=5,
               padx=10,
               bg="#0DCAF0",
               command=self.launchFileExplorer).grid(row=1, column=1, padx=5)
        Button(self.window,
               font=buttonFont,
               text="Regresar",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               command=self.window.destroy).grid(row=1, column=2, padx=5)
