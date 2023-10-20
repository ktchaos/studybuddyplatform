class MenuOpcaoInvalida(Exception):
    "valor da opcao invalida"
    def __init__(self, message="valor da opcao invalida"):
        self.message = message
        super().__init__(self.message)
