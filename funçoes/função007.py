# Verificação de senha forte

def verificar_senha(senha: str):
    if len(senha) >= 8 and any(char.isdigit() for char in senha) and any(char.isupper() for char in senha):
        return True
    else:
        return False
    
senha = input("Digite sua senha: ")

if verificar_senha(senha):
    if verificar_senha(senha):
        print("Senha forte. Bem vindo!")

else:
    for tentativas in range(2):
        fraca = input("Senha fraca. Deseja alterar? (s/n): ")    
        if fraca.lower() == "n":
            print("tentativas encerradas.")
            break
        elif fraca.lower() == "s":
            nova_senha = input("Digite a nova senha: ")
            if verificar_senha(nova_senha):
                print("Senha alterada com sucesso.Bem vindo!")
                break
            elif tentativas == 1:
                print("Número máximo de tentativas atingido. Tente novamente mais tarde.")
            else:
                print("Senha ainda fraca. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")
            continue
    

# Fim do código