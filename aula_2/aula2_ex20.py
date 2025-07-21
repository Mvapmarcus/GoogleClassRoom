# exercício 20 - Ingresso de Cinema
# Verifica se o usuário paga meia entrada ou inteira

estudante = input('Você é estudante? (sim/não):')
idade = int(input('Qual a sua idade? '))
dia = int(input('''Qual o dia da semana?
                1. Segunda
                2. Terça    
                3. Quarta
                4. Quinta
                5. Sexta
                6. Sábado
                7. Domingo:
                Escolha a opção de 1 a 7: '''))

if idade < 18 or estudante in 'sim':
    print('Você paga meia!')
elif dia == 3:
    print('Você paga meia!')
else:
    print('Você paga inteira!')
