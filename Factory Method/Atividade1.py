from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def load(self):
        pass

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self, file_type: str) -> Document:
        pass

class PDF(Document):
    def load(self):
        print("Carregando um documento PDF.")

class word(Document):
    def load(self):
        print("Carregando um documento Word.")

class HTML(Document):
    def load(self):
        print("Carregando um documento HTML.")

class ConcreteDocumentFactory(DocumentFactory):
    def create_document(self, file_type: str) -> Document:
        if file_type == "PDF":
            return PDF()
        elif file_type == "word":
            return word()
        elif file_type == "html":
            return HTML()
        else:
            raise ValueError("Tipo de arquivo inválido.")

def main():
    document_factory = ConcreteDocumentFactory()

    pdf = document_factory.create_document("PDF")
    word = document_factory.create_document("word")
    html = document_factory.create_document("html")

    pdf.load()
    word.load()
    html.load()

if __name__ == "__main__":
    main()
