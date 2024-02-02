class Modelo:
    def __init__(self, nome, elementos):
        self.nome = nome
        self.elementos = elementos
        
    def __str__(self):
        return f"Modelo: {self.nome}, Elementos: {self.elementos}"

class BaseDeDados:
    def __init__(self):
        self.modelos = {} 

    def cadastrar(self, modelo):
        self.modelos[modelo.nome] = modelo
        print(f"Modelo {modelo.nome} cadastrado com sucesso.")

    def recuperar(self, nome):
        if nome in self.modelos:
            return self.modelos[nome]
        else:
            print(f"Modelo {nome} não encontrado.")

    def atualizar(self, modelo):
        if modelo.nome in self.modelos:
            self.modelos[modelo.nome] = modelo
            print(f"Modelo {modelo.nome} atualizado com sucesso.")
        else:
            print(f"Modelo {modelo.nome} não encontrado.")

    def remover(self, nome):
        if nome in self.modelos:
            del self.modelos[nome]
            print(f"Modelo {nome} removido com sucesso.")
        else:
            print(f"Modelo {nome} não encontrado.")

class Conexao:
    def __init__(self, base_de_dados):
        self.base_de_dados = base_de_dados
        print("Conexão estabelecida.")

    def fechar(self):
        print("Conexão fechada.")

class Cliente:
    def __init__(self):
        self.base_de_dados = BaseDeDados() 
        self.conexao = None

    def conectar(self):
        self.conexao = Conexao(self.base_de_dados)

    def desconectar(self):
        self.conexao.fechar()
        self.conexao = None

    def cadastrar_modelo(self, modelo):
        if self.conexao:
            self.conexao.base_de_dados.cadastrar(modelo)
        else:
            print("Conexão não estabelecida.")

    def recuperar_modelo(self, nome):
        if self.conexao:
            return self.conexao.base_de_dados.recuperar(nome)
        else:
            print("Conexão não estabelecida.")

    def atualizar_modelo(self, modelo):
        if self.conexao:
            self.conexao.base_de_dados.atualizar(modelo)
        else:
            print("Conexão não estabelecida.")

    def remover_modelo(self, nome):
        if self.conexao:
            self.conexao.base_de_dados.remover(nome)
        else:
            print("Conexão não estabelecida.")


if __name__ == "__main__":
    cliente = Cliente()

    modelo1 = Modelo("A", ["a1", "a2", "a3"])
    modelo2 = Modelo("B", ["b1", "b2"])

    cliente.cadastrar_modelo(modelo1) 

    cliente.conectar()

    cliente.cadastrar_modelo(modelo1)
    cliente.cadastrar_modelo(modelo2)

    modelo = cliente.recuperar_modelo("A")
    print(modelo)
    modelo = cliente.recuperar_modelo("B")
    print(modelo)

    modelo2.elementos.append("b3")
    cliente.atualizar_modelo(modelo2)
    
    modelo = cliente.recuperar_modelo("B")
    print(modelo)

    cliente.remover_modelo("A")

    cliente.desconectar()
