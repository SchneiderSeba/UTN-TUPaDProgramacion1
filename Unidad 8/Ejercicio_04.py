def decimal_a_binario(n):
    # Caso base
    if n < 2:
        return str(n)
    # Caso recursivo
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingresa un número entero positivo: "))

if num < 0:
    print("El número debe ser positivo.")
else:
    binario = decimal_a_binario(num)
    print(f"El número {num} en binario es {binario}")
