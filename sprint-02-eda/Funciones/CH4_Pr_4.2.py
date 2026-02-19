"""
    Agrega un producto al inventario o actualiza la cantidad si ya existe.
    
    Parámetros:
    - product (str): Nombre del producto.
    - quantity (int): Cantidad a agregar.
    """

# Diccionario global que representa los niveles de inventario actuales
inventory = {
    'manzana': 50,
    'plátano': 30,
    'naranja': 20
}

# Muestra el inventario inicial
print("Inventario inicial:", inventory)

# Función para agregar stock
def add_stock(inventory, product, quantity):
    # Función pura que recibe el inventario como parámetro 
    if product in inventory:
        new_quantity = inventory[product] + quantity
        inventory[product] = new_quantity
        print(f"Se agrega(n) {quantity} {product}(s). Nuevo inventario: {new_quantity}")
    else:
        inventory[product] = quantity
        print(f"Se agrega el nuevo producto {product} con {quantity} unidades. Nuevo inventario: {quantity}")

# Realiza operaciones de stock
add_stock('manzana', 20)   # Agregar 20 manzanas
add_stock('kiwi', 30)      # Agregar 30 kiwis