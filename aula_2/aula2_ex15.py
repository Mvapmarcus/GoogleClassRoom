idade = int(input("Digite a sua idade: "))
valor = float(input("Digite o valor da compra: "))

if idade >= 60 or valor > 200:
    print(f"Você tem direito a um desconto de 10%. O valor com desconto é: {valor - (valor * .1)}")
else:
    print(f"Você não tem direito a desconto. O valor da compra é: {valor}")
    