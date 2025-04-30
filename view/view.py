# view.py

from controller.controller import InscricaoController
from model.model import Inscricao
from datetime import datetime
import json
from model.model import r
import os

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
            print("\n===","\U0001F525","Semana da Informática","\U0001F525","===\n")
            print("1. Fazer Inscrição")
            print("2. Listar Inscrições")
            print("3. Confirmar Pagamento")
            print("4. Acessar o Chat")
            print("0. Sair")
            escolha = input("Escolha uma opção: ")
            os.system('cls' if os.name == 'nt' else 'clear')

            if escolha == '1':
                self.fazer_inscricao()
            elif escolha == '2':
                self.listar_inscricoes()
            elif escolha == '3':
                self.confirmar_pagamento()
            elif escolha == '4':
                self.chat()
            elif escolha == '0':
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
        print("\nObrigado por se inscrever na Semana da Informática! Abraços! Ass: ItiBit")
        os.system('cls' if os.name == 'nt' else 'clear')

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
        op = input("\nAperte qualquer tecla para sair...")
        os.system('cls' if os.name == 'nt' else 'clear')

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
        os.system('cls' if os.name == 'nt' else 'clear')


    def chat(self):
        print("\n","\U0001F525","CHAT","\U0001F525","\n")

        print("\n=== Mensagens anteriores ===\n")
        mensagens = r.lrange("chat:mensagens", 0, -1)
        if mensagens:
            for m in mensagens:
                msg = json.loads(m)
                print(f"[{msg['timestamp']}] {msg['nome']}: {msg['mensagem']}")
        else:
            print("Nenhuma mensagem ainda.")
        
        nome = input("\nDigite seu nome (como foi cadastrado): ")
        print("\nDigite sua mensagem. Escreva 'sair' para encerrar o chat.\n")

        while True:
            mensagem = input("> ")

            if mensagem.lower() == 'sair':
                print("\nEncerrando chat...")
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dado = {
                "nome": nome,
                "mensagem": mensagem,
                "timestamp": timestamp
            }

            r.rpush("chat:mensagens", json.dumps(dado))

