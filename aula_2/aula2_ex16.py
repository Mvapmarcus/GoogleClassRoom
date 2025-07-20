idade = int(input('Digite a sua idade: '))
empregado = input('Você está empregado? (sim/não): ')

if idade < 12 or idade >= 65 or empregado in 'não':
    print('Você pode pegar o ônibus de graça.')
else:
    print('Você não pode pegar o ônibus de graça.')
    