def favoritar_musica(musica):
    """Marca a música passada como favorita."""
    musica["favorita"] = True
    return musica

musica = {
    'titulo': 'Imagine',
    'artista': 'John Lennon',
    'favorita': False
}

favoritar_musica(musica)
print(f"Música '{musica}")
    