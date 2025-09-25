# quero calcular a media de 3 notas dos alunos 

def calcular_media(n1:float, n2:float, n3:float):
    media = (n1 + n2 + n3) / 3
    return media

aluno1 = calcular_media(7, 8, 9)
aluno2 = calcular_media(6, 5, 4)
aluno3 = calcular_media(10, 9, 8)

media = calcular_media(aluno1, aluno2, aluno3)

print(f"A média do aluno 1 é: {aluno1}")
print(f"A média do aluno 2 é: {aluno2}")
print(f"A média do aluno 3 é: {aluno3}")
print(f"A média das notas dos alunos é: {media}")

# Fim do código