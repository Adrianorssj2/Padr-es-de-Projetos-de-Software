class ContadorDeCliques:
    def __init__(self):
        self._cliques = 0
        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.atualizar(self._cliques)

    def clicar(self):
        self._cliques += 1
        self.notificar_observadores()

class Observador:
    def __init__(self, nome):
        self._nome = nome

    def atualizar(self, cliques):
        print(f"{self._nome} recebeu a notificação: o número de cliques é {cliques}")

contador = ContadorDeCliques()

observador1 = Observador("Observador 1")
observador2 = Observador("Observador 2")

contador.adicionar_observador(observador1)
contador.adicionar_observador(observador2)

contador.clicar()
contador.clicar()
contador.clicar()

contador.remover_observador(observador1)

contador.clicar()
contador.clicar()
