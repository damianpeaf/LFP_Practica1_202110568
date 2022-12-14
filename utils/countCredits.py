from data.Data import Data


def countGeneralCredits():

    aprobados = 0
    cursando = 0
    pendientes = 0
    for row in Data.data:

        estado = row.estado['number']
        opcionalidad = row.obligatorio['number']
        creditos = row.creditos

        if estado == -1 and opcionalidad == 1:
            pendientes += creditos
        elif estado == 1:
            cursando += creditos
        elif estado == 0:
            aprobados += creditos

    return {
        "aprobados": aprobados,
        "cursando": cursando,
        "pendientes": pendientes
    }


def countObligatoryCreditsToN(semesterNumber):
    creditos = 0
    try:
        for row in Data.data:
            if row.semestre <= int(semesterNumber):
                if row.obligatorio['number'] == 1:
                    creditos += row.creditos
    except:
        pass

    return creditos


def countAllCreditsOfN(semesterNumber):
    creditos = 0

    try:
        for row in Data.data:
            if row.semestre == int(semesterNumber):
                creditos += row.creditos
    except:
        pass

    return creditos
