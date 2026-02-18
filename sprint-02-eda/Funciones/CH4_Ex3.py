# Inventario inicial
inventory = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"titulo": "La casa de los espíritus", "autor": "Isabel Allende", "disponible": True},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": False},
]

#1 Definir la función para agregar un libro
def add_book(titulo, autor, disponible):
    new_book = {
        'titulo': titulo,
        'autor': autor,
        'disponible': True
    }
    inventory.append(new_book)
    #2 Crear un diccionario que contenga los datos del libro
    #3 Agregar el nuevo libro al inventario con append()

#4 Definir la función para verificar disponibilidad
def check_availability(titulo):
    available = False
    for book in inventory:
        #5 Revisar si el libro está en el inventario y disponible
        if book["titulo"] == titulo and book["disponible"]:
            available = True
            break
               #6 Si no se encuentra, imprimir el mensaje de no disponibilidad
    if available:
        print(f"'{titulo}' está disponible.")
    else:
        print(f"'{titulo}' no está disponible")

# Uso de las funciones
add_book("Pedro Páramo", "Juan Rulfo", disponible=True)
check_availability("Pedro Páramo")
