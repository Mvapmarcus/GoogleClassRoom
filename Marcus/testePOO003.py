class Artista:
    def __init__(self, nome = str , favorito = bool):
        self.nome = nome
        self.favorito = favorito

    def favoritar(self):
        self.favorito = True

artista_01 = Artista('John Lennon', False)
artista_02 = Artista('Paul McCartney', False)

if __name__ == '__main__':
    print(artista_01.nome, artista_01.favorito)
    print(artista_02.nome, artista_02.favorito)
    artista_01.favoritar()
    artista_02.favoritar()
    print(artista_01.nome, artista_01.favorito)
    print(artista_02.nome, artista_02.favorito)