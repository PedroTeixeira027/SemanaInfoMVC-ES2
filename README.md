# ☁️ Infraestrutura da Aplicação - SemanaInfoMVC-ES2

Este repositório contém a aplicação desenvolvida durante o projeto da disciplina Engenharia de Software 2 (ES2). Esta parte do projeto é responsável por provisionar a **infraestrutura** na Oracle Cloud Infrastructure (OCI), utilizando **Terraform** e **Docker**. E também a splicação escrita em Python, que roda em uma VM Linux.

### 👨‍💻 Responsável pela Infraestrutura

| Nome         | Função                                                                          |
|--------------|---------------------------------------------------------------------------------|
| Kawan Silva  | Provisionamento da infraestrutura, Instalação e configuração do Linux e Docker  |



---

### 🔧 Tecnologias Utilizadas

- Oracle Cloud Infrastructure (OCI)
- Terraform
- Docker
- MySQL Server (instalado na VM)
- Redis (em container Docker)
- Linux
- Python

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

### ✅ MySQL Server (fora do Docker)
- Instalado diretamente na máquina virtual (Ubuntu/Linux).
- Porta padrão: `3306`
- Utilizado para armazenar os dados da aplicação.

### ✅ Redis (via Docker)
- Instalado no docker via Docker Compose.
- Porta padrão: `6379`


<br>

  Você pode usar um arquivo terraform.tfvars para definir valores sensíveis, como:

`tenancy_ocid = "ocid1.tenancy.oc1..."` <br>
`compartment_ocid = "ocid1.compartment.oc1..."` <br> 
`region = "sa-saopaulo-1"` <br> 
... <br>

## :memo: License
  
 This project is under [MIT License](./LICENSE).

<p align='center'>
  Do you like my open source projects? <a href='https://stars.github.com/nominate/'>Nominate us to Github Stars ⭐</a>
</p>
