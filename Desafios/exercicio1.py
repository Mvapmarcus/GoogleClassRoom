# Exercício 1 - Calcular o valor restante da divida de uma meta
# Pede ao usuário o valor da meta e em quantas parcelas ele quer dividir, em seguida informa 
# o valor restante da divida a cada parcela paga.

valor = float(input('Digite o valor da meta: '))
parcela = int(input('Digite a quantidade de parcelas: '))
valor_parcela = valor / parcela # mostra o valor de cada parcela
resto = valor  # Inicializa o valor restante com o valor total da meta

for i in range(1, parcela + 1):
    if i <= parcela:
       resto -= valor_parcela  # Atualiza o valor restante após cada parcela 
    print(f'Parcela {i}: Valor {valor_parcela:.2f}, falta R$ {resto:.2f}')
