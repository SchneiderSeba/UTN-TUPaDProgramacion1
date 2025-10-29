
def calcular_promedio(a, b, c):

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (ValueError, TypeError):
        print("Error: Todos los valores deben ser números válidos.")
        return None

    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c} es: {promedio}")
    return promedio