# Aula 2

def validar_senha (senha:str):
    if len(senha) >= 8:
        return True
    else:
        return False
    
senha = input("Digite sua senha: ")
if validar_senha(senha):
    print("Senha válida")
else:    
    print("Senha inválida")

# Fim do código