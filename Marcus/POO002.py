class ContaBancaria:

    def __init__(self, titular = str, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor = float):
        self.saldo += valor
        print(f'Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}')

    def sacar(self, valor = float):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}')
        else:
            print(f'Saldo insuficiente para saque de R$ {valor:.2f}. Saldo atual: R$ {self.saldo:.2f}')
    
    def ver_saldo(self):
        print(f'Saldo atual: R$ {self.saldo:.2f}')

conta_maria = ContaBancaria('Maria' ,100.0)

conta_maria.ver_saldo()
conta_maria.depositar(50.0)
conta_maria.sacar(30.0)
conta_maria.sacar(200.0)
conta_maria.ver_saldo()