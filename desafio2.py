# jogo pedra papel ou tesoura 
#o computador escolhe pedra, papel ou tesoura
#o usuario escolhe pedra, papel ou tesoura
#o computador e o usuario jogam 3 vezes
#no final o computador e o usuario mostram quantas vezes ganharam

import random

opcoes = ['pedra', 'papel', 'tesoura']
vitorias_usuario = 0
vitorias_computador = 0

for i in range(3):
    computador = random.choice(opcoes)
    usuario = input(f"Tentativa {i + 1}/3 - Escolha pedra, papel ou tesoura: ").lower()
    
    if usuario not in opcoes:
        print("Opção inválida! Tente novamente.")
        continue
    
    print(f"Computador escolheu: {computador}")
    
    if (usuario == 'pedra' and computador == 'tesoura') or \
       (usuario == 'papel' and computador == 'pedra') or \
       (usuario == 'tesoura' and computador == 'papel'):
        print("Você ganhou!")
        vitorias_usuario += 1
    elif usuario == computador:
        print("Empate!")
    else:
        print("Computador ganhou!")
        vitorias_computador += 1

print(f"Resultado final:")
print(f"Vitórias do usuário: {vitorias_usuario}")
print(f"Vitórias do computador: {vitorias_computador}")    
