import time
import os
from src.obter_tendencias_emprego import obter_tendencias_emprego
from src.calcular_taxa_crescimento_individual import calcular_taxa_crescimento_individual
from src.calcular_taxa_crescimento import calcular_taxa_crescimento


class Sistema:
    
    # Inicializa atributos básicos do sistema
    def __init__(self, headers="", api=""):
        self.headers = headers                     # Guarda os headers da API
        self.api = api                             # Guarda a URL base da API
        self.opcoes = ["1", "2", "3", "4", "q"]    # Opções aceitas no menu principal


    # Limpa o terminal de acordo com o sistema operacional
    def limpar_terminal(self):
        if os.name == "nt":        # Windows
            return os.system("cls")
        else:                      # Linux / Mac
            return os.system("clear")


    # Pausa o sistema e retorna ao menu inicial
    def voltar_menu(self):
        input("Pressione ENTER para voltar ao menu principal. ")
        return self.menu()


    # Exibe a lista de empregos formatada
    def exibir_empregos(self, empregos):

        # Verifica se houve erro ou resposta vazia
        if len(empregos) == 0:
            print("O sistema demorou muito para responder.")
            print("Tente novamente.")
            return self.voltar_menu()

        # Exibe cada emprego com suas informações
        for emprego in empregos:
            print(f"Emprego: {emprego['titulo']}")
            print(f"Empresa: {emprego['empresa']}")
            print(f"Local: {emprego['local']}")
            print(f"Tipo: {emprego['tipo']}")
            print(f"Publicado: {emprego['publicado']}")
            print(f"Link: {emprego['link']}")
            print("-" * 30)
            print()

        self.voltar_menu()


    # Menu que exibe tendências de emprego gerais
    def menu_tendencias_emprego(self):
        self.limpar_terminal()
        print("--- Tendências de emprego ---")
        
        print("Carregando...")
        empregos = obter_tendencias_emprego(self.api, self.headers)

        self.exibir_empregos(empregos)


    # Menu para filtrar empregos por palavra-chave
    def menu_filtrar_empregos(self):
        self.limpar_terminal()
        print("--- Filtrar empregos ---")
        print("Digite V para voltar ao menu.")

        palavra_chave = ""

        # Solicita uma palavra-chave válida
        while not palavra_chave:
            palavra_chave = input("Digite uma área de interesse (ex: python): ").strip().lower()

            if palavra_chave == "v":
                return self.menu()

            print("Carregando...")
            empregos = obter_tendencias_emprego(self.api, self.headers, palavra_chave)
            return self.exibir_empregos(empregos)


    # Menu para calcular taxa de crescimento de uma profissão específica
    def menu_calcular_crescimento_individual(self):
        self.limpar_terminal()
        print("--- Calcular taxa de crescimento de uma profissão ---")

        profissao = input("Digite a profissão (ex: dev, IA, python): ").strip().lower()

        print("Carregando...")
        taxa = calcular_taxa_crescimento_individual(self.api, self.headers, profissao)

        print(f"A taxa de crescimento da profissão '{profissao}' é: {taxa:.2f}%")
        self.voltar_menu()


    # Menu para calcular taxa de crescimento de várias profissões
    def menu_calcular_crescimento(self):
        self.limpar_terminal()
        print("--- Calcular taxa de crescimento de várias profissões ---")
        print("Para parar de inserir, digite V.")

        profissoes = []

        # Recebe várias profissões até o usuário parar
        while True:
            profissao = input(f"Digite a {len(profissoes) + 1}ª área: ").strip().lower()

            if profissao == "v":
                break

            profissoes.append(profissao)
        
        print("Carregando...")
        taxa = calcular_taxa_crescimento(self.api, self.headers, profissoes)

        profissoes_formatada = ", ".join(profissoes)
        print(f"A soma das taxas de crescimento das profissões ({profissoes_formatada}) é: {taxa:.2f}%")

        self.voltar_menu()


    # Menu principal do sistema
    def menu(self):
        self.limpar_terminal()
        print("--- Menu ---")

        print("1. Exibir tendências de emprego")
        print("2. Filtrar empregos")
        print("3. Calcular taxa de crescimento individual")
        print("4. Calcular soma da taxa de crescimento de várias áreas")
        print("Q. Sair")

        escolha = input(">>> ").strip().lower()
        
        if escolha in self.opcoes:
            if escolha == "1":
                return self.menu_tendencias_emprego()
            if escolha == "2":
                return self.menu_filtrar_empregos()
            if escolha == "3":
                return self.menu_calcular_crescimento_individual()
            if escolha == "4":
                return self.menu_calcular_crescimento()
            if escolha == "q":
                print("Saindo do sistema...")
                return exit()

        else:
            print("Opção inválida.")
            time.sleep(1)
            return self.menu()
