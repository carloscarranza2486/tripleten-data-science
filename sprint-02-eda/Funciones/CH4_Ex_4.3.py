# Diccionario global que representa los niveles de inventario actuales
inventory = {
    'manzana': 50,
    'plátano': 30,
    'naranja': 20
}

# Muestra el inventario inicial
print("Inventario inicial:", inventory)


# Función para quitar stock
def remove_stock(product, quantity):
    if product in inventory and quantity <= inventory[product]:
        inventory[product] -= quantity
        print(f'Se quita(n) {quantity} {product}(s). Nuevo inventario: {inventory[product]}')
    elif product in inventory and quantity > inventory[product]:
        print(f'Stock insuficiente de {product}. No se puede(n) quitar {quantity} {product}(s).')
    else:
        print(f'El producto {product} no existe en el inventario. No se puede quitar el stock.')
        


# Realiza operaciones de stock
remove_stock('plátano', 10)    # Quitar 10 plátanos
remove_stock('naranja', 25)    # Intentar quitar 25 naranjas
remove_stock('uva', 50)        # Quitar 50 uvas