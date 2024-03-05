import os

def menu():
    os.system('cls')
    titulo= """
        ++++++++++++++
        + MENU NOTAS +
        ++++++++++++++
    """
    print(str(titulo))
    
    opciones = ['Añadir nota en parciales', 'añadir nota en quices', 'añadir nota en trabajos', 'ver lista de notas', 'ver lista de notas(promedio)', 'salir']
    for idx, items in enumerate(opciones):
        print(str(f'{idx+1}. {items}'))
    
    try:
        op = int(input(':)_'))
    except ValueError:
        print('ingrese una opcion valida')
        os.system('pause')
    else:
        return op 