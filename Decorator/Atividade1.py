class Hamburger:
    def __init__(self):
        self.nome = "Hambúrguer"
        self.preco = 5.0

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

class Decorator(Hamburger):
    def __init__(self, hamburger):
        self.hamburger = hamburger

    def get_nome(self):
        return self.hamburger.get_nome() + " com " + self.nome

    def get_preco(self):
        return self.hamburger.get_preco() + self.preco

class Queijo(Decorator):
    def __init__(self, hamburger):
        super().__init__(hamburger)
        self.nome = "queijo"
        self.preco = 1.0

class Bacon(Decorator):
    def __init__(self, hamburger):
        super().__init__(hamburger)
        self.nome = "bacon"
        self.preco = 2.0

class Alface(Decorator):
    def __init__(self, hamburger):
        super().__init__(hamburger)
        self.nome = "alface"
        self.preco = 0.5

class Tomate(Decorator):
    def __init__(self, hamburger):
        super().__init__(hamburger)
        self.nome = "tomate"
        self.preco = 0.5
        
class Ovo(Decorator):
    def __init__(self, hamburger):
        super().__init__(hamburger)
        self.nome = "ovo"
        self.preco = 1.5

class Cebola(Decorator):
    def __init__(self, hamburger):
        super().__init__(hamburger)
        self.nome = "cebola"
        self.preco = 0.5

class Picles(Decorator):
    def __init__(self, hamburger):
        super().__init__(hamburger)
        self.nome = "picles"
        self.preco = 0.5

class Molho(Decorator):
    def __init__(self, hamburger, sabor):
        super().__init__(hamburger)
        self.nome = f"molho {sabor}"
        self.preco = 0.5
        self.sabor = sabor 

h1 = Hamburger()
print(h1.get_nome()) 
print(h1.get_preco()) 

h2 = Queijo(Bacon(Hamburger()))
print(h2.get_nome()) 
print(h2.get_preco()) 

h3 = Alface(Tomate(Hamburger()))
print(h3.get_nome()) 
print(h3.get_preco()) 

h4 = Ovo(Cebola(Hamburger()))
print(h4.get_nome()) 
print(h4.get_preco())


h5 = Picles(Molho(Hamburger(), "barbecue"))
print(h5.get_nome()) 
print(h5.get_preco()) 
