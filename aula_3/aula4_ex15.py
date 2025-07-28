# Exercício 15: interrupção de loop com break
# pede ao usuário uma palavra e interrompe o loop quando a primeira consoante for digitada.

palavra = input('Digite uma palavra: ')

for letra in palavra:
    if letra.lower() in 'aeiou':
        continue  # Ignora as vogais
    else:
        print(f'A primeira consoante encontrada é: {letra}')
        break  # Interrompe o loop ao encontrar a primeira consoante 