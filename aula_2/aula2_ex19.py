# exercício 19 - Empréstimo
# Verifica se o usuário pode obter um empréstimo com base na renda, idade e aposentadoria

renda = float(input('Qual a sua renda? '))
idade = int(input('Qual a sua idade? '))
aposentado = input('Você é aposentado? (sim/não) ')

if renda > 3000 and aposentado in 'sim':
    print('Empréstimo aprovado')
elif renda > 5000 and idade >= 30:
    print('Empréstimo aprovado')
else:
    print('Empréstimo negado')


