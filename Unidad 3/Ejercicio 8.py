print("----- Pares , Inpares , Negativos y Positivos -----")

User_Range = int(input("Ingresa la Cantidad de Numeros que va a Ingresar: "))
# User_Num = int(input("Ingresa los número uno por uno: "))

Even_Counter = 0
Odd_Counter = 0
Positive_Counter = 0
Negative_Counter = 0

for i in range(1, User_Range + 1):
    
    User_Num = int(input(f"Ingresa el número {i}: "))
    
    if User_Num % 2 == 0:
        Even_Counter += 1
    else:
        Odd_Counter += 1

    if User_Num > 0:
        Positive_Counter += 1
    elif User_Num < 0:
        Negative_Counter += 1

    # User_Num = int(input(f"Ingresa el número {i}: "))

print(f"\nEn total ingresaste {Even_Counter} números pares.")
print(f"En total ingresaste {Odd_Counter} números impares.")
print(f"En total ingresaste {Positive_Counter} números positivos.")
print(f"En total ingresaste {Negative_Counter} números negativos.")

print("----- Fin -----")
