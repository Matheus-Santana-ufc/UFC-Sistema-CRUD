class Endereco:
    def __init__(self,bairro,cidade):

        self.bairro = bairro
        self.cidade = cidade

    def __str__(self):
        return f"{self.bairro} - {self.cidade}"