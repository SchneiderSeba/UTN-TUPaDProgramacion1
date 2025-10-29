# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.


parcial_1 = {5, 7, 10, 2, 8}
parcial_2 = {5, 6, 7, 8, 9}

freez_parcial_1 = list(parcial_1)
freez_parcial_2 = list(parcial_2)

aprobados1 = {n for n in freez_parcial_1 if n >= 7}
aprobados2 = {n for n in freez_parcial_2 if n >= 7}
print("Estudiantes que aprobaron el Parcial 1:", aprobados1)
print("Estudiantes que aprobaron el Parcial 2:", aprobados2)

ambos_parciales = aprobados1 | aprobados2
print("Estudiantes que aprobaron ambos parciales:", ambos_parciales)

solo_uno = aprobados1 ^ aprobados2
print("Estudiantes que aprobaron solo uno de los dos parciales:", solo_uno)

al_menos_uno = aprobados1 | aprobados2
print("Estudiantes que aprobaron al menos uno de los dos parciales:", al_menos_uno)