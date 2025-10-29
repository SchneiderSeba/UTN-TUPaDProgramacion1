# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevodiccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores

original = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago'}

nuevo_diccionario = {value: key for key, value in original.items()}

print("Diccionario original:", original)
print("Nuevo diccionario:", nuevo_diccionario)