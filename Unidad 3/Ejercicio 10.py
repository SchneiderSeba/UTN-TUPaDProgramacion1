print("➖➖➖➖➖ Invertidor de Numeros ➖➖➖➖➖")

User_Num = str(input("Ingresa un número: "))
invers_str = ""

for digit in User_Num:
    invers_str = digit + invers_str
    print(f"\n➡️   Dígito: {digit}")

print(f"\nEl número invertido es: {int(invers_str)}")

print("\n➖➖➖➖➖ Fin ➖➖➖➖➖")  
