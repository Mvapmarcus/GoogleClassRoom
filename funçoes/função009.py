#função variavel de argumentos

def soma(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

resultado = soma(1, 2, 3, 4, 5)
print(f"A soma dos números é: {resultado}")
