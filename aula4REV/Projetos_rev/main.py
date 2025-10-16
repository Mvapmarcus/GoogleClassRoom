# projeto de historias engraçadas

# combinar palavras aleatorias de tres categorias: protagonista , açoes e locais
# divididos em tres arquivos
# 1 banco_de_palavras.py
# contendo  tres funcoes que retornam uma lista de strings
# . obter_protagonsita()
#   "Um gato de botas"
#   "Um robo cozinheiro"
#   "Uma fada do dente"
# . obter_acoes()
#   "dançou break"
#   "comeu uma pizza de abacaxi"
#   "programou em Python"
# . obter_locais
#   "na lua"
#   "dentro de um vulcão"
#   "na biblioteca"
# 2 montador_de_historias.py
# criar função gerar_frases_aleatorias()
# . importe o modulo random
# . importe a função 1 banco_de_palavras
# . usar random.choice()
# . montar a frase no formato protagonista/ação/local
# . retorne a frase
# 3 main.py
# . importe a função gerar_frases_aleatorias()
# . print("Olá bem vindo")
# . print("A seguir serão exibidas histórias malucas, aproveite!")
# . usar "for" para gerar 3 frases e print cada uma delas

from montador_de_historias import gerar_frase_aleatoria

print("Olá bem vindo!")
print("A seguir serão exibidas histórias maluca, aproveite.")

for i in range(3):
    frase_aleatoria = gerar_frase_aleatoria()
    print(frase_aleatoria)