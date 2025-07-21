# Exercício 23 ano bissexto
# Verifica se uma data é válida considerando anos bissextos

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))  
ano = int(input("Digite o ano: "))

# 2024 foi ano bissexto
# ano bissexto acontece quando o ano é divisível por 4, exceto se for divisível por 100,
# a menos que também seja divisível por 400.

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    if mes == 2 and dia > 29:
        print("Data inválida!")
    elif mes in [4, 6, 9, 11] and dia > 30:
        print("Data inválida!")
    elif mes < 1 or mes > 12 or dia < 1 or dia > 31:
        print("Data inválida!")
    else:
        print("Data válida!")
else:
    if mes == 2 and dia > 28:
        print("Data inválida!")
    elif mes in [4, 6, 9, 11] and dia > 30:
        print("Data inválida!")
    elif mes < 1 or mes > 12 or dia < 1 or dia > 31:
        print("Data inválida!")
    else:
        print("Data válida!")