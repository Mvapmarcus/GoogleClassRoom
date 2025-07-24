valor = float(input('Digite o valor da meta: '))
parcela = int(input('Digite a quantidade de parcelas: '))

for i in range(1,parcela):
    total = valor / parcela
    restante = valor - total

    print(f'{restante}')
