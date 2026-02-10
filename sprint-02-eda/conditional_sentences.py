# Función que valida si una condición se cumple
movie_info = ['Fight club', 'USA', 1999, 'thrille, crime', 139, 8.644]
#print(movie_info[2] > 1996 and movie_info[2] < 1998)
# Función que valida si una condición NO se cumple
movie_info = ['Fight club', 'USA', 1999, 'thrille, crime', 139, 8.644]
print(not(movie_info[2] > 1996 and movie_info[2] < 1998))

# Función de predicado: Devuelve "True" or "False"
"""
- islower(): Devuelve True si todos los caracteres alfabéticos del string están en minúsculas
- isdigit():Devuelve True si todos los caracteres del string contiene solo números
- isalpha(): Devuelve True si un string contiene solo letras
"""

print('hola'.islower())
print('777'.isdigit())
print('La cadena contiene espacios, así como signos de puntuación.'.isalpha())

# Ejercicio 1

text_entries = ['Hola', 'hola', '1234', "hola1234"]  # Lista de entradas de texto
for text in text_entries:
    print(f"Texto '{text}':") 
    # Comprueba si el texto solo contiene caracteres alfabéticos
    condicion_1 = (text.isalpha())
    print("Solo contiene alfabeto", condicion_1)
    # Comprueba si el texto contiene solo letras en minúscula
    condicion_2 = text.islower()
    print("Solo contiene minúsculas", condicion_2 )
    # Comprueba si el texto contiene solo dígitos
    condicion_3 = text.isdigit()
    print("Solo contiene dígitos", condicion_3)