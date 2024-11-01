class Produto:
    def __init__(self, nome: str, preco: float, quantidade:int) -> None:
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def exibir_informacoes(self) -> None:
        return f"{self.nome}: Nome,{self.preco}: Preco, {self.quantidade}: Quantidade"
        print("Informações do Produto")
        print(f"Nome do Produto: {self.nome}")
        print(f"Preço do Produto: {self.preco}")
        print(f"Quantidade: {self.quantidade}")
    
    def atualizar_preco(self, novo_preco:float) -> None:
        self.novo_preco += 6.99
        print(f"{self.nome} atualizou o preço")
    
    def atualizar_quantidade(self, nova_quantidade:int) -> None:         
        self.nova_quantidade += 2
        print(f"{self.nova_quantidade}")

prod1 = Produto("Maçã", 3.99, 1)
prod1.atualizar_preco()
print(prod1.preco)
prod1.atualizar_quantidade()
print(prod1.quantidade)   