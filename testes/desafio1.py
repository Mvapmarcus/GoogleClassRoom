# criar um jogo de adivinhação.
# o computador escolhe um numero de 1 a 20
# o usuario tenta adivinhar o numero dentro de 5 tentativas

import random

numero_secreto = random.randint(1, 20)
tentativas = 5

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 20.")

for i in range(tentativas):
    palpite = int(input(f"Tentativa {i + 1}/{tentativas}: Digite seu palpite: "))
    
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        break
else:
    print(f"Você não conseguiu adivinhar o número. O número era {numero_secreto}.") 