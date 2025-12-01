from infos.Campus import Campus
from infos.Cursos import Curso
from infos.Campus import Endereco
from infos.Cursos import Disciplinas

class CRUD:
    def __init__(self):
        self.campus = []

    def criar_campus(self, nome_campus, rua, cidade):
        novo_endereco = Endereco(rua, cidade)
        novo_campus = Campus(nome_campus, novo_endereco)
        self.campus.append(novo_campus)
        print(f"✅ Campus '{nome_campus}' criado com sucesso!")

    def adicionar_curso_ao_campus(self, nome_campus_alvo, nome_curso):
        campus = self.buscar_campus(nome_campus_alvo)
        if campus:
            novo_curso = Curso(nome_curso)
            campus.adicionar_curso(novo_curso)
            print(f"✅ Curso '{nome_curso}' adicionado ao campus '{campus.nome}'.")
        else:
            print("❌ Campus não encontrado.")
    def adicionar_disciplinas_optativas(self, nome_campus, nome_disciplina, horas):
        campus = self.buscar_campus(nome_campus)
        if campus:
            if campus:
                nova_disciplina = Disciplinas(nome_disciplina, horas)
                campus.adicionar_disciplinas_optativas(nova_disciplina)
            print(f"✅ Disciplina '{nome_disciplina}' adicionada ao Campus '{nome_campus}'.")
        else:
            print("❌ Curso não encontrado neste campus.")
    def adicionar_disciplina_ao_curso(self, nome_campus, nome_curso, nome_disciplina, horas):
        campus = self.buscar_campus(nome_campus)
        if campus:
            curso_alvo = next((c for c in campus.cursos if c.nome == nome_curso), None)
            if curso_alvo:
                nova_disciplina = Disciplinas(nome_disciplina, horas)
                curso_alvo.adicionar_disciplina(nova_disciplina)
                print(f"✅ Disciplina '{nome_disciplina}' adicionada ao curso '{nome_curso}'.")
            else:
                print("❌ Curso não encontrado neste campus.")
        else:
            print("❌ Campus não encontrado.")

    def listar(self):
        if not self.campus:
            print("\n--- Nenhum dado cadastrado ---")
            return

        print("\n=== RELATÓRIO GERAL ===")
        for campus in self.campus:
            print(f"\n🏢 {campus}")
            if not campus.cursos:
                print("   └── (Sem cursos)")
            for curso in campus.cursos:
                print(f"   🎓 Curso: {curso}")
                if not curso.disciplinas:
                    print("      └── (Sem disciplinas)")
                for disciplina in curso.disciplinas:
                    print(f"      📚 {disciplina}")
            if campus.disciplinas_optativas:
                print(f"\n    ⭐ DISCIPLINAS OPTATIVAS ofertadas no Campus {campus.nome}:")
                for disc_opt in campus.disciplinas_optativas:
                    print(f"      - {disc_opt}")
            else:
                print("    (Nenhuma disciplina optativa cadastrada neste campus)")


    def atualizar_nome_campus(self, nome_antigo, novo_nome):
        campus = self.buscar_campus(nome_antigo)
        if campus:
            campus.nome = novo_nome
            print(f"✅ Campus renomeado para '{novo_nome}'.")
        else:
            print("❌ Campus não encontrado.")

    def remover_campus(self, nome_campus):
        campus = self.buscar_campus(nome_campus)
        if campus:
            self.campus.remove(campus)
            print(f"🗑️ Campus '{nome_campus}' removido do sistema.")
        else:
            print("❌ Campus não encontrado.")

    def buscar_campus(self, nome):
        for i in self.campus:
            if i.nome == nome:
                return i
        return None