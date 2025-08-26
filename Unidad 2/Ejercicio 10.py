print("----- En que estación del año estás? -----")

User_hemisphere = input("Por favor, ingresa el hemisferio (N/S): ").upper()

User_month = int(input("Por favor, ingresa el mes (1-12): "))

User_day = int(input("Por favor, ingresa el día (1-31): "))

if User_hemisphere == 'N':
    if (User_month == 12 and 21 <= User_day <= 31) or (User_month in [1, 2]) or (User_month == 3 and 1 <= User_day <= 20):
        print("----- Invierno -----")
    elif (User_month == 3 and 21 <= User_day <= 31) or (User_month in [4, 5]) or (User_month == 6 and 1 <= User_day <= 20):
        print("----- Primavera -----")
    elif (User_month == 6 and 21 <= User_day <= 30) or (User_month in [7, 8]) or (User_month == 9 and 1 <= User_day <= 20):
        print("----- Verano -----")
    elif (User_month == 9 and 21 <= User_day <= 30) or (User_month in [10, 11]) or (User_month == 12 and 1 <= User_day <= 20):
        print("----- Otoño -----")
    else:
        print("----- Fecha no válida -----")
elif User_hemisphere == 'S':
    if (User_month == 12 and 21 <= User_day <= 31) or (User_month in [1, 2]) or (User_month == 3 and 1 <= User_day <= 20):
        print("----- Verano -----")
    elif (User_month == 3 and 21 <= User_day <= 31) or (User_month in [4, 5]) or (User_month == 6 and 1 <= User_day <= 20):
        print("----- Otoño -----")
    elif (User_month == 6 and 21 <= User_day <= 30) or (User_month in [7, 8]) or (User_month == 9 and 1 <= User_day <= 20):
        print("----- Invierno -----")
    elif (User_month == 9 and 21 <= User_day <= 30) or (User_month in [10, 11]) or (User_month == 12 and 1 <= User_day <= 20):
        print("----- Primavera -----")
    else:
        print("----- Fecha no válida -----")
else:
    print("----- Hemisferio no válido -----")
