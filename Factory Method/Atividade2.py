from abc import ABC, abstractmethod
import random

class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def flee(self):
        pass

    @abstractmethod
    def die(self):
        pass

class Soldier(Enemy):
    def attack(self):
        print("O soldado atira com sua arma.")

    def flee(self):
        print("O soldado corre para se proteger.")

    def die(self):
        print("O soldado cai no chão.")

class Monster(Enemy):
    def attack(self):
        print("O monstro morde com seus dentes afiados.")

    def flee(self):
        print("O monstro se esconde na escuridão.")

    def die(self):
        print("O monstro solta um grito agudo.")

class Boss(Enemy):
    def attack(self):
        print("O chefe lança uma magia poderosa.")

    def flee(self):
        print("O chefe se teleporta para outro lugar.")

    def die(self):
        print("O chefe explode em uma nuvem de fumaça.")

def create_enemy(level):
    enemy_type = random.choice(["soldado", "monstro", "chefe"])
    if enemy_type == "soldado":
        enemy = Soldier()
    elif enemy_type == "monstro":
        enemy = Monster()
    else:
        enemy = Boss()
    return enemy

def main():
    level = 1
    max_level = 10
    while level <= max_level:
        enemy = create_enemy(level)
        print(f"Você encontrou um {type(enemy).__name__} no nível {level}.")
        enemy.attack()
        print("Você revida com sua espada.")
        enemy.die()
        print(f"Você derrotou o {type(enemy).__name__} e avançou para o próximo nível.")
        level += 1
    print("Parabéns, você completou o jogo!")

if __name__ == "__main__":
    main()
