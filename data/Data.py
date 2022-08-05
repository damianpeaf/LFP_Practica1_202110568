
from data.RowData import RowData


class Data():

    headerErrors = []
    globalrowErrors = []
    warningMessagesList = []
    errorMessages = ""
    warningMessages = ""
    data = []

    def __init__(self, textFromFile):

        self.headerErrors = []
        self.globalrowErrors = []
        self.warningMessagesList = []

        # * Recibe el texto en crudo

        rowsInList = textFromFile.split("\n")

        rowNumber = 1
        for rowWithCommas in rowsInList:
            row = self.createRow(rowWithCommas, rowNumber)
            if(row):
                self.addRowToData(row)
            rowNumber += 1

        self.generateErrorsAndWarning()

    def addRowToData(self, newRow):
        if len(newRow.errores['list']) > 0:
            self.globalrowErrors.append(newRow.errores)
        else:
            rowIndex = 0
            for rowInData in Data.data:
                if rowInData.codigo == newRow.codigo:
                    self.warningMessagesList.append(
                        'Fila ' + str(rowIndex+1) + " sobreescrita por la fila " + str(newRow.rowNumber))
                    newRow.rowNumber = (rowIndex+1)
                    Data.data[rowIndex] = newRow
                    return
                rowIndex += 1
            Data.data.append(newRow)

    def generateErrorsAndWarning(self):

        self.cleanErrors()
        Data.errorMessages += " Errores de Cabecera: \n\n"

        for headerError in self.headerErrors:
            Data.errorMessages += headerError['msg'] + "\n"

        Data.errorMessages += "\n\nErrores de filas: \n\n"

        for rowError in self.globalrowErrors:
            Data.errorMessages += "Errores en la fila: " + \
                str(rowError['rowNumber']) + "\n"
            for rowErrorList in rowError['list']:
                Data.errorMessages += "-parametro: " + \
                    rowErrorList['param'] + "\n" + \
                    "--Mensaje: " + rowErrorList['msg'] + "\n\n"
        # print(Data.errorMessages)

        Data.warningMessages += "Advertencias: \n\n"
        for waringMessage in self.warningMessagesList:
            Data.warningMessages += waringMessage + "\n"
        # print(Data.warningMessages)

    def cleanErrors(self):
        Data.errorMessages = ""
        Data.warningMessages = ""

    @staticmethod
    def cleanData():
        Data.data = []

    def createRow(self, rowWithCommas, rowNumber):
        row = rowWithCommas.split(',')
        try:
            # self, rowNumber, codigo, nombre, prerrequisitos, obligatorio, semestre, creditos, estado
            codigo = row[0]
            nombre = row[1]
            prerrequisitos = row[2]
            obligatorio = row[3]
            semestre = row[4]
            creditos = row[5]
            estado = row[6]

            return RowData(rowNumber, codigo, nombre, prerrequisitos, obligatorio, semestre, creditos, estado)

        except IndexError:
            self.headerErrors.append({
                'rowNumber': rowNumber,
                'msg': 'Hace falta un dato en la fila ' + str(rowNumber)
            })
            return None
