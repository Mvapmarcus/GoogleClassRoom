#exercício 22 - Caixa Eletrônico
# Verifica se o valor do saque é válido e fornece as notas correspondentes

valor = int(input("Digite o valor do saque: "))

if valor < 10 or valor > 600:
    print("Valor inválido!.")
else:
    notas_100 = valor // 100
    valor = valor % 100

    notas_50 = valor // 50
    valor = valor % 50

    notas_10 = valor // 10
    valor = valor % 10

    notas_5 = valor // 5
    valor = valor % 5

    notas_1 = valor

    print("Notas fornecidas:")
    print(f"Notas de 100: {notas_100}")
    print(f"Notas de 50: {notas_50}")
    print(f"Notas de 10: {notas_10}")
    print(f"Notas de 5: {notas_5}")
    print(f"Notas de 1: {notas_1}")