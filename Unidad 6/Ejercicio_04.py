# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

guia_telefonica = {}

print("➖➖➖➖➖➖➖➖➖➖➖➖➖")

for _ in range(2):
    nombre = input("Ingrese el nombre: ").lower()
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    telefono = int(input("Ingrese el número de teléfono: "))
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    guia_telefonica[nombre] = telefono

name_to_search = input("Ingrese un Nombre para ver su Numero Telefonico...").lower()
print("➖➖➖➖➖➖➖➖➖➖➖➖➖")

if name_to_search in guia_telefonica:
    print("El número de teléfono de", name_to_search.capitalize(), "es:", guia_telefonica[name_to_search])
else:
    print("No se encontró el nombre en la guía telefónica.")

print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
