print('----- Paras Decrecientes en un Rango -----')

User_Num_Init = int(input("Ingresa un número inicial: "))
User_Num_End = int(input("Ingresa un número final: "))

for i in range(User_Num_End, User_Num_Init - 1, -1):
    if i % 2 == 0:
        print(i)
        
print('----- Fin -----')
