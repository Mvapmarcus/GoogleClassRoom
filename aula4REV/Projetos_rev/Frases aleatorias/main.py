# projeto de historias engraçadas

from montador_de_historias import gerar_frase_aleatoria

if __name__ == "__main__":
    print("Olá. Bem vindo!")
    print("A seguir serão exibidas histórias maluca, aproveite.")
for i in range(3):
    frase_aleatoria = gerar_frase_aleatoria()
    print(frase_aleatoria)