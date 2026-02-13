# # Traditional manner of print each elemnt of a list 

# film_genres = ['scifi', 'Drama', 'thriller', 'comedy', 'action']

# print(film_genres[0])
# print(film_genres[1])
# print(film_genres[2])
# print(film_genres[3])
# print(film_genres[4])

# # For loop to optimize impresion of elements in a list

# print('-------------------------------')

# for value in film_genres:
#     print(value)


# Practice
'''
Los departamentos de seguridad del banco no quedaron satisfechos con la forma en la que presentamos la lista de clientes la última vez. Esta vez nos pidieron que proporcionáramos los nombres completos de los clientes imprimiendo cada nombre en una línea separada.
Haz un bucle en la lista de clientes y muestra sus nombres. No es necesario que hagas cambios en el string, solo muestra la lista.

'''

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],]

for client in clients: # Defined variable go through each item on the list
    print(client[1]) # Prints only the index number 1 of each list in the matrix

