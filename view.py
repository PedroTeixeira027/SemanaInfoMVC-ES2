# view.py

from controller import InscricaoController

class InscricaoView:
    """
    Classe responsável pela interface do sistema (console).
    
    Princípios aplicados:
    - Separação de interesses: apenas interação com o usuário.
    - Alta coesão: apenas funções relacionadas à apresentação.
    """

    def __init__(self):
        self.controller = InscricaoController()

    def exibir_menu(self):
        """
        Exibe o menu principal do sistema.
        """
        while True:
            print("\n=== Semana da Informática ===")
            print("1. Fazer Inscrição")
            print("2. Listar Inscrições")
            print("3. Confirmar Pagamento")
            print("4. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.fazer_inscricao()
            elif escolha == '2':
                self.listar_inscricoes()
            elif escolha == '3':
                self.confirmar_pagamento()
            elif escolha == '4':
                print("\nObrigado por se inscrever na Semana da Informática! Abraços! Ass: ItiBit")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def fazer_inscricao(self):
        """
        Coleta dados do usuário para fazer uma nova inscrição.
        """
        print("\n--- Nova Inscrição ---")
        nome = input("Nome completo: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        escolaridade = input("Escolaridade: ")
        email = input("Email: ")
        telefone = input("Telefone: ")

        inscricao = self.controller.fazer_inscricao(nome, data_nascimento, escolaridade, email, telefone)

        print(f"\nInscrição realizada com sucesso!")
        print(f"Valor da taxa de inscrição: R$15,00")
        print(f"Chave Pix para pagamento: {inscricao.chave_pix}")

    def listar_inscricoes(self):
        """
        Lista todas as inscrições feitas até agora.
        """
        print("\n--- Lista de Inscrições ---")
        inscricoes = self.controller.listar_inscricoes()

        if not inscricoes:
            print("Nenhuma inscrição encontrada.")
            return

        for inscricao in inscricoes:
            print(f"\nID: {inscricao[0]}")
            print(f"Nome: {inscricao[1]}")
            print(f"Data de Nascimento: {inscricao[2]}")
            print(f"Escolaridade: {inscricao[3]}")
            print(f"Email: {inscricao[4]}")
            print(f"Telefone: {inscricao[5]}")
            print(f"Chave Pix: {inscricao[6]}")
            print(f"Status de Pagamento: {inscricao[7]}")

    def confirmar_pagamento(self):
        """
        Permite confirmar o pagamento de uma inscrição.
        """
        print("\n--- Confirmar Pagamento ---")
        try:
            id_inscricao = int(input("Digite o ID da inscrição para confirmar pagamento: "))
            self.controller.confirmar_pagamento(id_inscricao)
            print("Pagamento confirmado com sucesso!")
        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")