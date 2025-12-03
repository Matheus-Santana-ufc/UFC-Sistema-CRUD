from infos.Cursos import DisciplinasOptativas, Curso

class Campus:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cursos = []
        self.disciplinas_optativas = []

    def adicionar_curso(self, curso):
        if isinstance(curso, Curso):
            self.cursos.append(curso)
        else:
            print("❌ Erro: O objeto fornecido não é um Curso válido.")

    def adicionar_disciplinas_optativas(self, disciplina):
        if isinstance(disciplina, DisciplinasOptativas):
            self.disciplinas_optativas.append(disciplina)
        else:
            print("❌ Erro: O objeto não é uma Disciplina Optativa válida.")

    def __str__(self):
        return f"Campus: {self.nome} - Endereço: {self.endereco}"

class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

    def __str__(self):
        return f"{self.rua} - {self.cidade}"