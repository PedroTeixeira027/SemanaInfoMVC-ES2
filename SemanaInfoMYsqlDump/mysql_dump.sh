#!/bin/bash

# Configurações
USUARIO="seu_usuario_aqui"
SENHA="sua_senha_aqui"
BANCO="seu_banco_aqui"
DESTINO="/BKP-MYSQL" 

# Data atual para nome do arquivo
DATA=$(date +"%Y-%m-%d_%H-%M-%S")

# Nome do arquivo final
ARQUIVO="$DESTINO/${BANCO}_backup_$DATA.sql"

# Criar diretório destino, se não existir
mkdir -p "$DESTINO"

# Executar o dump
mysqldump -u"$USUARIO" -p"$SENHA" "$BANCO" > "$ARQUIVO"

# Verificar se foi bem-sucedido
if [ $? -eq 0 ]; then
    echo "Backup realizado com sucesso: $ARQUIVO"
else
    echo "Erro ao realizar o backup!"
    exit 1
fi
