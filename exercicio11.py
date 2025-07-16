distancia = float(input('Digite a distancia em km que deseja percorrer:'))
consumo_veiculo = float(input('Digite o consumo do veiculo em km/litro:'))
combustível = distancia/consumo_veiculo

print(f'A quantidade de combustível necessária para essa viajem é {combustível} litros')