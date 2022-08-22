from tkinter import *
from tkinter import messagebox

from utils.countCredits import countAllCreditsOfN, countGeneralCredits, countObligatoryCreditsToN


class ConteoCreditos():

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("450x290")
        self.window.config(bg='#1B1F3B')
        self.window.title("Conteo de creditos")
        self.initUI()

    def countToN(self):
        self.creditosObligatoriosHastaN.delete(0, END)

        try:
            semesterNumber = int(self.hastaSemestreNSpinbox.get())

            if semesterNumber <= 0 or semesterNumber > 10:
                messagebox.showerror(title="Error", message="Rango no valido")
                return

            self.creditosObligatoriosHastaN.insert(
                0, str(countObligatoryCreditsToN(semesterNumber)))
        except:
            messagebox.showerror(title="Error", message="Valor invalido")

    def countOfN(self):
        try:
            self.totalCreditosDeSemestre.delete(0, END)

            semesterNumber = int(self.semestreNSpinBox.get())

            if semesterNumber <= 0 or semesterNumber > 10:
                messagebox.showerror(title="Error", message="Rango no valido")
                return

            self.totalCreditosDeSemestre.insert(
                0, str(countAllCreditsOfN(semesterNumber)))
        except:
            messagebox.showerror(title="Error", message="Valor invalido")

    def loadGeneralData(self):

        generalCredits = countGeneralCredits()
        self.totalCreditosAprobados.delete(0, END)
        self.totalCreditosAprobados.insert(0, str(generalCredits['aprobados']))

        self.totalCreditosCursando.delete(0, END)
        self.totalCreditosCursando.insert(0, str(generalCredits['cursando']))

        self.totalCreditosPendientes.delete(0, END)
        self.totalCreditosPendientes.insert(0,
                                            str(generalCredits['pendientes']))

    def initUI(self):

        # * Generales
        Label(self.window, text="Creditos aprobados", bg='#1B1F3B',
              fg='white').grid(column=0, row=0)
        self.totalCreditosAprobados = Entry(self.window)
        self.totalCreditosAprobados.grid(column=1, row=0)

        Label(self.window, text="Creditos cursando", bg='#1B1F3B',
              fg='white').grid(column=0, row=1)
        self.totalCreditosCursando = Entry(self.window)
        self.totalCreditosCursando.grid(column=1, row=1)

        Label(self.window,
              text="Creditos pendientes",
              bg='#1B1F3B',
              fg='white').grid(column=0, row=2)
        self.totalCreditosPendientes = Entry(self.window)
        self.totalCreditosPendientes.grid(column=1, row=2)

        self.loadGeneralData()

        # * Conteo personalizado

        # * Hasta semestre N
        Label(self.window,
              text="Creditos obligatorios hasta semestre N: ",
              bg='#1B1F3B',
              fg='white').grid(column=0, row=3)
        self.creditosObligatoriosHastaN = Entry(self.window)
        self.creditosObligatoriosHastaN.grid(column=1, row=3)

        # * Controles
        Label(self.window, text="Semestre", bg='#1B1F3B',
              fg='white').grid(column=0, row=4)
        self.hastaSemestreNSpinbox = Spinbox(self.window, from_=1, to=10)
        self.hastaSemestreNSpinbox.grid(column=1, row=4)
        Button(self.window,
               text="Contar",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               fg="white",
               command=self.countToN).grid(column=2, row=4)

        # * De semestre especifico
        Label(self.window,
              text="Creditos del semestre: ",
              bg='#1B1F3B',
              fg='white').grid(column=0, row=5)
        self.totalCreditosDeSemestre = Entry(self.window)
        self.totalCreditosDeSemestre.grid(column=1, row=5)

        # * Controles
        Label(self.window, text="Semestre", bg='#1B1F3B',
              fg='white').grid(column=0, row=6)
        self.semestreNSpinBox = Spinbox(self.window, from_=1, to=10)
        self.semestreNSpinBox.grid(column=1, row=6)
        Button(self.window,
               text="Contar",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               fg="white",
               command=self.countOfN).grid(column=2, row=6)

        # * Regresar
        Button(self.window,
               text="Regresar",
               pady=5,
               padx=10,
               bg="#DC3545",
               fg="white",
               command=self.window.destroy).grid(column=2, row=7)
