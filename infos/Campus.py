class Campus:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cursos = []


    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def __str__(self):
        return f"Campus: {self.nome} - Endereço: {self.endereco}"