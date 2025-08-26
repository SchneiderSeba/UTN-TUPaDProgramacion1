from statistics import mean, median, mode
import random

print("----- Calculadora de Estadísticas -----")


Random_Numbers = [random.randint(1, 100) for i in range(50)]

# Prueba para el Sin Sesgo
# Random_Numbers = [10,10,10,10,10,10]

Mode_Random_Numbers = mode(Random_Numbers)
Mean_Random_Numbers = mean(Random_Numbers)
Median_Random_Numbers = median(Random_Numbers)

print(f"Media: {Mean_Random_Numbers}")
print(f"Mediana: {Median_Random_Numbers}")
print(f"Moda: {Mode_Random_Numbers}")


if Mean_Random_Numbers > Median_Random_Numbers and Median_Random_Numbers > Mode_Random_Numbers:
    print("----- Sesgo positivo o a la derecha -----")
elif Mean_Random_Numbers < Median_Random_Numbers and Median_Random_Numbers < Mode_Random_Numbers:
    print("----- Sesgo negativo o a la izquierda -----")
elif Mean_Random_Numbers == Median_Random_Numbers == Mode_Random_Numbers:
    print("----- Sin Sesgo -----")
else:
    print("----- Algo Salió Mal -----")

