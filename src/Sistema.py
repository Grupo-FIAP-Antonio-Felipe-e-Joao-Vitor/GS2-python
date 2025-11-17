import time
import os
from src.obter_tendencias_emprego import obter_tendencias_emprego

class Sistema:
    
    def __init__(self, headers="", api=""):
        
        self.headers = headers
        self.api = api
        self.opcoes = ["1", "2", "3", "q"]

    def limpar_terminal (self):
        if os.name == "nt":
            return os.system("cls")
        else:
            return os.system("clear")

    def voltar_menu (self):
        str(input("Pressione ENTER para voltar ao menu principal."))
        return self.menu()
    
    def exibir_empregos (self, empregos):
        if len(empregos) == 0:
            print("O sistema demorou muito para responder.")
            print("Tente novamente.")

        for emprego in empregos:
            print(f"Emprego: {emprego["titulo"]}")
            print(f"Empresa: {emprego["empresa"]}")
            print(f"Local: {emprego["local"]}")
            print(f"Tipo: {emprego["tipo"]}")
            print(f"Publicado: {emprego["publicado"]}")
            print(f"Link: {emprego["link"]}")
            print("-" * 30)
            print()
            
        self.voltar_menu()

    def menu_tendencias_emprego (self):
        self.limpar_terminal()
        print("--- Tendencias de emprego ---")
        
        empregos = obter_tendencias_emprego(self.api, self.headers)

        self.exibir_empregos(empregos)
        

    def menu_filtrar_empregos (self):
        self.limpar_terminal()
        print("--- Filtrar empregos ---")
        print("Digite V para voltar ao menu.")

        palavra_chave = ""
        while not palavra_chave:
            palavra_chave = str(input("Digite uma área que você tem interesse (ex: python): ")).strip(" ").lower()
            if palavra_chave == "v":
                self.menu()
            else:

                empregos = obter_tendencias_emprego(self.api, self.headers, palavra_chave)
                self.exibir_empregos(empregos)


    def menu_calcular_crescimento (self):
        pass


    def menu (self):
        self.limpar_terminal()
        print("--- Menu ---")

        print("1. Exibir tendencias de emprego")
        print("2. Filtrar empregos")
        print("3. Calcular taxa de crescimento")
        print("Q. Sair")

        escolha = str(input(">>> ")).strip(" ").lower()
        
        if escolha in self.opcoes:
            if escolha == "1":
                return self.menu_tendencias_emprego()
            if escolha == "2":
                return self.menu_filtrar_empregos()
            if escolha == "3":
                return self.menu_calcular_crescimento()
            if escolha == "q":
                print("Saindo do sistema...")
                return exit()
        else:
            print("Opção inválida.")
            time.sleep(1)
            return
        