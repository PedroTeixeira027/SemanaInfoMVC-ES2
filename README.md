# 🧠 Desenvolvimento da Aplicação - SemanaInfoMVC-ES2

Este repositório contém a aplicação desenvolvida durante o projeto da disciplina Engenharia de Software 2 (ES2). A aplicação foi construída seguindo o padrão arquitetural MVC (Model-View-Controller), promovendo a separação de interesses, modularidade e organização do código.

A aplicação foi desenvolvida pensando nas Tecnologias atuais, como Cloud Computing, IaC, entre outros assuntos.

### 👨‍💻 Responsáveis pelo Desenvolvimento

| Nome           | Função                                                                          |
|----------------|---------------------------------------------------------------------------------|
| Pedro T Vargas |  Desenvolvimento, configuração do Mysql e Redis e criação da README             |
| Pedro Teixeira |  Desenvolvimento, configuração do Mysql e criação do Repostitório

### 👨‍💻 Responsável pela Infraestrutura

| Nome         | Função                                                                          |
|--------------|---------------------------------------------------------------------------------|
| Kawan Silva  | Provisionamento da infraestrutura, Instalação e configuração do Linux, Zabbix, Docker e o MYSQL  |

---

### 📁 Estrutura dos Arquivos

### model.py

- Responsável por representar os dados e interagir com o banco de dados MySQL e o Redis:

- Inscricao: Classe que representa a entidade de uma inscrição, com geração automática de chave Pix.

- BancoDeDados: Classe para operações com o MySQL (criação de tabela, inserção, listagem, atualização de status de pagamento).

- Conexão com Redis para o recurso de chat.

### controller.py

- Contém a lógica da aplicação:

- InscricaoController: Coordena as ações entre a view e o model, como criação de inscrições, listagem e confirmação de pagamento.

### view.py

- Interface em modo texto (console) para interação com o usuário:

- Menu com opções de inscrição, listagem de inscritos, confirmação de pagamento e chat.

- Recurso de chat baseado em Redis, onde os participantes podem deixar mensagens persistentes.

---

### 💡 Funcionalidades Implementadas

- Cadastro de Inscrições: coleta dados como nome, email, escolaridade etc. e gera uma chave Pix.

- Listagem de Inscrições: exibe todos os cadastros armazenados no banco.

- Confirmação de Pagamento: altera o status da inscrição para "Pago".

- Chat Integrado: funcionalidade baseada em Redis para troca de mensagens entre os participantes do evento.

---

### ⚙️ Tecnologias Internas

- Python: linguagem principal da aplicação.

- MySQL: utilizado para armazenar os dados principais das inscrições.

- Redis: utilizado para armazenar mensagens em tempo real no chat.

- Paradigmas aplicados: abstração, encapsulamento, separação de interesses e baixo acoplamento.


---

# ☁️ Infraestrutura da Aplicação - SemanaInfoMVC-ES2

Esta parte do projeto é responsável por provisionar a **infraestrutura** na Oracle Cloud Infrastructure (OCI), utilizando **Terraform** e **Docker**.


### 🔧 Tecnologias Utilizadas

- Oracle Cloud Infrastructure (OCI)
- Terraform
- Docker
- Linux (Ubuntu)

---

### 🏗️ Infraestrutura Provisionada

A infraestrutura criada com Terraform na OCI inclui:

- VCN (Virtual Cloud Network)
- Sub-redes
- Instância Compute (VM) para execução da aplicação
- Regras de segurança (NSG e Security Lists)
- Volume de armazenamento

---

### 📦 Serviços Configurados

### ✅ MySQL Server 
- Instalado na VM
- Porta padrão: `3306`

### ✅ Redis 
- Instalado na VM
- Porta padrão: `6379`

### ✅ Redisinsight (via Docker)
- Instalado no docker via Docker Compose.
- Porta padrão: `5540`
- Utilizado para facilitar a visualização dos comentários do chat.

### ✅ DBeaver (via Docker)
- Instalado no docker via Docker Compose.
- Porta padrão: `8978`
- Utilizado para facilitar a visualização dos dados inseridos no cadastro.

### ✅ UptimeKuma
- Instalado no Docker
- Porta padrão: `3001`
---


#### :memo: License
  
 This project is under [MIT License](./LICENSE).

<p align='center'>
  Do you like my open source projects? <a href='https://stars.github.com/nominate/'>Nominate us to Github Stars ⭐</a>
</p>
