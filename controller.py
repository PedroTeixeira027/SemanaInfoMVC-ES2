# controller.py

from model import Inscricao, BancoDeDados

class InscricaoController:
    """
    Controlador que gerencia as operações de inscrição.
    
    Princípios aplicados:
    - Separação de interesses: separa a lógica da interface.
    - Baixo acoplamento: depende apenas de interfaces necessárias (model).
    """

    def __init__(self):
        self.banco = BancoDeDados()

    def fazer_inscricao(self, nome, data_nascimento, escolaridade, email, telefone):
        """
        Cria uma nova inscrição e salva no banco de dados.
        """
        nova_inscricao = Inscricao(nome, data_nascimento, escolaridade, email, telefone)
        self.banco.adicionar_inscricao(nova_inscricao)
        return nova_inscricao

    def listar_inscricoes(self):
        """
        Retorna a lista de todas as inscrições cadastradas.
        """
        return self.banco.listar_inscricoes()

    def confirmar_pagamento(self, id_inscricao):
        """
        Atualiza o status de pagamento de uma inscrição.
        """
        self.banco.atualizar_pagamento(id_inscricao)