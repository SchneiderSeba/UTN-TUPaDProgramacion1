def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    # Caso recursivo
    return base * potencia(base, exponente - 1)

base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente (entero no negativo): "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")
