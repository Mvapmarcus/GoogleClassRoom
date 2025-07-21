# exercício 13 - Login e Senha
# Verifica se o login e senha correspondem aos cadastrados

login = input('Digite o login: ')
senha = input('Digite a senha: ')

if login == 'admin'and senha == '1234':
    print('Login realizado com sucesso!')
else:
    print('Nome de usuário ou senha inválidos!')