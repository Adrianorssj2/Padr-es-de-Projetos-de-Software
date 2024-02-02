class RelatorioFinanceiro:
    def __init__(self, dados):
        self.dados = dados 

    def gerar(self):
        raise NotImplementedError


class RelatorioHTML(RelatorioFinanceiro):
    def gerar(self):
        html = "<html><head><title>Relatório Financeiro</title></head><body>"
        html += "<h1>Relatório Financeiro</h1>"
        for chave, valor in self.dados.items():
            html += f"<p>{chave}: {valor}</p>"
        html += "</body></html>"
        return html

class RelatorioPDF(RelatorioFinanceiro):
    def gerar(self):
        pdf = "Relatório Financeiro\n"
        for chave, valor in self.dados.items():
            pdf += f"{chave}: {valor}\n"
        return pdf

class RelatorioSimples(RelatorioFinanceiro):
    def gerar(self):
        simples = "Relatório Financeiro Simples\n"
        simples += f"Receita: {self.dados['receita']}\n"
        simples += f"Despesa: {self.dados['despesa']}\n"
        simples += f"Lucro: {self.dados['lucro']}\n"
        return simples

class RelatorioCompleto(RelatorioFinanceiro):
    def gerar(self):
        completo = "Relatório Financeiro Completo\n"
        for chave, valor in self.dados.items():
            completo += f"{chave}: {valor}\n"
        completo += "Análise Financeira:\n"
        completo += f"Margem de lucro: {self.dados['lucro'] / self.dados['receita']}\n"
        completo += f"Retorno sobre o investimento: {self.dados['lucro'] / self.dados['investimento']}\n"
        return completo

class FabricaRelatorio:
    def criar_relatorio(self, tipo, dados):
        if tipo == "HTML":
            return RelatorioHTML(dados)
        elif tipo == "PDF":
            return RelatorioPDF(dados)
        elif tipo == "Simples":
            return RelatorioSimples(dados)
        elif tipo == "Completo":
            return RelatorioCompleto(dados)
        else:
            raise ValueError(f"Tipo de relatório inválido: {tipo}")

if __name__ == "__main__":
    fabrica = FabricaRelatorio()

    dados = {
        "receita": 100000,
        "despesa": 80000,
        "lucro": 20000,
        "investimento": 50000,
        "imposto": 15000,
        "divida": 30000
    }

    tipos = ["HTML", "PDF", "Simples", "Completo"]
    for tipo in tipos:
        relatorio = fabrica.criar_relatorio(tipo, dados)
        print(f"Relatório {tipo}:")
        print(relatorio.gerar())
        print()
