import os

RUTA_ARCHIVO = "productos.txt"

PRODUCTOS_INICIALES = [
    ("Lapicera", 120.5, 30),
    ("Cuaderno", 250.0, 50),
    ("Regla", 45.0, 100),
]


def crear_archivo_inicial(ruta: str):

    if not os.path.exists(ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            for nombre, precio, cantidad in PRODUCTOS_INICIALES:
                f.write(f"{nombre},{precio},{cantidad}\n")


def leer_productos(ruta: str):
    productos = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")
                if len(partes) != 3:

                    print(f"Aviso: línea con formato inválido ignorada: {linea}")
                    continue
                nombre = partes[0].strip()
                try:
                    precio = float(partes[1])
                except ValueError:
                    print(f"Aviso: precio inválido en línea ignorada: {linea}")
                    continue
                try:
                    cantidad = int(float(partes[2]))
                except ValueError:
                    print(f"Aviso: cantidad inválida en línea ignorada: {linea}")
                    continue
                productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    except FileNotFoundError:

        return []
    return productos


def mostrar_productos(productos):

    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def agregar_producto_a_archivo(ruta: str, producto: dict):

    with open(ruta, "a", encoding="utf-8") as f:
        f.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")


def pedir_producto_usuario():

    entrada = input("Ingrese un producto (nombre,precio,cantidad) o ENTER para terminar: ").strip()
    if entrada == "":
        return None
    partes = [p.strip() for p in entrada.split(",")]
    if len(partes) != 3:
        print("Error: Debes ingresar exactamente 3 valores separados por comas.")
        return None
    nombre = partes[0]
    try:
        precio = float(partes[1])
    except ValueError:
        print("Error: precio inválido.")
        return None
    try:
        cantidad = int(float(partes[2]))
    except ValueError:
        print("Error: cantidad inválida.")
        return None
    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}


def buscar_producto(productos, nombre_buscar):

    nombre_buscar = nombre_buscar.strip().lower()
    resultados = [p for p in productos if p["nombre"].strip().lower() == nombre_buscar]
    return resultados


def guardar_productos(ruta: str, productos):

    with open(ruta, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")


def main():
    crear_archivo_inicial(RUTA_ARCHIVO)

    # 1 y 4. Leer y cargar en lista de diccionarios
    productos = leer_productos(RUTA_ARCHIVO)

    # 2. Mostrar productos
    print("\nProductos actuales:")
    mostrar_productos(productos)

    # 3. Agregar productos desde teclado (permite agregar varios hasta ENTER)
    print("\nAgregar productos. Para terminar deje la línea vacía y presione ENTER.")
    while True:
        nuevo = pedir_producto_usuario()
        if nuevo is None:
            break
        # Añadimos al archivo inmediatamente sin borrar contenido previo
        agregar_producto_a_archivo(RUTA_ARCHIVO, nuevo)
        # También actualizamos la lista en memoria
        productos.append(nuevo)
        print(f"Producto '{nuevo['nombre']}' agregado.")

    # 5. Buscar producto por nombre
    nombre_busqueda = input("\nIngrese el nombre de un producto para buscar (o ENTER para omitir): ").strip()
    if nombre_busqueda:
        encontrados = buscar_producto(productos, nombre_busqueda)
        if encontrados:
            print("\nCoincidencias encontradas:")
            for p in encontrados:
                print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        else:
            print("Error: producto no encontrado.")

    # 6. Guardar productos actualizados sobrescribiendo el archivo
    guardar_productos(RUTA_ARCHIVO, productos)
    print(f"\nCambios guardados en '{RUTA_ARCHIVO}'. Fin.")


if __name__ == "__main__":
    main()
