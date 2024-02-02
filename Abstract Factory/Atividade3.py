from abc import ABC, abstractmethod

class HousePart(ABC):
    @abstractmethod
    def build(self):
        pass

class Foundation(HousePart):
    def __init__(self, material):
        self.material = material

    def build(self):
        print(f"Construindo um alicerce de {self.material}.")

class Walls(HousePart):
    def __init__(self, material, color):
        self.material = material
        self.color = color

    def build(self):
        print(f"Construindo paredes de {self.material} na cor {self.color}.")

class Roof(HousePart):
    def __init__(self, material, shape):
        self.material = material
        self.shape = shape

    def build(self):
        print(f"Construindo um telhado de {self.material} no formato {self.shape}.")

class HousePartFactory(ABC):
    @abstractmethod
    def create_foundation(self) -> HousePart:
        pass
   
    @abstractmethod
    def create_walls(self) -> HousePart:
        pass
   
    @abstractmethod
    def create_roof(self) -> HousePart:
        pass

class ContemporaryHousePartFactory(HousePartFactory):
    def create_foundation(self) -> HousePart:
        return Foundation("concreto")

    def create_walls(self) -> HousePart:
        return Walls("vidro", "transparente")

    def create_roof(self) -> HousePart:
        return Roof("metal", "plano")

class ColonialHousePartFactory(HousePartFactory):
    def create_foundation(self) -> HousePart:
        return Foundation("pedra")

    def create_walls(self) -> HousePart:
        return Walls("madeira", "branca")

    def create_roof(self) -> HousePart:
        return Roof("telha", "triangular")

class House:
    def __init__(self, foundation: HousePart, walls: HousePart, roof: HousePart):
        self.foundation = foundation
        self.walls = walls
        self.roof = roof

    def build(self):
        self.foundation.build()
        self.walls.build()
        self.roof.build()

def main():
    contemporary_factory = ContemporaryHousePartFactory()
    colonial_factory = ColonialHousePartFactory()

    house1 = House(contemporary_factory.create_foundation(), contemporary_factory.create_walls(), contemporary_factory.create_roof())
    house2 = House(colonial_factory.create_foundation(), colonial_factory.create_walls(), colonial_factory.create_roof())

    house1.build()
    house2.build()

if __name__ == "__main__":
    main()
