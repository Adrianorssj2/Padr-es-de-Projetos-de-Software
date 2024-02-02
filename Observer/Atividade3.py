class SistemaDeNoticias:
    def __init__(self):
        self._noticias = []
        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self, noticia):
        for observador in self._observadores:
            observador.atualizar(noticia)

    def publicar_noticia(self, titulo, conteudo):
        noticia = {"titulo": titulo, "conteudo": conteudo}
        self._noticias.append(noticia)
        self.notificar_observadores(noticia)

class Observador:
    def __init__(self, nome):
        self._nome = nome

    def atualizar(self, noticia):
        print(f"{self._nome} recebeu a notificação: {noticia['titulo']}")

sistema = SistemaDeNoticias()

observador1 = Observador("Observador 1")
observador2 = Observador("Observador 2")

sistema.adicionar_observador(observador1)
sistema.adicionar_observador(observador2)

sistema.publicar_noticia("Noticia 1", "Comentario.")
sistema.publicar_noticia("Noticia 2", "Comentario.")
sistema.publicar_noticia("Noticia 3", "Comentario.")

sistema.remover_observador(observador1)

sistema.publicar_noticia("Noticia 4", "Cometario.")
