print("----- Suma de Intervalos -----")

User_Num_Init = int(input("Ingrese un número de Inicio : "))
User_Num_End = int(input("Ingrese un número de Fin : "))
Counter = 0

for Num in range(User_Num_Init, User_Num_End + 1):
    Counter += Num

print(f"La Suma de los numerosentre {User_Num_Init} y {User_Num_End} : {Counter}")

print("----- Fin -----")
