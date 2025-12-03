class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        if isinstance(disciplina, Disciplinas):
            self.disciplinas.append(disciplina)
        else:
            print("❌ Erro: Objeto inválido. Esperava-se uma Disciplina.")

    def __str__(self):
        return f"{self.nome}"

class Disciplinas:
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"{self.nome} ({self.carga_horaria}h)"

class DisciplinasOptativas(Disciplinas):
    def __init__(self, nome, carga_horaria):
        super().__init__(nome, carga_horaria)
        self.nome = nome
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"📚 [OPTATIVA] {self.nome} ({self.carga_horaria}h)"