# movies = [
#     ["The Shawshank Redemption", 1994, "Frank Darabont"],
#     ["The Godfather", 1972, "Francis Ford Coppola"],
#     ["The Dark Knight", 2008, "Christopher Nolan"],
#     ["12 Angry Men", 1957, "Sidney Lumet"],
#     ["Schindler's List", 1993, "Steven Spielberg"],
#     ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
# ]

# movie_to_change = "The Lord of the Rings: The Return of the King"
# new_movie = "The Lord of the Rings: The Fellowship of the Ring"
# new_year = 2001

# for movie in movies:
#     if movie[0] == movie_to_change:# establece una condición aquí
#         movie[0] = new_movie
#         movie[1] = new_year
        

# # no modifiques el código de abajo, ya que imprime el resultado
# for movie in movies:
#     print(movie)

"""
Code that increase salary of people and seniority level if its salary is above an specific threshold
name_to_update = "Alicia" (empleado a analizar)
salary_increase = 10.000 (valor en el que se incrementará su salario)
salary_threshold = 80.000 (límite para cambiar de rango, si el salario actualizado supera ese tope se deberá actualizar su rango)
new_seniority = "Senior" (nuevo rango a implementar si supera el tope salarial)
"""


employees = [['Alice', 75000, 'Desarrollador', 'Júnior'],
            ['Bob', 68000, 'Diseñador', 'Semi sénior'],
            ['Charlie', 78000, 'Desarrollador', 'Júnior'],
            ['David', 85000, 'Gerente', 'Sénior'],
            ['Eve', 80000, 'Desarrollador', 'Semi sénior']]

name_to_update = 'Alice'
salary_increase = 10000
salary_threshold = 80000
new_seniority = 'Senior'

for employee in employees:
    if employee[0] == name_to_update:
        employee[1] = employee[1] + salary_increase
        if employee[1] >= salary_threshold:
            employee[3] = new_seniority

print(employees)