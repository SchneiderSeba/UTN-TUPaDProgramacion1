print("➖➖➖➖➖➖ Matriz de Temp , Promedio ➖➖➖➖➖➖➖➖")

Matriz_7x2 = [
    [10.5, 16.2],
    [9.1, 14.3],
    [12.0, 16.3],
    [8.6, 18.0],
    [9.0, 10.9],
    [11.1, 12.5],
    [7.5, 14.0]
]

print(f"\nMatriz Original: {Matriz_7x2} ")

minimun_value_avg = 0
maximun_value_avg = 0
max_range_value = 0
max_range_row_index = 0
max_range_found = False

for index, row in enumerate(Matriz_7x2):
    maximun_value_row = max(row)
    minimun_value_row = min(row)
    range_value = maximun_value_row - minimun_value_row

    maximun_value_avg += maximun_value_row
    minimun_value_avg += minimun_value_row

    if range_value > max_range_value:
        max_range_value = range_value
        max_range_row_index = index
        max_range_found = True

print(f"Promedio Maximo : {maximun_value_avg / len(Matriz_7x2)}")
print(f"Promedio Minimo : {minimun_value_avg / len(Matriz_7x2)}")
print(f"Rango Maximo : {max_range_value}")

if max_range_found:
    match max_range_row_index:
        case 0:
            print("El rango maximo se encuentra en el dia Lunes")
        case 1:
            print("El rango maximo se encuentra en el dia Martes")
        case 2:
            print("El rango maximo se encuentra en el dia Miercoles")
        case 3:
            print("El rango maximo se encuentra en el dia Jueves")
        case 4:
            print("El rango maximo se encuentra en el dia Viernes")
        case 5:
            print("El rango maximo se encuentra en el dia Sabado")
        case 6:
            print("El rango maximo se encuentra en el dia Domingo")

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")