
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    if division is None:
        print("División: Error (división por cero)")
    else:
        print(f"División: {division}")

    return (suma, resta, multiplicacion, division)