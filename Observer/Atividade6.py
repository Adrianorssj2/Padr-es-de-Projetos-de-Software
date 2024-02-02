class Observer:
    def update(self, subject):
        pass

class Subject:
    def __init__(self):
        self.observers = [] 

    def attach(self, observer):
        self.observers.append(observer) 

    def detach(self, observer):
        self.observers.remove(observer) 

    def notify(self):
        for observer in self.observers: 
            observer.update(self)


class Product(Subject):
    def __init__(self, name, price):
        super().__init__() 
        self.name = name 
        self.price = price 

    def get_price(self):
        return self.price 

    def set_price(self, price):
        self.price = price 
        self.notify() 


class Customer(Observer):
    def __init__(self, name):
        self.name = name 

    def update(self, subject):
        print(f"{self.name} recebeu uma notificação: O preço do produto {subject.name} mudou para R$ {subject.get_price()}") 


p1 = Product("Camiseta", 50)
p2 = Product("Calça", 100)
c1 = Customer("Adriano")
c2 = Customer("Bruno")

p1.attach(c1)
p1.attach(c2)
p2.attach(c1)

p1.set_price(40)
p2.set_price(120)
