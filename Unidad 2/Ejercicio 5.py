print("-----Verificador de Contraseña-----")

User_Pass = input("Ingresa Tu Contraseña: ")

if len(User_Pass) >= 8 and len(User_Pass) <= 14:
    print("------ Ha ingresado una contraseña correcta ------")
else:
    print("------ Por favor, ingrese una contraseña de entre 8 y 14 caracteres ------")
