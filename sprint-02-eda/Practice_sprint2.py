items = 10

items += 5
print(items)

items -= 5
print(items)

items *= 5
print(items)

items //= 5
print(items)

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 126]

total_duration = sum(movies_duration) #Suma todos los elementos de la lista
max_duration = max(movies_duration) # Obtiene el elemento más grande en la lista
min_duration = min(movies_duration) # Obtiene el elemento más pequeño en la lista

print(f'La duración total de las películas es: {total_duration} minutos')
print(f'La película con mayor duración tiene un total de {max_duration} minutos')
print(f'La película con menor duración tiene un total de {min_duration} minutos')