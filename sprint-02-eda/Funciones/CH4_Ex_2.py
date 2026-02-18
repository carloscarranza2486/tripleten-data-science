"""
Docstring for sprint-02-eda.Funciones.CH4_Ex_2

Function that check if an specific book is available in the inventory

Parameters:


"""

# Inventario inicial
inventory = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"titulo": "La casa de los espíritus", "autor": "Isabel Allende", "disponible": True},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": False},
]


#1 Definir la función para verificar disponibilidad
def check_availability(titulo):
    available = False
    for dict in inventory:
        if dict["titulo"] == titulo and dict["disponible"] == True:
            available = True
            break
        elif dict["titulo"] == titulo and dict["disponible"] == False:
            available = False
            break
        else:
            dict["titulo"] != titulo
            available = None
    if available == True:
        print(f"'{titulo}' está disponible.")
    elif available == False:
        print(f"'{titulo}' no está disponible.")
    else: 
        print(f"'{titulo}' no está en el inventario.")
            
    #2 Crear un bucle para recorrer cada libro
    #3 Revisar si el libro está en el inventario y su estado es "disponible"
    #4 Imprimir la frase "'{titulo}' está disponible." si está disponible
    #5 Si no se encuentra, imprimir el mensaje {titulo}' no está en el inventario.


# Uso de la función
check_availability("Cien años de soledad")
check_availability("Pedro Páramo")
