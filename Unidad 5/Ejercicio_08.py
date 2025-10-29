
def calcular_imc(peso, altura):

    try:
        peso = float(peso)
        altura = float(altura)
        
    except (TypeError, ValueError):
        print("Error: El peso y la altura deben ser números válidos.")
        return None

    try:
        if altura <= 0 or peso <= 0:
            raise ValueError("La altura y el peso deben ser números positivos mayores que cero.")
    except ValueError:
        print("Error: La altura y el peso deben ser números positivos mayores que cero.")
        return None
    
    imc = peso / (altura ** 2)
    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
    return imc