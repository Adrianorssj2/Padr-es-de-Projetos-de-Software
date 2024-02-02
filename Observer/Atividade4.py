class SistemaDeEstoque:
    def __init__(self):
        self._produtos = {}
        self._observadores = {}

    def adicionar_produto(self, produto, quantidade):
        self._produtos[produto] = quantidade
        self._observadores[produto] = []

    def adicionar_observador(self, produto, observador):
        self._observadores[produto].append(observador)

    def remover_observador(self, produto, observador):
        self._observadores[produto].remove(observador)

    def notificar_observadores(self, produto, quantidade):
        for observador in self._observadores[produto]:
            observador.atualizar(produto, quantidade)

    def alterar_quantidade(self, produto, quantidade):
        self._produtos[produto] = quantidade
        self.notificar_observadores(produto, quantidade)

class Observador:
    def __init__(self, nome):
        self._nome = nome

    def atualizar(self, produto, quantidade):
        print(f"{self._nome} recebeu a notificação: o produto {produto} tem {quantidade} unidades em estoque")

sistema = SistemaDeEstoque()

observador1 = Observador("Observador 1")
observador2 = Observador("Observador 2")

sistema.adicionar_produto("Camiseta", 10)
sistema.adicionar_produto("Calça", 5)

sistema.adicionar_observador("Camiseta", observador1)
sistema.adicionar_observador("Calça", observador2)

sistema.alterar_quantidade("Camiseta", 8)
sistema.alterar_quantidade("Calça", 7)
sistema.alterar_quantidade("Camiseta", 6)

sistema.remover_observador("Camiseta", observador1)

sistema.alterar_quantidade("Camiseta", 4)
sistema.alterar_quantidade("Calça", 3)
