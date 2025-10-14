#Peça ao usuário para digitar um número e exiba a tabuada desse número de 1 a 10.

numero = int(input('Digite um número: '))
multiplo = 1

while multiplo < 10:
    multiplo += 1
    print(f'{numero} x {multiplo} = {numero * multiplo}')
