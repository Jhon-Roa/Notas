import os

def menu ():
    os.system('cls')
    titulo = """
        ++++++++++++++++
        + MENU ALUMNOS +
        ++++++++++++++++
    """
    print(titulo)

    opciones = ['Añadir alumno', 'Borrar alumno por id', 'Borrar alumno por nombre', 'buscar alumno', 'Lista de alumnos', 'añadir notas', 'salir']
    for idx, item in enumerate(opciones):
        print(f'{idx+1}. {item}')
        
    try:
        op = int(input(':)_'))
    except ValueError:
        print('ingrese una opcion valida')
        os.system('pause')
    else:
        return op