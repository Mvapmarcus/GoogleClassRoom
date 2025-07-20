preço_produto = float(input('Digite o preço do produto:'))
desconto = float(input('Digite o percentual de desconto:'))
preço_final = preço_produto - (preço_produto * desconto / 100)

print(f'Preço final: {preço_final}')
