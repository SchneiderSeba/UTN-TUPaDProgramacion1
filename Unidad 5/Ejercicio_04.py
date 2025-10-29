import math

def calcular_area_circulo(radio):
    resultado = math.pi * radio ** 2
    print(f"El área del círculo con radio {radio} es {resultado}")
    return resultado

def calcular_perimetro_circulo(radio):
    resultado = 2 * math.pi * radio
    print(f"El perímetro del círculo con radio {radio} es {resultado}")
    return resultado