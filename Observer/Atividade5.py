class SistemaDeChat:
    def __init__(self):
        self._clientes = []
        self._mensagens = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)

    def remover_cliente(self, cliente):
        self._clientes.remove(cliente)

    def notificar_clientes(self, mensagem):
        for cliente in self._clientes:
            cliente.atualizar(mensagem)

    def enviar_mensagem(self, remetente, texto):
        mensagem = {"remetente": remetente, "texto": texto}
        self._mensagens.append(mensagem)
        self.notificar_clientes(mensagem)

class Cliente:
    def __init__(self, nome):
        self._nome = nome

    def atualizar(self, mensagem):
        print(f"{self._nome} recebeu a mensagem: {mensagem['remetente']}: {mensagem['texto']}")

sistema = SistemaDeChat()

cliente1 = Cliente("Cliente 1")
cliente2 = Cliente("Cliente 2")
cliente3 = Cliente("Cliente 3")

sistema.adicionar_cliente(cliente1)
sistema.adicionar_cliente(cliente2)
sistema.adicionar_cliente(cliente3)

sistema.enviar_mensagem("Cliente 1", "Olá, pessoal!")
sistema.enviar_mensagem("Cliente 2", "Oi, tudo bem?")
sistema.enviar_mensagem("Cliente 3", "Tudo ótimo, e vocês?")
sistema.enviar_mensagem("Cliente 1", "Eu estou bem, obrigado.")

sistema.remover_cliente(cliente3)

sistema.enviar_mensagem("Cliente 2", "Que bom que estão bem. Eu também estou.")
