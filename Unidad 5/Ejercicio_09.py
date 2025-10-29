
def celsius_a_fahrenheit(celsius):
    try:
        celsius = float(celsius)
    except (ValueError, TypeError):
        print("Error: La temperatura debe ser un número válido.")
        return None

    resultado = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {resultado} grados Fahrenheit.")
    return resultado