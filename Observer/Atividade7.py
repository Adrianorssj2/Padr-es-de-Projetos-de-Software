class Candidato:
    def __init__(self, nome, numero, partido):
        self.nome = nome 
        self.numero = numero 
        self.partido = partido 
        self.votos = 0 

    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.partido}"

class Urna:
    def __init__(self, secao, zona):
        self.secao = secao 
        self.zona = zona 
        self.candidatos = [] 
        self.observadores = [] 
        self.votando = False 
    def adicionar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.atualizar(self)

    def iniciar_votacao(self):
        self.votando = True
        print(f"Urna {self.secao} - {self.zona} iniciou a votação")

    def encerrar_votacao(self):
        self.votando = False
        print(f"Urna {self.secao} - {self.zona} encerrou a votação")
        self.notificar_observadores() 

    def receber_voto(self, numero):
        if self.votando: 
            candidato = self.buscar_candidato(numero) 
            if candidato: 
                candidato.votos += 1 
                print(f"Voto confirmado para {candidato}")
            else: 
                print("Voto nulo")
        else: 
            print("Urna fechada")

    def buscar_candidato(self, numero):
        for candidato in self.candidatos:
            if candidato.numero == numero:
                return candidato
        return None 

class Boletim:
    def __init__(self, nome):
        self.nome = nome 
        self.urnas = [] 
        self.total = 0 

    def atualizar(self, urna):
        self.urnas.append(urna) 
        self.total += self.contar_votos(urna) 
        self.exibir() 

    def contar_votos(self, urna):
        votos = 0
        for candidato in urna.candidatos:
            votos += candidato.votos
        return votos

    def exibir(self):
        print(f"Boletim {self.nome}")
        print(f"Total de votos: {self.total}")
        print("Votos por urna:")
        for urna in self.urnas:
            print(f"- Urna {urna.secao} - {urna.zona}: {self.contar_votos(urna)} votos")
        print("Votos por candidato:")
        for candidato in self.listar_candidatos():
            print(f"- {candidato}: {candidato.votos} votos")
        print()

    def listar_candidatos(self):
        candidatos = []
        for urna in self.urnas:
            for candidato in urna.candidatos:
                if candidato not in candidatos and candidato.votos > 0:
                    candidatos.append(candidato)
        return candidatos

c1 = Candidato("Adriano", 10, "ABC")
c2 = Candidato("Joao", 20, "DEF")
c3 = Candidato("Kamilly", 30, "GHI")
c4 = Candidato("Daniela", 40, "JKL")

u1 = Urna(1, 1)
u2 = Urna(2, 1)
u3 = Urna(3, 2)
u4 = Urna(4, 2)

u1.adicionar_candidato(c1)
u1.adicionar_candidato(c2)
u2.adicionar_candidato(c1)
u2.adicionar_candidato(c2)
u3.adicionar_candidato(c3)
u3.adicionar_candidato(c4)
u4.adicionar_candidato(c3)
u4.adicionar_candidato(c4)

b1 = Boletim("Zona 1")
b2 = Boletim("Zona 2")
b3 = Boletim("Geral")

u1.adicionar_observador(b1)
u1.adicionar_observador(b3)
u2.adicionar_observador(b1)
u2.adicionar_observador(b3)
u3.adicionar_observador(b2)
u3.adicionar_observador(b3)
u4.adicionar_observador(b2)
u4.adicionar_observador(b3)

u1.iniciar_votacao()
u2.iniciar_votacao()
u3.iniciar_votacao()
u4.iniciar_votacao()

u1.receber_voto(10)
u1.receber_voto(20)
u1.receber_voto(10)
u1.receber_voto(50)
u2.receber_voto(20)
u2.receber_voto(20)
u2.receber_voto(10)
u2.receber_voto(10)
u3.receber_voto(30)
u3.receber_voto(40)
u3.receber_voto(30)
u3.receber_voto(60)
u4.receber_voto(40)
u4.receber_voto(40)
u4.receber_voto(30)
u4.receber_voto(30)

u1.encerrar_votacao()
u2.encerrar_votacao()
u3.encerrar_votacao()
u4.encerrar_votacao()
