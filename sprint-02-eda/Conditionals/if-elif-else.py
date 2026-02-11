# countries = ['France', 'Italy', 'New Zealand', 'Italy', 'France', 'USA']

# # empieza a escribir tu bucle for aquí
# for country in countries:
#     if country == 'USA':
#         print('The movie was released in the USA.')
#     elif country == 'France':
#         print('Le film est sorti en France.')
#     elif country == 'Italy':
#         print('Il film e stato rilasciato in Italia.')
#     else: print('Country not defined.')


"""
Sistema de rating
Parámetros:
Muestra mala si la calificación original se encuentra en un intervalo de 0 a 59 puntos,
Muestra buena si la calificación original se encuentra en un intervalo de 60 a 100 puntos.
"""


# ratings = [91, 35, 65, 89, 78, 93]

# for rating in ratings:
#     if rating <= 59:
#         print('mala')
#     else:
#         rating >59
#         print('buena')
    

"""
Clasificación de clientes en cuentas bancarias, según dinero dcepositado
Parámetros:

1- Cuenta Estándar para los clientes con ingresos entre $1 y $100.000.

2- Cuenta Plus para ingresos entre $100.001 y $200.000.

3- Cuenta Elite para ingresos entre $200.001 y $300.000.

4- Cuenta Executive para ingresos de $300.001 o más.
"""

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# listas vacías para agregar clientes
standard = []
plus = []
elite = []
executive = []

# escribe tu código aquí
for client in clients:
    income = client[3]
    if client[3] <= 100000:
        standard.append(client)
    elif 100001 <= income <= 200000:
        plus.append(client)
    elif 200001 <= income <= 300000:
        elite.append(client)
    else:
        executive.append(client)

print(executive)