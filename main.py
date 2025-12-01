from infos.CRUD import CRUD

def main():
    sistema = CRUD()
    sistema.criar_campus("Jardins de Anita",  "Rua Francisco José Oliveira","Itapajé")
    sistema.adicionar_curso_ao_campus("Jardins de Anita", "SI")
    sistema.adicionar_curso_ao_campus("Jardins de Anita", "CD")
    sistema.adicionar_curso_ao_campus("Jardins de Anita", "ADS")

    while True:
        print("\n" + "=" * 31)
        print(" Universidade Federal do Ceará ")
        print("=" * 31)
        print("1. Novo Campus")
        print("2. Adicionar Curso a um Campus")
        print("3. Adicionar Disciplina a um Curso")
        print("4. Adicionar Disciplina Optativa a um Campus")
        print("5. Listar")
        print("6. Atualizar Nome de Campus")
        print("7. Deletar Campus")
        print("8. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Campus: ")
            rua = input("Rua: ")
            cidade = input("Cidade: ")
            sistema.criar_campus(nome, rua, cidade)

        elif opcao == '2':
            campus_alvo = input("Nome do Campus onde o curso será criado: ")
            nome_curso = input("Nome do novo Curso: ")
            sistema.adicionar_curso_ao_campus(campus_alvo, nome_curso)

        elif opcao == '3':
            campus_alvo = input("Nome do Campus: ")
            curso_alvo = input("Nome do Curso: ")
            nome_disc = input("Nome da Disciplina: ")
            horas = input("Carga Horária: ")
            sistema.adicionar_disciplina_ao_curso(campus_alvo, curso_alvo, nome_disc, horas)

        elif opcao == '5':
            sistema.listar()

        elif opcao == '6':
            antigo = input("Nome atual do Campus: ")
            novo = input("Novo nome para o Campus: ")
            sistema.atualizar_nome_campus(antigo, novo)

        elif opcao == '7':
            nome = input("Nome do Campus a deletar: ")
            sistema.remover_campus(nome)
        elif opcao == '4':
            campus_alvo = input("Nome do Campus: ")
            nome_disc = input("Nome da Disciplina: ")
            horas = input("Carga Horária: ")
            sistema.adicionar_disciplinas_optativas(campus_alvo, nome_disc, horas)
        elif opcao == '8':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()