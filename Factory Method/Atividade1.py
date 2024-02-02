from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def load(self):
        pass

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self, file_type: str) -> Document:
        pass

class TXT(Document):
    def load(self):
        print("Carregando um documento de texto.")

class PNG(Document):
    def load(self):
        print("Carregando um documento do tipo imagem.")

class HTML(Document):
    def load(self):
        print("Carregando um documento HTML.")

class ConcreteDocumentFactory(DocumentFactory):
    def create_document(self, file_type: str) -> Document:
        if file_type == "txt":
            return TXT()
        elif file_type == "png":
            return PNG()
        elif file_type == "html":
            return HTML()
        else:
            raise ValueError("Tipo de arquivo inválido.")

def main():
    document_factory = ConcreteDocumentFactory()

    pdf = document_factory.create_document("txt")
    word = document_factory.create_document("png")
    html = document_factory.create_document("html")

    pdf.load()
    word.load()
    html.load()

if __name__ == "__main__":
    main()
