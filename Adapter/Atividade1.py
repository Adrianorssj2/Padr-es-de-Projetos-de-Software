class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def requisitar(self, servico):
        return servico.fazer()

class Servico:
    def __init__(self, descricao):
        self.descricao = descricao

    def executar(self):
        return f"Executando o serviço: {self.descricao}"

class Adapter:
    def __init__(self, servico):
        self.servico = servico

    def fazer(self):
        return self.servico.executar()

if __name__ == "__main__":
    cliente = Cliente("João")

    servico = Servico("Enviar e-mail")

    adaptador = Adapter(servico)

    resultado = cliente.requisitar(adaptador)

    print(resultado) 