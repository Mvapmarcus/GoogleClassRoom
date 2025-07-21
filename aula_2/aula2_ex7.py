# exercício 7 - Saque Bancário
# Verifica se o valor do saque é válido

valor = float(input('Digite o valor a ser sacado:'))

if valor > 0:
    print('Saque efetuado com sucesso!')
else:
    print('Valor inválido!')