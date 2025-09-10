print("➖➖➖➖➖➖ Promedio de Notas por Alumno y por Materia ➖➖➖➖➖➖➖➖")

Matriz = [
    [1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8],
    [7, 8, 9, 10, 10]
]
#Filas son materias
#Columnas son alumnos

Student_1_Avg = (Matriz[0][0] + Matriz[1][0] + Matriz[2][0]) / len(Matriz) 
Student_2_Avg = (Matriz[0][1] + Matriz[1][1] + Matriz[2][1]) / len(Matriz)
Student_3_Avg = (Matriz[0][2] + Matriz[1][2] + Matriz[2][2]) / len(Matriz)
Student_4_Avg = (Matriz[0][3] + Matriz[1][3] + Matriz[2][3]) / len(Matriz)
Student_5_Avg = (Matriz[0][4] + Matriz[1][4] + Matriz[2][4]) / len(Matriz)

Subject_1_Avg = sum(Matriz[0]) / len(Matriz[0])
Subject_2_Avg = sum(Matriz[1]) / len(Matriz[1])
Subject_3_Avg = sum(Matriz[2]) / len(Matriz[2])

print(f"\nEl promedio del Alumno 1 es: {Student_1_Avg}")
print(f"\nEl promedio del Alumno 2 es: {Student_2_Avg}")
print(f"\nEl promedio del Alumno 3 es: {Student_3_Avg}")
print(f"\nEl promedio del Alumno 4 es: {Student_4_Avg}")
print(f"\nEl promedio del Alumno 5 es: {Student_5_Avg}")

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

print(f"\nEl promedio de la Materia 1 es: {Subject_1_Avg}")
print(f"\nEl promedio de la Materia 2 es: {Subject_2_Avg}")
print(f"\nEl promedio de la Materia 3 es: {Subject_3_Avg}")

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")