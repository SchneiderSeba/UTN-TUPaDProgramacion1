def contar_digito(numero, digito):
    # Caso base: cuando el número tiene un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    # Caso recursivo: comparar último dígito y continuar con el resto
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("Ingresa un número entero positivo: "))
digito = int(input("Ingresa un dígito (0-9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("Entrada inválida. Usa un número positivo y un dígito entre 0 y 9.")
else:
    resultado = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {resultado} veces en {numero}.")