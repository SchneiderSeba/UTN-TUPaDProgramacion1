print("----- Media de un Rango -----")

User_Range = int(input("Ingresa la Cantidad de Numeros que va a Ingresar: "))

Accumulated_Sum = 0

for i in range(1, User_Range + 1):

    User_Num = int(input(f"➡️   Ingresa el número {i}: "))
    Accumulated_Sum += User_Num

print(f"\nLa media de los números ingresados es: {Accumulated_Sum / User_Range}\n")


print("➖➖➖➖➖ Fin ➖➖➖➖➖")