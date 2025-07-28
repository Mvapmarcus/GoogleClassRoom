for i in range(0,4):
    numero = float(input('Digite um número:'))

    if numero > 0:
        print(f'Número {numero} é positivo')
    elif numero == 0:
        print('Você digitou 0')
    else:
        print(f'Número {numero} é negativo')
