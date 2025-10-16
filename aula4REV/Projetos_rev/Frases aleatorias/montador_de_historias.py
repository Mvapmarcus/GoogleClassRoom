import random
from banco_de_palavras import obter_local, obter_protagonista, obter_acao

def gerar_frase_aleatoria():
    lista_protagonista = obter_protagonista()
    protagonista_aleatorio = random.choice(lista_protagonista)
    
    lista_acoes = obter_acao()
    acao_aleatoria = random.choice(lista_acoes)
    
    lista_locais = obter_local()
    local_aleatorio = random.choice(lista_locais)
    
    frase_aleatoria = f'{protagonista_aleatorio} {acao_aleatoria} {local_aleatorio}'
    
    return frase_aleatoria



  

