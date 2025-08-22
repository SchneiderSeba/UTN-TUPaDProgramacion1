
print("-----Verificador de Edad-----")

User_Age = int(input("Ingresa Tu Edad: "))

match User_Age:
    case age if age < 12:
        print("-----Eres un Niño-----")
    case age if age >= 12 and age < 18:
        print("-----Eres un Adolescente-----")
    case age if age >= 18 and age < 30:
        print("-----Eres un Adulto Joven-----")
    case _:
        print("-----Eres Un Adulto-----")
