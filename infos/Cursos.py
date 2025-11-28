class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []
        self.disciplinas_optativas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def adicionar_disciplina_optativa(self, disciplina):
        self.disciplinas_optativas.append(disciplina)

    def __str__(self):
        return f"{self.nome}"

class Disciplinas(Curso):
    def __init__(self, nome, carga_horaria):
        super().__init__(nome)
        self.nome = nome
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"{self.nome} ({self.carga_horaria}h)"