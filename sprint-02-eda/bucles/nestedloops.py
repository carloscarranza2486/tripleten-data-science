#Example 1:

movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

for row in movies_info:
    runtime = row[4]
    runtime /=60
    print(runtime)

# Exercise 1:

# Lista anidada de pedidos: [precio, cantidad, descuento]
orders = [
    [199.99, 2, 0.10],  # 10% de descuento
    [349.99, 1, 0.05],  # 5% de descuento
    [129.99, 3, 0.00],  # Sin descuento
    [499.99, 1, 0.20],  # 20% de descuento
    [249.99, 4, 0.15],  # 15% de descuento
]
# Inicializa las variables
total_revenue = 0
highest_order_value = 0
final_price = []

for order in orders:
    total_revenue += (order[0]*order[1])*(1-(order[2])) 
    final_price.append(order[0]*order[1]*(1-order[2]))
    highest_order_value = max(final_price)
    
print("Ingresos totales después de descuentos y tasas:", total_revenue) # Salida: Ingresos totales después de descuentos y tasas: 2332.4005
print("Valor de pedido único más alto:", highest_order_value)  # Salida: Valor de pedido único más alto: 849.966