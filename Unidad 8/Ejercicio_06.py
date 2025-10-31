def suma_digitos(n):
    # Caso base
    if n < 10:
        return n
    # Caso recursivo
    return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingresa un número entero positivo: "))

if num < 0:
    print("El número debe ser positivo.")
else:
    resultado = suma_digitos(num)
    print(f"La suma de los dígitos de {num} es {resultado}")