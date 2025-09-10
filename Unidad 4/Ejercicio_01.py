print("➖➖➖➖➖➖ Promedio , Mas Alto y Mas Bajo ➖➖➖➖➖➖➖➖")

Notes = [9, 8, 5, 7, 9, 6, 4, 3, 2, 4]

acc = 0

highest = 0

lowest = 10

for i in range(len(Notes)):
    acc += Notes[i]
    if Notes[i] > highest:
        highest = Notes[i]
    if lowest == 0 or Notes[i] < lowest:
        lowest = Notes[i]

print(Notes)

print(f"\nEl promedio es: {acc / len(Notes)}")
print(f"\nLa nota más alta es: {highest}")
print(f"\nLa nota más baja es: {lowest}")

print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")