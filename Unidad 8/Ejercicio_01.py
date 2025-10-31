def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    return n * factorial(n - 1)

num = int(input("Ingresa un número entero: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")
