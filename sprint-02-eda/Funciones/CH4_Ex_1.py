"""
Docstring for sprint-02-eda.Funciones.CH4_Ex_1
Code that filters a list of customers according to the customer's work area

Parameters:

client name & field

"""

clients_list = [
       [47635, "David Kim", 36, 180000, "Finance"],
        [49571, "Samantha Chen", 42, 220000, "Retail"],
        [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
        [34556, "Lucas Hernandez", 37, 75000, "Education"],
        [64291, "Jessica Li", 25, 125000, "IT"],
        [104556, "William Brown", 38, 289000, "Finance"],
        [105491, "Emily Smith", 29, 193000, "Healthcare"],
        [107512, "Michael Perez", 53, 415000, "Transportation"]]



# crea aquí tu función filter_clients. Usar la lista de clientes y el field como parámetros
def filter_clients(clients, field):
    field = 'Finance'
    filtered_clients = []
    for client in clients:
        if client[4] == field:
            filtered_clients.append(client)
    return filtered_clients
        

filtered_list = filter_clients(clients_list, 'Finance')

# muestra el resultado
print(filtered_list)