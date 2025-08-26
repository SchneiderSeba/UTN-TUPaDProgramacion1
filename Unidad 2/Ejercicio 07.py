print('----- Tu Frase termina en Vocal o No ? -----')

User_Phrase = input("Por favor, ingresa una frase: ").lower()

if User_Phrase[-1] == "a" or User_Phrase[-1] == "e" or User_Phrase[-1] == "i" or User_Phrase[-1] == "o" or User_Phrase[-1] == "u":
    print(f"{User_Phrase} !")
else:
    print(User_Phrase)
