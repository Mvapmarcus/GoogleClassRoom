# Exercício 1 - Calcular o valor restante da divida de uma meta
# Pede ao usuário o valor da meta e em quantas parcelas ele quer dividir, em seguida informa 
# o valor restante da divida a cada parcela paga.

valor = float(input('Digite o valor da meta: '))
parcela = int(input('Digite a quantidade de parcelas: '))
parcela_paga = int(input('Digite a quantidade de parcelas pagas: '))
valor_parcela = valor / parcela # mostra o valor de cada parcela
resto = valor - (parcela_paga * valor_parcela) # mostra o valor restante da meta
if parcela_paga == 0:
    print(f"Você ainda não pagou nenhuma parcela de . O valor restante da meta é R${resto:.2f}.")
else:
    for i in range(1,(parcela+1)):
        if i <= parcela_paga:
            print(f'Parcela {i}: R${valor_parcela:.2f} Resto  da meta: R${resto:.2f}')
        elif i > parcela_paga:
            resto = resto - valor_parcela
            parcela_paga += 1             
            print(f'Parcela {i}: R${valor_parcela:.2f} Resto da meta: R${resto:.2f}')
            
    

    