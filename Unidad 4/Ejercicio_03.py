import random

print("➖➖➖➖➖➖ Generar 15 Numeros Random y Mostra los Pares e Impares ➖➖➖➖➖➖➖➖")

Item_List = random.sample(range(1, 100), 15)

Even_List = []

Odd_List = []


for item in Item_List:
    if item % 2 == 0:
        Even_List.append(item)
    else:
        Odd_List.append(item)

print(f"\nLista generada: {sorted(Item_List)} con {len(Item_List)} números.")
print(f"\nLista de Números Pares: {sorted(Even_List)} con {len(Even_List)} números.")
print(f"\nLista de Números Impares: {sorted(Odd_List)} con {len(Odd_List)} números.")
print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")