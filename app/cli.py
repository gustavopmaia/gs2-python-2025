from data.carreiras import carreiras
from data.competencias import competencias_disponiveis
from domain.competencia import Competencia
from domain.perfil import Perfil
from services.recomendador import Recomendador


def exibir_menu():
    print("\n=== FUTURE AT WORK - ORIENTAÇÃO DE CARREIRA ===")
    print("1. Criar perfil")
    print("2. Adicionar competência ao perfil")
    print("3. Listar competências")
    print("4. Gerar recomendação")
    print("5. Sair")
    return input("Escolha uma opção: ")


def criar_perfil():
    nome = input("Digite o nome do usuário: ")
    if not nome:
        print("O nome não pode ser vazio!")
        return None
    print(f"Perfil criado para {nome}.")
    return Perfil(nome)


def adicionar_competencia(perfil):
    if not perfil:
        print("Crie um perfil primeiro!")
        return perfil

    print("\n=== Competências disponíveis ===")
    nomes = list(competencias_disponiveis.keys())
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome.capitalize()} ({competencias_disponiveis[nome]})")

    try:
        escolha = int(input("\nSelecione o número da competência: "))
        nivel = int(input("Nível (0 a 10): "))
    except ValueError:
        print("Entrada inválida!")
        return perfil

    if escolha < 1 or escolha > len(nomes) or nivel < 0 or nivel > 10:
        print("Opção ou nível inválido!")
        return perfil

    nome_comp = nomes[escolha - 1]
    tipo = competencias_disponiveis[nome_comp]
    perfil.adicionar_competencia(Competencia(nome_comp, tipo, nivel))
    print("Competência adicionada!")
    return perfil


def listar_competencias(perfil):
    if not perfil:
        print("Crie um perfil primeiro!")
        return

    print("\n=== Competências do Perfil ===")
    if not perfil.competencias:
        print("Nenhuma competência cadastrada.")
    else:
        for competencia in perfil.listar_competencias():
            print(" -", competencia)


def gerar_recomendacao(perfil, recomendador):
    if not perfil:
        print("Crie um perfil primeiro!")
        return

    print("\nAnalisando perfil...\n")
    resultados = recomendador.avaliar(perfil)

    for resultado in resultados:
        print(f"Carreira: {resultado['carreira']}")
        print(f"Afinidade: {round(resultado['score'] * 100)}%")
        if resultado["faltantes"]:
            print("Pontos a melhorar:")
            for item, deficit in resultado["faltantes"]:
                print(f" - {item} (faltam {deficit} pontos)")
        else:
            print("Requisitos completamente atendidos!")
        print("-" * 40)


def run_cli():
    perfil = None
    recomendador = Recomendador(carreiras)

    while True:
        opcao = exibir_menu()
        if opcao == "1":
            perfil = criar_perfil()
        elif opcao == "2":
            perfil = adicionar_competencia(perfil)
        elif opcao == "3":
            listar_competencias(perfil)
        elif opcao == "4":
            gerar_recomendacao(perfil, recomendador)
        elif opcao == "5":
            print("Encerrando... Obrigado por utilizar o sistema!")
            break
        else:
            print("Opção inválida!")
