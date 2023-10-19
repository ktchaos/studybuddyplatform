from .Report import ReportTemplate

class HTMLReport(ReportTemplate):
    def generateHeader(self):
        print("<html><head><title>Relatório HTML</title></head><body>")

    def generateBody(self):
        print("<h1>Estatísticas de Acesso em HTML</h1>")
        # Lógica para gerar o corpo do relatório em HTML

    def generateFooter(self):
        print("</body></html>")