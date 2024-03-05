import os
from tabulate import tabulate

def AddParciales(alumnos):
    addOther= True
    while addOther:
        id = str(input('ingresa la id a la que quieres añadir la nota del parcial :'))
        if id in alumnos:
            notaCorrecta = True
            while notaCorrecta:
                try:
                    notaTrue= True
                    while notaTrue:
                        nota = float(input('ingresa la nota del parcial :'))
                        if nota <= 100 and nota >= 0:
                            notaYes = nota
                            notaTrue = False
                        else:
                            print('ingrese una nota valida entre 1 y 100.')
                            os.system('pause')
                except ValueError:
                    print('valor invalido ')
                else:
                    notaCorrecta = False
            alumnos[id]['calificaciones']['parciales'].append(notaYes)
            
            notas = alumnos[id]['calificaciones']['parciales']
            promedioNotas = sum(notas)/len(notas)
            alumnos[id]['calificaciones']['promedios'].update({'promedioP' : promedioNotas})
            os.system('pause')
        else:
            print('el alumno no se encuentra')
            os.system('pause')
        addOther= input('desea agregar otra nota Si[S] No[ENTER] :')

def AddQuices(alumnos):
    addOther = True
    while addOther:
        id = str(input('Ingresa la ID a la que quieres añadir la nota del quizz: '))
        if id in alumnos:
            notaCorrecta = True
            while notaCorrecta:
                try:
                    notaTrue = True
                    while notaTrue:
                        nota = float(input('Ingresa la nota del quizz: '))
                        if 0 <= nota <= 100:
                            notaYes = nota
                            notaTrue = False
                        else:
                            print('Ingresa una nota válida entre 0 y 100.')
                            os.system('pause')
                except ValueError:
                    print('Valor inválido. Inténtalo de nuevo.')
                else:
                    notaCorrecta = False
            alumnos[id]['calificaciones']['quices'].append(notaYes)
            
            notas = alumnos[id]['calificaciones']['quices']
            promedioNotas = sum(notas) / len(notas)
            alumnos[id]['calificaciones']['promedios'].update({'promedioQu': promedioNotas})
            os.system('pause')
        else:
            print('El alumno no se encuentra')
            os.system('pause')
        addOther = input('¿Desea agregar otra nota? Si[S] No[ENTER]: ')

def AddTrabajos(alumnos):
    addOther = True
    while addOther:
        id = str(input('Ingresa la ID a la que quieres añadir la nota del trabajo: '))
        if id in alumnos:
            notaCorrecta = True
            while notaCorrecta:
                try:
                    notaTrue = True
                    while notaTrue:
                        nota = float(input('Ingresa la nota del trabajo: '))
                        if 0 <= nota <= 100:
                            notaYes = nota
                            notaTrue = False
                        else:
                            print('Ingresa una nota válida entre 0 y 100.')
                            os.system('pause')
                except ValueError:
                    print('Valor inválido. Inténtalo de nuevo.')
                else:
                    notaCorrecta = False
            alumnos[id]['calificaciones']['trabajos'].append(notaYes)
            
            notas = alumnos[id]['calificaciones']['trabajos']
            promedioNotas = sum(notas) / len(notas)
            alumnos[id]['calificaciones']['promedios'].update({'promedioT': promedioNotas})
            os.system('pause')
        else:
            print('El alumno no se encuentra')
            os.system('pause')
        addOther = input('¿Desea agregar otra nota? Si[S] No[ENTER]: ')


def TablaNotas(alumnos):
    info = []
    os.system('cls')

    for key, value in alumnos.items():
        onlyNotes = {
            'nombre': value['nombre'],
            'parciales': value['calificaciones']['parciales'],
            'quices': value['calificaciones']['quices'],
            'trabajos': value['calificaciones']['trabajos']
        }
        
        info.append(onlyNotes)

    print(tabulate(info, headers='keys', tablefmt='grid'))
    os.system('pause')
    
def TablaPromedios(alumnos):
    info= []
    os.system('cls')
    
    for key, value in alumnos.items():
        promedioD= ((value['calificaciones']['promedios']['promedioP'])+(value['calificaciones']['promedios']["promedioQu"])+(value['calificaciones']['promedios']['promedioT']))/3
        value['calificaciones']['promedios'].update({'promedioF': promedioD})
        onlyPromedios = {
            'nombre': value['nombre'],
            'parciales': value['calificaciones']['promedios']['promedioP'],
            'quices': value['calificaciones']['promedios']['promedioQu'],
            'trabajos': value['calificaciones']['promedios']['promedioT'],
            'total': value['calificaciones']['promedios']['promedioF']
        }
        info.append(onlyPromedios)
        info= sorted(info, key=lambda item: item['total'], reverse= True)
        
    print(tabulate(info, headers='keys', tablefmt='grid'))
    os.system('pause')