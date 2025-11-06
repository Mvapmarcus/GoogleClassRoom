class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
    
pessoa_01 = Pessoa('Alice', 30)
pessoa_02 = Pessoa('Bob', 25)   

pessoa_01.apresentar()
pessoa_02.apresentar()