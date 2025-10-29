# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra
print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
frase = input("Ingrese una frase: ")
palabras = set(frase.split())

for palabra in palabras:
    contador = frase.split().count(palabra)
    palabras_diccionario = {palabra: contador}
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f'Recuento : {palabras_diccionario}')
print("➖➖➖➖➖➖➖➖➖➖➖➖➖")    
print(f'Palabras únicas: {palabras}')
print("➖➖➖➖➖➖➖➖➖➖➖➖➖")