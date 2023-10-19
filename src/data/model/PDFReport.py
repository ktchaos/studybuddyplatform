from .Report import ReportTemplate

class PDFReport(ReportTemplate):
    def generateHeader(self):
        print("Gerando cabeçalho do relatório PDF")

    def generateBody(self):
        print("Gerando corpo do relatório PDF")
        # Lógica para gerar o corpo do relatório em PDF

    def generateFooter(self):
        print("Gerando rodapé do relatório PDF")