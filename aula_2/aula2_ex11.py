# exercício 11 - Nota do Aluno
# Classifica a nota do aluno em Aprovado, Recuperação ou Reprovado

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")    
else:
    print("Reprovado")
    