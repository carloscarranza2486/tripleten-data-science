# esta función muestra la tabla filtrada. No modificar
def print_movie_info(data):
    for movie in data:
        print(movie)

# Utiliza como referencia la función que definiste en el ejercicio anterior.
# Renombra la funcion y realiza los ajustes necesarios para crear filter_by_year() 
def filter_by_timing(data, target_duration): 
    filtered_result = []
    for row in data:
        if row[4] > target_duration: # Pista: aquí debes cambiar el elemento de la fila que comparas
            filtered_result.append(row)
    return filtered_result 

def filter_by_year(data, year): # Creamos función que recibe parámetros data (una lista de listas) y un año (un número entero)
    filtered_years = [] # Creamos lista para almacenar resultados filtrados
    for row in data: # iteramos en las filas de la tabla (cada fila es una lista)
        if row[2] > year: # Comparamos el elemento de la fila que corresponde al año (en este caso, el índice 2) con el año objetivo
            filtered_years.append(row) # Agregamos la fila a la lista de resultados filtrados si cumple la condición
    return filtered_years    # Retornamos la lista de resultados filtrados

    
movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

# A continuación tienes dos llamadas a funciones: una para filtrar y otra para mostrar el resultado en pantalla
movies_filtered = filter_by_year(movies_info, 1990)
print_movie_info(movies_filtered)