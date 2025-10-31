def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingresa la cantidad de términos de la serie Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(pos):
    print(fibonacci(i), end=" ")
print()