# model.py

import sqlite3
import random
import string
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

class Inscricao:
    """
    Classe que representa uma inscrição na Semana da Informática.
    
    Princípios aplicados:
    - Abstração: simplifica o conceito de uma inscrição.
    - Encapsulamento: dados e comportamento juntos.
    """


    def __init__(self, nome, data_nascimento, escolaridade, email, telefone, chave_pix=None, pagamento='Pendente'):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.escolaridade = escolaridade
        self.email = email
        self.telefone = telefone
        self.chave_pix = chave_pix if chave_pix else self.gerar_chave_pix()
        self.pagamento = pagamento

    def gerar_chave_pix(self):
        """
        Gera uma chave Pix aleatória para o pagamento.
        """
        caracteres = string.ascii_letters + string.digits
        chave = ''.join(random.choice(caracteres) for _ in range(20))
        return chave

class BancoDeDados:
    """
    Classe que gerencia a conexão com o banco de dados.
    
    Princípios aplicados:
    - Modularidade: banco separado das outras partes do sistema.
    """

    def __init__(self, nome_banco='semana_informatica.db'):
        self.conexao = sqlite3.connect(nome_banco)
        self.criar_tabela()

    def criar_tabela(self):
        """
        Cria a tabela de inscrições, se ainda não existir.
        """
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inscricoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                escolaridade TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                chave_pix TEXT NOT NULL,
                pagamento TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def adicionar_inscricao(self, inscricao):
        """
        Adiciona uma nova inscrição no banco de dados.
        """
        cursor = self.conexao.cursor()
        cursor.execute('''
            INSERT INTO inscricoes (nome, data_nascimento, escolaridade, email, telefone, chave_pix, pagamento)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (inscricao.nome, inscricao.data_nascimento, inscricao.escolaridade, inscricao.email, inscricao.telefone, inscricao.chave_pix, inscricao.pagamento))
        self.conexao.commit()

    def listar_inscricoes(self):
        """
        Lista todas as inscrições cadastradas.
        """
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM inscricoes')
        return cursor.fetchall()

    def atualizar_pagamento(self, id_inscricao):
        """
        Atualiza o status de pagamento para 'Pago'.
        """
        cursor = self.conexao.cursor()
        cursor.execute('''
            UPDATE inscricoes
            SET pagamento = 'Pago'
            WHERE id = ?
        ''', (id_inscricao,))
        self.conexao.commit()