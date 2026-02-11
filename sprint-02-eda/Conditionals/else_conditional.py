# """ Ejercicio 1: Usar el bloque "if/else" como filtro y
#  agregar resultados específicos a una nueva lista
#  """

# clients = [
#     [32456, "Jack Wilson", 32, 150000, "Healthcare"],
#     [34591, "Nina Brown", 45, 250000, "Telecom"],
#     [37512, "Alex Smith", 39, 210000, "IT"],
#     [39591, "Brian Perez", 29, 340000, "Transportation"],
#     [45123, "Sarah Lee", 28, 120000, "Marketing"],
#     [47635, "David Kim", 36, 180000, "Finance"],
#     [49571, "Samantha Chen", 42, 220000, "Retail"],
#     [50391, "Juan Rodriguez", 31, 160000, "Architecture"]
# ]

# elite_clients = [] # añade elite clients aquí

# for client in clients:
# 		if client[3] >= 200000:
# 			elite_clients.append(client)
# print(elite_clients)

"""Ejercicio 2: Crear una lista de clientes en 2 segmentos (Estandar y plus)"""

clients = [
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
neo = []
plus = []

for client in clients:
		if client[2]<=41:
			neo.append(client)
		else:
		    plus.append(client)

print(neo)