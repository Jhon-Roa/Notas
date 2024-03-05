from tabulate import tabulate
import os
alumno = {}

def AddStudent(alumnos:dict):
    os.system('cls')
    replace = True
    while replace:
        id = input('ingrese el id :')
        if id not in alumnos:
            replace = False
        elif id in alumnos:
            replace = bool(input('seguro que quieres reemplazar esta id No[N] o Si[ENTER]'))
    nombre = input('ingrese el nombre :')
    isEdadTrue = True
    while isEdadTrue:
        try:  
            edad = int(input(f'ingrese la edad de {nombre} :'))
        except ValueError:
            print('ingrese una edad valida')
        else:
            isEdadTrue = False
    email = input(f'ingrese el email de {nombre} :')
    alumno = {
    'id': id,
    'nombre': nombre,
    'edad': edad,
    'email': email,
    'calificaciones': {
        'parciales': [],
        'quices': [],
        'trabajos': [],
        'promedios': {
            'promedioP': 0.0,
            'promedioQu': 0.0,
            'promedioT': 0.0,
            'promedioF': 0.0
        }
    }
}
    alumnos.update({id:alumno})
    print(alumno)
    os.system('pause')

def SearchStudent(alumnos:dict):
    id = input('ingrese el numero de id del estudiantes')
    data = alumnos.get(id, False)
    if(type(data) == dict):
        print(data)
    elif(type(data) == bool) and (data == False):
        print('el estudiante no se encuentra resgistrado')

def ListData(alumnos:dict):
    info =[]
    os.system('cls')
    for key,value in alumnos.items():
        calificacionesNot = value.copy()
        del calificacionesNot['calificaciones']
        info.append(calificacionesNot)
    print(tabulate(info,headers="keys",tablefmt='grid'))
    os.system('pause')

def ValidateStudent(alumnos: dict, id)->bool:
    return bool(alumnos.get(id, ''))

def DelStudent(alumnos: dict):
    delAStudent = True
    while delAStudent:
        id = input('ingrese el nro id del estudiante :')
        if (ValidateStudent(alumnos,id)):
            alumnos.pop(id)
            delAStudent = False
            break
        else:
            print(f'el estudiante con id {id} no esta registrado')
            delAStudent = bool(input('deseas borrar un alumno? Si[S] o No[ENTER]'))

def DelByName(alumnos: dict):
    delAStudent = True
    while delAStudent:
        nombre = input('ingrese el nombre del estudiante :')
        for key, value in alumnos.items():
            if (nombre in value['nombre']):
                alumnos.pop(key) 
                delAStudent = False
                break
            else:
                print(f'el estudiante con nombre {nombre} no esta registrado')
                delAStudent = bool(input('deseas borrar un alumno? Si[S] o No[ENTER]'))
