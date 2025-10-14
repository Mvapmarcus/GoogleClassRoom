# pedir numeros inteiros positivos
# se numero for negativo encerrre e mostre a soma dos numeros

soma = 0
while True:
    numero = int(input('Digite um número positivo: '))
    if numero > 0:
        soma += numero
    else:   
        print(f'A soma dos números positivos é: {soma}')
        break
    