class TV:
    def __init__(self):
        self.ligada = False
        self.volume = 10
        self.entrada = "DVD"

    def ligar(self):
        self.ligada = True
        print("TV ligada")

    def desligar(self):
        self.ligada = False
        print("TV desligada")

    def ajustar_volume(self, valor):
        self.volume += valor
        print(f"Volume da TV: {self.volume}")

    def escolher_entrada(self, entrada):
        self.entrada = entrada
        print(f"Entrada da TV: {self.entrada}")

class SomSurround:
    def __init__(self):
        self.ligado = False
        self.volume = 10
        self.entrada = "DVD"
        self.modo = "Estereo"

    def ligar(self):
        self.ligado = True
        print("Som Surround ligado")

    def desligar(self):
        self.ligado = False
        print("Som Surround desligado")

    def ajustar_volume(self, valor):
        self.volume += valor
        print(f"Volume do Som Surround: {self.volume}")

    def escolher_entrada(self, entrada):
        self.entrada = entrada
        print(f"Entrada do Som Surround: {self.entrada}")

    def escolher_modo(self, modo):
        self.modo = modo
        print(f"Modo do Som Surround: {self.modo}")

class DVD:
    def __init__(self):
        self.ligado = False
        self.playing = False

    def ligar(self):
        self.ligado = True
        print("DVD ligado")

    def desligar(self):
        self.ligado = False
        print("DVD desligado")

    def play(self):
        self.playing = True
        print("DVD reproduzindo")

    def pause(self):
        self.playing = False
        print("DVD pausado")

class SintonizadorTV:
    def __init__(self):
        self.ligado = False
        self.canal = "AR"

    def ligar(self):
        self.ligado = True
        print("Sintonizador de TV ligado")

    def desligar(self):
        self.ligado = False
        print("Sintonizador de TV desligado")

    def escolher_canal(self, canal):
        self.canal = canal
        print(f"Canal do Sintonizador de TV: {self.canal}")

class HomeTheater:
    def __init__(self):
        self.tv = TV()
        self.som = SomSurround()
        self.dvd = DVD()
        self.sintonizador = SintonizadorTV()

    def assistir_dvd(self):
        self.tv.ligar()
        self.tv.escolher_entrada("DVD")
        self.som.ligar()
        self.som.escolher_entrada("DVD")
        self.som.escolher_modo("Estereo")
        self.dvd.ligar()
        self.dvd.play()

    def assistir_tv(self):
        self.tv.ligar()
        self.tv.escolher_entrada("TV")
        self.som.ligar()
        self.som.escolher_entrada("TV")
        self.som.escolher_modo("Mono")
        self.sintonizador.ligar()
        self.sintonizador.escolher_canal("Cabo")

    def desligar_tudo(self):
        self.tv.desligar()
        self.som.desligar()
        self.dvd.desligar()
        self.sintonizador.desligar()

if __name__ == "__main__":
    home_theater = HomeTheater()

    print("Assistir um DVD:")
    home_theater.assistir_dvd()
    print()

    print("Assistir TV:")
    home_theater.assistir_tv()
    print()

    print("Desligar tudo:")
    home_theater.desligar_tudo()
    print()
