
# # cumprimento
# def cumprimentar(nome:str):
#     print("-----------")
#     print(f"Olá {nome}")
#     print("-----------")

# nome_usuario= input("Digite o seu nome:")
# cumprimentar(nome_usuario)
# cumprimentar(nome_usuario)
# cumprimentar(nome_usuario)

# print("-----------")
# # tabuada
# def fazer_tabuada(n:int):
#     for i in range(1,11):
#         resultado = n * i
#         print(resultado)

# fazer_tabuada(2)
# numero = int(input("Digite um numero para fazer a tabuada:"))
# fazer_tabuada(numero)
# print("-----------")

#IMC
def imc(peso:float, altura:float):
    resultado = peso / altura ** 2
    print(resultado)

peso_usuario = float(input("Digite o seu peso: "))
altura_usuario = float(input("Digite a sua altura: "))

imc(peso_usuario, altura_usuario)
print("-----------")

#verificação de idade
def verificar_idade(idade:int):
    if idade < 18:
        print("Você é menor de idade.")
    else:
        print("Você é maior de idade.")

idade_usuario = int(input("Digite a sua idade:"))

verificar_idade(idade_usuario)

