# Exercicio 12: Contagem de vogais
# Pede ao usuário uma string e conta quantas vogais existem nela.

frase = input('Digite uma frase: ')
vogais = 'aeiouAEIOU'
contador = 0

for i in frase:
    if i in vogais:
        contador += 1

print(f'Essa frase tem {contador} vogais.')