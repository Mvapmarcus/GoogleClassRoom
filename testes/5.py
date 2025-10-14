# Pedir usuario e senha 
# Se usuario = senha peça novamente

usuario = input('Digite o nome de usuario: ')
senha = input('Digite a senha: ')

while usuario == senha:
    print('Erro! A senha não pode ser igual ao nome de usuario')
    usuario = input('Digite o nome de usúurio: ')
    senha = input('Digite a senha: ')
print('Cadastro Realizado com sucesso!')
