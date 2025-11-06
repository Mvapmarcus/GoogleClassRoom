class Musica:
    """Representa uma música simples."""

    def __init__(self, titulo: str, artista: str, favorita: bool = False):
        self.titulo = titulo
        self.artista = artista
        self.favorita = favorita

    def __repr__(self) -> str:
        estrela = ' ★' if self.favorita else ''
        return f"{self.titulo} - {self.artista}{estrela}"


# variável música (instância única conforme pedido)
musica = Musica('Imagine', 'John Lennon')


def favoritar_musica():
    """Marca a variável global `musica` como favorita."""
    global musica
    musica.favorita = True
    print(f"Música '{musica.titulo}' marcada como favorita.")


if __name__ == '__main__':
    print('Antes:', musica)
    favoritar_musica()
    print('Depois:', musica)
