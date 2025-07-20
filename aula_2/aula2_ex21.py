nota_1 = float(input('Digite a primeira nota:'))
nota_2 = float(input('Digite a segunda nota:'))
media = (nota_1 + nota_2) / 2 

if media <= 4:
    print(f'Você foi REPROVADO com média {media}. Seu conceito é E.')
elif media > 4 and media < 6:
    print(f'Você foi REPROVADO com média {media}. Seu conceito é D.')
elif media >= 6 and media < 7.5:
    print(f'Você foi APROVADO com média {media}. Seu conceito é C.')
elif media >= 7.5 and media < 9:
    print(f'Você foi APROVADO com média {media}. Seu conceito é B.')
else:
    print(f'Você foi APROVADO com média {media}. Seu conceito é A.')