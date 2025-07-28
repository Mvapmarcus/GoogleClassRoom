# Exercicio 13: Números maiores que 10
# Pede ao usuário cinco números e imprime apenas os maiores que 10.

contador = 0

for i in range(1, 6):
    numero = float(input(f'Digite o {i}º número: '))
    if numero > 10:
        contador += 1
print(f'Você digitou {contador} número(s) maior(es) que 10:')