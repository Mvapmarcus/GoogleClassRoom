# exercício 9 - Voto Obrigatório
# Verifica se o usuário tem idade para votar

idade = int(input(f'Digite a sua idade:'))

if idade >= 18:
    print('Voto obrigatório')
elif idade >= 16 and idade <18:
    print('Voto facultativo')
else:
    print('Não tem idade pra votar')