import Ejercicio_01, Ejercicio_02, Ejercicio_03, Ejercicio_04, Ejercicio_05, Ejercicio_06, Ejercicio_07, Ejercicio_08, Ejercicio_09, Ejercicio_10

while True:
    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
    print("Seleccione una opción:\n")
    print("1. Hola Mundo del Ejercicio 01")
    print("2. Saludo a usuario del Ejercicio 02")
    print("3. Información personal del Ejercicio 03")
    print("4. Cálculo del área del círculo del Ejercicio 04")
    print("5. Conversión de segundos a horas del Ejercicio 05")
    print("6. Tabla de multiplicar del Ejercicio 06")
    print("7. Operaciones básicas del Ejercicio 07")
    print("8. Cálculo del IMC del Ejercicio 08")
    print("9. Conversión de Celsius a Fahrenheit del Ejercicio 09")
    print("10. Cálculo del promedio del Ejercicio 10")
    print("0. Salir")
    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")

    opcion = input("Ingrese su opción: ")

    if opcion == "0":
        print("Saliendo...")
        break

    match opcion:
        case "1":
            # Hola Mundo del Ejercicio 01
            Ejercicio_01.imprimir_hola_mundo()
        case "2":
            # Saludo a usuario del Ejercicio 02
            nombre = input("Ingrese su nombre: ")
            Ejercicio_02.saludar_usuario(nombre)
        case "3":
            # Información personal del Ejercicio 03
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            edad = input("Ingrese su edad: ")
            residencia = input("Ingrese su lugar de residencia: ")
            Ejercicio_03.informacion_personal(nombre, edad, apellido, residencia)
        case "4":
            # Cálculo del área del círculo del Ejercicio 04
            radio = float(input("Ingrese el radio del círculo: "))
            Ejercicio_04.calcular_area_circulo(radio)
            Ejercicio_04.calcular_perimetro_circulo(radio)
        case "5":
            # Conversión de segundos a horas del Ejercicio 05
            segundos = int(input("Ingrese la cantidad de segundos: "))
            Ejercicio_05.segundos_a_horas(segundos)
        case "6":
            # Tabla de multiplicar del Ejercicio 06
            numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
            Ejercicio_06.tabla_multiplicar(numero)
        case "7":
            # Operaciones básicas del Ejercicio 07
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            Ejercicio_07.operaciones_basicas(a, b)
        case "8":
            # Cálculo del IMC del Ejercicio 08
            peso = input("Ingrese su peso en kg: ")
            altura = input("Ingrese su altura en metros: ")
            Ejercicio_08.calcular_imc(peso, altura)
        case "9":
            # Conversión de Celsius a Fahrenheit del Ejercicio 09
            celsius = input("Ingrese la temperatura en Celsius: ")
            Ejercicio_09.celsius_a_fahrenheit(celsius)
        case "10":
            # Cálculo del promedio del Ejercicio 10
            a = input("Ingrese el primer número: ")
            b = input("Ingrese el segundo número: ")
            c = input("Ingrese el tercer número: ")
            Ejercicio_10.calcular_promedio(a, b, c)
