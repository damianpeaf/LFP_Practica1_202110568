class RowData():

    def __init__(self, rowNumber, codigo, nombre, prerrequisitos, obligatorio,
                 semestre, creditos, estado):

        self.errores = {'rowNumber': None, 'list': []}
        self.rowNumber = rowNumber
        self.errores['rowNumber'] = self.rowNumber
        self.setCodigo(codigo)
        self.setNombre(nombre)
        self.setPrerrequisitos(prerrequisitos)
        self.setObligatorio(obligatorio)
        self.setSemestre(semestre)
        self.setCreditos(creditos)
        self.setEstado(estado)
        # ? raise exception if errores is not empty

    def setCodigo(self, value):
        try:
            self.codigo = int(value)
        except ValueError:
            self.errores['list'].append({
                'param': 'codigo',
                'msg': 'El codigo debe ser un entero',
            })

    def setNombre(self, value):
        try:
            self.nombre = str(value)
        except ValueError:
            self.errores['list'].append({
                'param':
                'nombre',
                'msg':
                'El nombre debe ser una cadena de text',
            })

    def setPrerrequisitos(self, values):
        posicion = 0
        try:

            if (str(values).strip() == ""):
                self.prerrequisitos = None
                return

            self.prerrequisitos = []
            values = str(values).split(";")

            for value in values:
                posicion += 1
                self.prerrequisitos.append(int(value))
        except Exception as e:
            self.errores['list'].append({
                'param': 'prerrequisitos',
                'msg': 'El prerrequisito debe ser un numero',
                'posicion': posicion,
            })

    def setObligatorio(self, value):
        validValues = [0, 1]
        dictionaryValues = [{
            'number': 1,
            'name': 'obligatorio'
        }, {
            'number': 0,
            'name': 'opcional'
        }]
        try:
            posibleValue = int(value)

            if posibleValue not in validValues:
                self.errores['list'].append({
                    'param':
                    'obligatorio',
                    'msg':
                    'El parametro obligatorio debe estar contenido dentro de los valores '
                    + ' o '.join(str(e) for e in validValues),
                })
            else:
                for dict in dictionaryValues:
                    if dict['number'] == posibleValue:
                        self.obligatorio = dict
        except ValueError:
            self.errores['list'].append({
                'param':
                'obligatorio',
                'msg':
                'El parametro obligatorio debe ser un entero',
            })

    def setSemestre(self, value):
        try:
            self.semestre = int(value)
        except ValueError:
            self.errores['list'].append({
                'param':
                'semestre',
                'msg':
                'El semestre debe ser un entero',
            })

    def setCreditos(self, value):
        try:
            self.creditos = int(value)
        except ValueError:
            self.errores['list'].append({
                'param':
                'creditos',
                'msg':
                'Los creditos deben de un numero entero',
            })

    def setEstado(self, value):
        validValues = [0, 1, -1]
        dictionaryValues = [{
            'number': -1,
            'name': 'pendiente'
        }, {
            'number': 1,
            'name': 'cursando'
        }, {
            'number': 0,
            'name': 'aprobado'
        }]
        try:
            posibleValue = int(value)

            if posibleValue not in validValues:
                self.errores['list'].append({
                    'param':
                    'estado',
                    'msg':
                    'El parametro estado debe estar contenido dentro de los valores '
                    + ' o '.join(str(e) for e in validValues),
                })
            else:
                for dict in dictionaryValues:
                    if dict['number'] == posibleValue:
                        self.estado = dict
                        return

        except ValueError:
            self.errores['list'].append({
                'param':
                'estado',
                'msg':
                'El estado obligatorio debe ser un entero',
            })

    def updateRow(self, nombre, prerrequisitos, obligatorio, semestre,
                  creditos, estado):
        self.errores = {'rowNumber': None, 'list': []}

        self.setNombre(nombre)
        self.setPrerrequisitos(prerrequisitos)
        self.setObligatorio(obligatorio)
        self.setSemestre(semestre)
        self.setCreditos(creditos)
        self.setEstado(estado)

        return self.errores['list']
