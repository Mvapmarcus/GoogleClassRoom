mes = int(input('Digite o numero do mes do ano:'))

if mes >= 1 and mes <=6:
    print('Primeiro semestre')
elif mes >= 7 and mes <= 12:
    print('Segundo semestre')
else:
    print('Mês inválido')