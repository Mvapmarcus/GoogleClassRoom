tempo = int(input('Digite o tempo em minutos:'))
distancia = float(input('Digite a distancia em km:'))
tarifa = 5 + (2.5*distancia) + (tempo*0.5)

print(f'O valor total da viajem é {tarifa}')