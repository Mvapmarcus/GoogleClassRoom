produtos = int(input('Digite a quantidade de produtos:'))
caixas = int(input('Digite a capacidade de produtos por caixa:'))
resto = produtos % caixas
total_caixas = produtos // caixas
if resto > 0:
    total_caixas += 1

print(f'Você precisará de {total_caixas} caixas')