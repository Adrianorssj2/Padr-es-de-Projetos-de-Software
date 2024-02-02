from abc import ABC, abstractmethod

class Event(ABC):
    @abstractmethod
    def log(self):
        pass

class EventFactory(ABC):
    @abstractmethod
    def create_event(self, event_type: str) -> Event:
        pass

class ErrorEvent(Event):
    def log(self):
        print("Registrando um evento de erro.")

class WarningEvent(Event):
    def log(self):
        print("Registrando um evento de aviso.")

class InfoEvent(Event):
    def log(self):
        print("Registrando um evento informativo.")

class SimpleEventFactory(EventFactory):
    def create_event(self, event_type: str) -> Event:
        if event_type == "error":
            return ErrorEvent()
        elif event_type == "warning":
            return WarningEvent()
        elif event_type == "info":
            return InfoEvent()
        else:
            raise ValueError(f"Tipo de evento inválido: {event_type}")

def main():
    event_factory = SimpleEventFactory()

    event1 = event_factory.create_event("error")
    event2 = event_factory.create_event("warning")
    event3 = event_factory.create_event("info")

    event1.log()
    event2.log()
    event3.log()

if __name__ == "__main__":
    main()
