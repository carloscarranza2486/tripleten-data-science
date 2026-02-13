"""
Docstring for sprint-02-eda.Dicts.inventory_ctrl_exercise

Control de inventario en un diccionario anidado

Parámetros:
Precio, cantidad disponible, descuento
"""
products = {
    'Product_A': {'price': 10, 'quantity': 2, 'discount': 0.1},
    'Product_B': {'price': 20, 'quantity': 1, 'discount': 0.05},
    'Product_C': {'price': 15, 'quantity': 5, 'discount': 0.2},
}

# Paso 1: Inicializa la variable para almacenar el total
total_cost = 0

# Paso 2: Recorre cada producto
for product in products:
    # Accede al precio y a la cantidad
    price = products[product]['price']
    quantity = products[product]['quantity']

    # Paso 3: Calcula el ingreso por producto y acumúlalo
    individual_cost = price * quantity
    total_cost += individual_cost
    

# Paso 4: Muestra el resultado final
print(f"Ingresos totales: ${total_cost}")

