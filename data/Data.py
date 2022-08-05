
from data.RowData import RowData


class Data():
    errorMessages = ""
    warningMessages = ""
    data = []
    headerErrors = []
    globalrowErrors = []
    warningMessagesList = []

    def __init__(self, textFromFile):

        Data.headerErrors = []
        Data.globalrowErrors = []
        Data.warningMessagesList = []

        rowsInList = textFromFile.split("\n")

        rowNumber = 1
        for rowWithCommas in rowsInList:
            row = Data.createRow(rowWithCommas, rowNumber)
            if(row):
                Data.addRowToData(row)
            rowNumber += 1

        Data.generateErrorsAndWarning()

    @staticmethod
    def addRowToData(newRow):
        if len(newRow.errores['list']) > 0:
            Data.globalrowErrors.append(newRow.errores)
        else:
            rowIndex = 0
            for rowInData in Data.data:
                if rowInData.codigo == newRow.codigo:
                    Data.warningMessagesList.append(
                        'Fila ' + str(rowIndex+1) + " sobreescrita por la fila " + str(newRow.rowNumber))
                    newRow.rowNumber = (rowIndex+1)
                    Data.data[rowIndex] = newRow
                    return
                rowIndex += 1
            Data.data.append(newRow)

    @staticmethod
    def generateErrorsAndWarning():

        Data.errorMessages = ""
        Data.warningMessages = ""

        Data.errorMessages += " Errores de Cabecera: \n\n"

        for headerError in Data.headerErrors:
            Data.errorMessages += headerError['msg'] + "\n"

        Data.errorMessages += "\n\nErrores de filas: \n\n"

        for rowError in Data.globalrowErrors:
            Data.errorMessages += "Errores en la fila: " + \
                str(rowError['rowNumber']) + "\n"
            for rowErrorList in rowError['list']:
                Data.errorMessages += "-parametro: " + \
                    rowErrorList['param'] + "\n" + \
                    "--Mensaje: " + rowErrorList['msg'] + "\n\n"

        Data.warningMessages += "Advertencias: \n\n"
        for waringMessage in Data.warningMessagesList:
            Data.warningMessages += waringMessage + "\n"

    @staticmethod
    def cleanErrors():
        Data.errorMessages = ""
        Data.warningMessages = ""
        Data.headerErrors = []
        Data.globalrowErrors = []
        Data.warningMessagesList = []

    @staticmethod
    def cleanData():
        Data.data = []

    @staticmethod
    def createRow(rowWithCommas, rowNumber):
        row = rowWithCommas.split(',')
        try:
            codigo = row[0]
            nombre = row[1]
            prerrequisitos = row[2]
            obligatorio = row[3]
            semestre = row[4]
            creditos = row[5]
            estado = row[6]

            return RowData(rowNumber, codigo, nombre, prerrequisitos, obligatorio, semestre, creditos, estado)

        except IndexError:
            Data.headerErrors.append({
                'rowNumber': rowNumber,
                'msg': 'Hace falta un dato en la fila ' + str(rowNumber)
            })
            return None
