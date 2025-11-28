from Cursos import Curso
class Disciplinas(Curso):
    def __init__(self, nome, carga_horaria):
        super().__init__(nome)
        self.nome = nome
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"{self.nome} ({self.carga_horaria}h)"