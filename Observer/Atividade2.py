class SistemaDeAlerta:
    def __init__(self, temperatura):
        self._temperatura = temperatura
        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.atualizar(self._temperatura)

    def alterar_temperatura(self, nova_temperatura):
        self._temperatura = nova_temperatura
        self.notificar_observadores()

class Observador:
    def __init__(self, nome):
        self._nome = nome

    def atualizar(self, temperatura):
        print(f"{self._nome} recebeu a notificação: a temperatura é {temperatura}°C")

sistema = SistemaDeAlerta(25)

observador1 = Observador("Observador 1")
observador2 = Observador("Observador 2")

sistema.adicionar_observador(observador1)
sistema.adicionar_observador(observador2)

sistema.alterar_temperatura(30)
sistema.alterar_temperatura(28)
sistema.alterar_temperatura(32)

sistema.remover_observador(observador1)

sistema.alterar_temperatura(27)
sistema.alterar_temperatura(29)
