
from random import randint

print("----- Adivina el Numero Secreto -----")

Secret_Num = randint(1, 9)

User_Num = int(input("Adivina el número secreto  🪄  : "))

Round_Counter = 1

while User_Num != Secret_Num:
    print(f"\n❌   Incorrecto. Intenta de nuevo. Era {Secret_Num}  🪄\n")
    User_Num = int(input("Adivina el número secreto: "))
    Round_Counter += 1

print(f"\n✅   ¡Correcto! Has adivinado el número secreto: {Secret_Num} en {Round_Counter} intentos.\n")

print("----- Fin del Juego -----")
