"""
Docstring for sprint-02-eda.Dicts.most_expensive

Calcular el producto más costoso de un diccionario de productos
Parámetros:
price, quantity, discount

"""
# Diccionario anidado que representa los productos
products = {
    'Product_A': {'price': 10, 'quantity': 2, 'discount': 0.1},
    'Product_B': {'price': 20, 'quantity': 1, 'discount': 0.05},
    'Product_C': {'price': 15, 'quantity': 5, 'discount': 0.2},
}

# Inicializa las variables
total_cost = 0
most_expensive_product = ""
highest_price = 0

# Calcula el costo total y encuentra el producto más caro
for product in products:
    # Accede a los detalles del producto
    price = products[product]['price']
    quantity = products[product]['quantity']

    # Calcula el costo de cada producto
    cost = price * quantity
    total_cost += cost

    # Comprueba si el producto actual es el más caro
    if price > highest_price:
        highest_price = price
        most_expensive_product = product
    
    
# Muestra los resultados
print(f"Ingresos totales: ${total_cost}")
print(f"Producto más caro: {most_expensive_product}")