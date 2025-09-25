#Funçoes básicas

def dizimo(valor: float):
    dizimo = valor * 0.10
    return dizimo

def triplicar(numero: float):
    triplicar = numero * 3
    return triplicar

def somar(n1:float, n2:float):
    soma = n1 + n2
    return soma

# usando lambda : Função simplificada
# usados para funções pequenas de uma linha

dizimo = lambda valor: valor * 0.10
triplicar = lambda numero: numero * 3
somar = lambda n1, n2: n1 + n2

