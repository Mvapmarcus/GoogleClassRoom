# soma


# def soma(numero1:float, numero2:float):
#     resultado = numero1 + numero2
#     print(f"A soma dos números é: {resultado}")

# soma(1,2)

#Contagem regressiva

# def contagem_regressiva(tempo:int):
#     for i in range(tempo, 0,-1):
#         print(i)

# contagem_regressiva(5)

def contagem_regressiva2(tempo:int):
    while True:
        if tempo > 0:
            print(tempo)
            tempo -= 1            
        else:
            break

contagem_regressiva2(5)
    

