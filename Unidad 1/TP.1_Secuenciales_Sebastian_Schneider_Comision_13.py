import math

# Ejercicio 1

print("--- Hola Mundo ---")

HOLA_MUNDO = "Hola Mundo !"
print(HOLA_MUNDO)

# Ejercicio 2

print("--- Saludo Personalizado ---")

USER_NAME = input("Ingrese su nombre: ")
print(f"Hola {USER_NAME}!")

# Ejercicio 3

print("--- Presentación con Datos---")

NAME_USER = input("Ingrese su nombre: ")

LAST_NAME_USER = input("Ingrese su apellido: ")

AGE_USER = input("Ingrese su edad: ")

RESIDENCE_USER = input("Ingrese su lugar de residencia: ")

print(f"Hola Soy {NAME_USER} {LAST_NAME_USER}, tengo {AGE_USER} años y vivo en {RESIDENCE_USER}.")

# Ejercicio 4

print("--- Area y Perimetro de un Circulo ---")
RADIUS = float(input("Ingrese el valor del Radio: "))

PERIMETER_CIRCULO = 2 * math.pi * RADIUS

AREA_CIRCULO = math.pi * RADIUS ** 2

print(f"El perímetro del círculo es: {PERIMETER_CIRCULO} y el área es: {AREA_CIRCULO}")

# Ejercicio 5

print("--- Segundos a Horas ---")

SECONDS = int(input("Ingrese la cantidad de segundos: "))

HOURS = SECONDS / 3600

print(f"{SECONDS} segundos son {HOURS} horas")

# Ejercicio 6

print(" --- Tabla de Multiplicar ---")

NUMBER_TABLE = int(input("Ingrese el Numero de la tabla de multiplicar que quiere ver : "))

for i in range(1, 11):
    print(f"{NUMBER_TABLE} x {i} = {NUMBER_TABLE * i}")

# Ejercicio 7

print("--- Calculadora Simple ---")

NUM_1 = int(input("Ingrese el primer número: "))
OPERATION = input("Ingrese la operación (+, -, *, /): ")
NUM_2 = int(input("Ingrese el segundo número: "))

match OPERATION:
    case "+":
        RESULT = NUM_1 + NUM_2
    case "-":
        RESULT = NUM_1 - NUM_2
    case "*":
        RESULT = NUM_1 * NUM_2
    case "/":
        RESULT = NUM_1 / NUM_2
    case _:
        RESULT = "Operación no válida"

print(f"El resultado es: {RESULT}")

# Ejercicio 8

print("--- Calculadora de IMC ---")

WEIGHT = float(input("Ingrese su peso en kg: "))
HEIGHT = float(input("Ingrese su altura en metros: "))

IMC = WEIGHT / (HEIGHT ** 2)

print(f"Su IMC es: {IMC}")

# Ejercicio 9

print(" --- Calculadora de Celsius a Fahrenheit ---")

CELSIUS = float(input("Ingrese la temperatura en grados Celsius: "))

FAHRENHEIT = (CELSIUS * 9/5) + 32

print(f"Temperatura en Fahrenheit: {FAHRENHEIT}")

# Ejercicio 10

print("--- Promedio ---")
NUM_1 = float(input("Ingrese el primer número: "))
NUM_2 = float(input("Ingrese el segundo número: "))
NUM_3 = float(input("Ingrese el tercer número: "))

AVERAGE = (NUM_1 + NUM_2 + NUM_3) / 3

print(f"El promedio es: {AVERAGE}")

