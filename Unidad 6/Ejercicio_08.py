# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

inventario = {'Pantalones': 50, 'Remeras': 30, 'Zapatillas': 20}

def validation_producto(producto):
    try:
        producto = str(producto)
        return True
    except ValueError:
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("El producto no es válido, debe ingresar solo letras ❌")
        return False
def validation_cantidad(cantidad):
    try:
        cantidad = int(cantidad)
        return True
    except ValueError:
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("La cantidad no es válida, Solo debe ingresar Numeros ❌")
        return False

def consultar_stock(producto):
    validation_producto(producto)
    return inventario.get(producto, "Producto no encontrado en el inventario.") 
def agregar_stock(producto, cantidad):
    validation_producto(producto)
    validation_cantidad(cantidad)
    if producto in inventario:
        inventario[producto] += cantidad
        return f"Se han agregado {cantidad} unidades a {producto}. Nuevo stock: {inventario[producto]}"
    else:
        return "Producto no encontrado en el inventario. Usa 'agregar_nuevo_producto' para agregarlo."
def agregar_nuevo_producto(producto, cantidad):
    validation_producto(producto)
    validation_cantidad(cantidad)
    if producto not in inventario:
        inventario[producto] = cantidad
        return f"Se ha agregado el nuevo producto {producto} con {cantidad} unidades."
    else:
        return "El producto ya existe en el inventario."

while True:

    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("🔍 Control de Inventario Seleccione una Opciones:")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("1. Consultar stock")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("2. Agregar stock a un producto existente")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("3. Agregar un nuevo producto")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("4. Salir")

    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == '1':
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        producto = input("Ingrese el nombre del producto a consultar: ").capitalize()
        print(consultar_stock(producto), "✅")
    elif opcion == '2':
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        producto = input("Ingrese el nombre del producto al que desea agregar stock: ").capitalize()
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        print(agregar_stock(producto, cantidad) , "✅")
    elif opcion == '3':
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        producto = input("Ingrese el nombre del nuevo producto: ").capitalize()
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        cantidad = int(input("Ingrese la cantidad inicial: "))
        print(agregar_nuevo_producto(producto, cantidad) , "✅")
    elif opcion == '4':
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("Saliendo del programa. ☠️")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")