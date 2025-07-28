# Exercicio 10: Numeros inteiros em um intervalo
# Pede ao usuário dois números inteiros e imprime todos os números inteiros entre eles.

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

print('O intervalo é :')# imprime apenas uma vez antes do loop
for i in range(min(numero_1, numero_2), max(numero_1, numero_2) + 1):#definição do intervalo
    print(i)
    