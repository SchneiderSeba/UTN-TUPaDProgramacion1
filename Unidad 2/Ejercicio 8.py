print('----- Modificacion de Nombre -----')

User_Name = input("Por favor, ingresa tu nombre: ")
User_Choice = input("Ingrese 1 : Para Ver Su Nombre En Mayusculas\nIngrese 2 : Para Ver Su Nombre En Minusculas\nIngrese 3 : Para Ver Su Nombre Con La Primer Letra En Mayuscula : ")


if User_Choice == "1":
    print(f"----- {User_Name.upper()} -----")
elif User_Choice == "2":
    print(f"----- {User_Name.lower()} -----")
elif User_Choice == "3":
    print(f"----- {User_Name.title()} -----")