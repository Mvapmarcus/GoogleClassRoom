class Funcionario:
     
    def __init__(self, nome :str, cpf :int, salario :float):
            self.nome = nome
            self.cpf = cpf
            self.salario = salario
            
    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Salário: R${self.salario:.2f}\n')     

class Analista(Funcionario):

    def __init__(self, nome :str, cpf :int, salario :float, projeto :str):
        super().__init__(nome, cpf, salario)
        self.projeto = projeto
    
class Gerente(Funcionario):

    def __init__(self, nome: str, cpf: str, salario: float, bonus_percentual: float):
        super().__init__(nome, cpf, salario)
        self.bonus_percentual = bonus_percentual
        self.equipe = []
   
    def calcular_bonus(self):
        print(f'Bônus: R${self.bonus_percentual * self.salario:.2f}\n')

analista_1 = Analista("Maria Silva", "12345678900", 4800, "Sistema de vendas")
analista_2 = Analista("Pedro Alves", "98765432100", 5200, "Aplicativo móvel")

gerente_1 = Gerente("João Pereira", "11122233344", 9000, 0.1)
gerente_2 = Gerente("Carla Souza", "55566677788", 12000, 0.15)

analista_1.exibir_dados()
analista_2.exibir_dados()
gerente_1.exibir_dados()
gerente_1.calcular_bonus()
gerente_2.exibir_dados()
gerente_2.calcular_bonus()
