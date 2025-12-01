from infos.Cursos import DisciplinasOptativas

class Campus():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cursos = []
        self.disciplinas_optativas = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def adicionar_disciplinas_optativas(self, disciplina):
        self.disciplinas_optativas.append(disciplina)

    def __str__(self):
        return f"Campus: {self.nome} - Endereço: {self.endereco}"

class Endereco:
    def __init__(self, bairro, cidade):
        self.bairro = bairro
        self.cidade = cidade

    def __str__(self):
        return f"{self.bairro} - {self.cidade}"