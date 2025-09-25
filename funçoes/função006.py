#função para calcular o preço com desconto

def calcular_desconto(preco:float, desconto:float):
    preco_final = preco - (preco * desconto / 100)
    return preco_final  

valor_produto = (100)
valor_desconto = (10)

preco_final = calcular_desconto(valor_produto, valor_desconto)

print(f"O preço final com desconto é: {preco_final}")

# Fim do código~/Documentos/marcus/Python/funçoes/função005.py
