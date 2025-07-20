numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"O maior número é: {numero_1}")
elif numero_2 > numero_1 and numero_2 > numero_3:   
    print(f"O maior número é: {numero_2}")
else:
    print(f"O maior número é: {numero_3}")