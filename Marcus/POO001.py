class Produto:
    def __init__(self, nome = str, preco = float, estoque = int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade = int):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f'Venda realizada: {quantidade} unidade(s) de {self.nome}.')
        else:
            print(f'Estoque insuficiente para vender {quantidade} unidade(s) de {self.nome}.')

arroz = Produto("Arroz 5kg", 22.90, 3 )


if __name__ == '__main__':
    arroz.vender(3)
    arroz.vender(10)