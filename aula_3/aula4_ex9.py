# Exercicio 9: Soma de numeros
# Pede ao usuário 5 números e imprime a soma deles.

soma = 0
for i in range(1, 6):
    numero = float(input(f'Digite o {i}º número: '))
    soma += numero
print(f'A soma dos números é: {soma}') 
