from abc import ABC, abstractmethod

class Widget(ABC):
    @abstractmethod
    def draw(self):
        pass

class WidgetFactory(ABC):
    @abstractmethod
    def create_button(self) -> Widget:
        pass
   
    @abstractmethod
    def create_textbox(self) -> Widget:
        pass
   
    @abstractmethod
    def create_menu(self) -> Widget:
        pass

class Button(Widget):
    def __init__(self, text):
        self.text = text

    def draw(self):
        print(f"Desenhando um botão com o texto: {self.text}")

class Textbox(Widget):
    def __init__(self, placeholder):
        self.placeholder = placeholder

    def draw(self):
        print(f"Desenhando uma caixa de texto com o placeholder: {self.placeholder}")

class Menu(Widget):
    def __init__(self, items):
        self.items = items

    def draw(self):
        print(f"Desenhando um menu com os itens: {self.items}")

class ModernWidgetFactory(WidgetFactory):
    def create_button(self) -> Widget:
        return Button("Clique aqui")

    def create_textbox(self) -> Widget:
        return Textbox("Digite algo")

    def create_menu(self) -> Widget:
        return Menu(["Arquivo", "Editar", "Ajuda"])

class ClassicWidgetFactory(WidgetFactory):
    def create_button(self) -> Widget:
        return Button("OK")

    def create_textbox(self) -> Widget:
        return Textbox("")

    def create_menu(self) -> Widget:
        return Menu(["File", "Edit", "Help"])

def main():
    modern_factory = ModernWidgetFactory()
    classic_factory = ClassicWidgetFactory()

    button1 = modern_factory.create_button()
    textbox1 = modern_factory.create_textbox()
    menu1 = modern_factory.create_menu()

    button2 = classic_factory.create_button()
    textbox2 = classic_factory.create_textbox()
    menu2 = classic_factory.create_menu()

    button1.draw()
    textbox1.draw()
    menu1.draw()

    button2.draw()
    textbox2.draw()
    menu2.draw()

if __name__ == "__main__":
    main()
