# Exercicio 8: Pagamento de divida parcelada
# Pede ao usuário o valor da divida e divide em parcelas.

valor = float(input('Digite o valor da dívida: '))
parcelas = int(input('Digite a quantidade de parcelas: '))
valor_parcela = valor / parcelas

for i in range(1, parcelas + 1):
    print(f'Parcela {i}: R$ {valor_parcela:.2f}') 