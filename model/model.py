# model.py

import mysql.connector 
import random
import string
import redis
import os


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
    def __init__(self, host='localhost', user='', password='', database=''):
        self.conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.criar_tabela()

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inscricoes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                data_nascimento VARCHAR(100) NOT NULL,
                escolaridade VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                telefone VARCHAR(100) NOT NULL,
                chave_pix VARCHAR(255) NOT NULL,
                pagamento VARCHAR(100) NOT NULL
            )
        ''')
        self.conexao.commit()

    def adicionar_inscricao(self, inscricao):
        cursor = self.conexao.cursor()
        cursor.execute('''
            INSERT INTO inscricoes (nome, data_nascimento, escolaridade, email, telefone, chave_pix, pagamento)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (inscricao.nome, inscricao.data_nascimento, inscricao.escolaridade, inscricao.email, inscricao.telefone, inscricao.chave_pix, inscricao.pagamento))
        self.conexao.commit()

    def listar_inscricoes(self):
        cursor = self.conexao.cursor()
        cursor.execute('SELECT * FROM inscricoes')
        return cursor.fetchall()

    def atualizar_pagamento(self, id_inscricao):
        cursor = self.conexao.cursor()
        cursor.execute('''
            UPDATE inscricoes
            SET pagamento = 'Pago'
            WHERE id = %s
        ''', (id_inscricao,))
        self.conexao.commit()

