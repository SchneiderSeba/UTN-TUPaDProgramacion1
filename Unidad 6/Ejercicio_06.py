# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}

for _ in range(2):
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    nombre = input("Ingrese el nombre del alumno: ")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    primera = float(input("Ingrese la primera nota: "))
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    segunda = float(input("Ingrese la segunda nota: "))
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    tercera = float(input("Ingrese la tercera nota: "))
    notas = (primera, segunda, tercera)
    alumnos[nombre] = notas
print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
print("Promedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f"{nombre}: {promedio:.2f}")
