def contar_bloques(n):
    # Caso base
    if n == 1:
        return 1
    # Caso recursivo
    return n + contar_bloques(n - 1)

niveles = int(input("Ingresa la cantidad de bloques en el nivel más bajo: "))

if niveles < 1:
    print("Debe ser un número entero positivo.")
else:
    total = contar_bloques(niveles)
    print(f"Se necesitan {total} bloques en total para construir la pirámide.")