print("➖➖➖➖➖➖ Analizis de Ventas por Matriz ➖➖➖➖➖➖➖➖")

Matriz = [
    [1, 2, 3, 4, 5, 6, 7],
    [4, 5, 7, 7, 8, 9, 5],
    [7, 8, 9, 2, 8, 1, 9],
    [0, 1, 2, 3, 4, 5, 6]
]
#Filas Productos
#Columnas Dias

index_most_selled_product = -1
total_sell = -1

for i in range(len(Matriz)):
    product_total_sell = sum(Matriz[i])
    if product_total_sell > total_sell:
        total_sell = product_total_sell
        index_most_selled_product = i
    print(f"\nEl total vendido del Producto {i + 1} es: {product_total_sell}")

total_sell_per_day = 0
day_most_selled_index = -1

# necesito sumar los valores de cada columna para ver que dia fue el que se vendio mas
for j in range(len(Matriz[0])):
    day_total_sell = 0
    for i in range(len(Matriz)):
        day_total_sell += Matriz[i][j]
        
    if day_total_sell > total_sell_per_day:
        total_sell_per_day = day_total_sell
        day_most_selled_index = j
match day_most_selled_index:
    case 0:
        print(f"\nEl dia que mas se vendio fue el Lunes con un total de {total_sell_per_day} ventas")
    case 1:
        print(f"\nEl dia que mas se vendio fue el Martes con un total de {total_sell_per_day} ventas")
    case 2:
        print(f"\nEl dia que mas se vendio fue el Miercoles con un total de {total_sell_per_day} ventas")
    case 3:
        print(f"\nEl dia que mas se vendio fue el Jueves con un total de {total_sell_per_day} ventas")
    case 4:
        print(f"\nEl dia que mas se vendio fue el Viernes con un total de {total_sell_per_day} ventas")
    case 5:
        print(f"\nEl dia que mas se vendio fue el Sabado con un total de {total_sell_per_day} ventas")
    case 6:
        print(f"\nEl dia que mas se vendio fue el Domingo con un total de {total_sell_per_day} ventas")

    # print(f"\nEl total vendido del Dia {j + 1} es: {day_total_sell}")
    
print(f"\nEl Producto {index_most_selled_product + 1} es el mas vendido con un total de {total_sell} ventas")

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")