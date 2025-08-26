print('----- Magnitud de Richter -----')

User_Magnitude = float(input("Por favor, ingresa la magnitud del Terremoto: "))

if User_Magnitude < 3.0:
    print("----- Muy Leve -----")
elif 3.0 <= User_Magnitude < 4.0:
    print("----- Leve -----")
elif 4.0 <= User_Magnitude < 5.0:
    print("----- Moderado -----")
elif 5.0 <= User_Magnitude < 6.0:
    print("----- Fuerte -----")
elif 6.0 <= User_Magnitude < 7.0:
    print("----- Muy Fuerte -----")
else:
    print("----- Extremo -----")
