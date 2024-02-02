from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self, data):
        pass

class ReportFactory(ABC):
    @abstractmethod
    def produce_pdf(self) -> Report:
        pass
   
    @abstractmethod
    def produce_csv(self) -> Report:
        pass
   
    @abstractmethod
    def produce_html(self) -> Report:
        pass

class PDFReport(Report):
    def generate(self, data):
        print("Gerando um relatório em PDF.")
        print(f"Nome: {data['nome']}")
        print(f"Idade: {data['idade']}")
        print(f"Profissão: {data['profissão']}")

class CSVReport(Report):
    def generate(self, data):
        print("Gerando um relatório em CSV.")
        print(f"Nome,Idade,Profissão")
        print(f"{data['nome']},{data['idade']},{data['profissão']}")

class HTMLReport(Report):
    def generate(self, data):
        print("Gerando um relatório em HTML.")
        print(f"<html>")
        print(f"<head>")
        print(f"<title>Relatório</title>")
        print(f"</head>")
        print(f"<body>")
        print(f"<h1>Relatório</h1>")
        print(f"<p>Nome: {data['nome']}</p>")
        print(f"<p>Idade: {data['idade']}</p>")
        print(f"<p>Profissão: {data['profissão']}</p>")
        print(f"</body>")
        print(f"</html>")

class FinancialReportFactory(ReportFactory):
    def produce_pdf(self) -> Report:
        return PDFReport()

    def produce_csv(self) -> Report:
        return CSVReport()

    def produce_html(self) -> Report:
        return HTMLReport()

class AcademicReportFactory(ReportFactory):
    def produce_pdf(self) -> Report:
        return PDFReport()

    def produce_csv(self) -> Report:
        return CSVReport()

    def produce_html(self) -> Report:
        return HTMLReport()

def main():
    financial_factory = FinancialReportFactory()
    academic_factory = AcademicReportFactory()

    data = {
        "nome": "Adriano",
        "idade": 23,
        "profissão": "Estudante"
    }

    report1 = financial_factory.produce_pdf()
    report2 = financial_factory.produce_csv()
    report3 = financial_factory.produce_html()

    report4 = academic_factory.produce_pdf()
    report5 = academic_factory.produce_csv()
    report6 = academic_factory.produce_html()

    report1.generate(data)
    report2.generate(data)
    report3.generate(data)

    report4.generate(data)
    report5.generate(data)
    report6.generate(data)

if __name__ == "__main__":
    main()
