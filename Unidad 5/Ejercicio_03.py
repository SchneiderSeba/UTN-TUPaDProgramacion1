def informacion_personal(nombre, edad, apellido, residencia):
    if nombre.isdigit():
        print("Error: El nombre no puede ser un número.")
        return

    if apellido.isdigit():
        print("Error: El apellido no puede ser un número.")
        return

    if not edad.isdigit():
        print("Error: La edad debe ser un número.")
        return

    if residencia.isdigit():
        print("Error: El lugar de residencia no puede ser un número.")
        return

    nombre = str(nombre)
    apellido = str(apellido)
    edad = int(edad)
    residencia = str(residencia)

    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")