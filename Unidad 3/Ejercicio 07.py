print("----- Suma de Numeros en un Rango -----")

User_Num_Init = 0
User_Num_End = int(input("Ingresa un número final: "))

Suma = 0
for i in range(User_Num_Init, User_Num_End + 1):
    Suma += i

print(f"\n La suma de los números en el rango es: {Suma}\n")

print("----- Fin -----")
