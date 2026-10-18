# 🎬 Recomendador de Filmes

## 📝 Descrição

Projeto de recomendação e busca de filmes desenvolvido em Python, utilizando o dataset 100k_movies. O sistema utiliza Pandas para manipulação e filtragem dos dados e FastMCP para disponibilizar ferramentas que podem ser utilizadas por agentes de Inteligência Artificial.

O objetivo é explorar a integração entre processamento de dados, agentes de IA e o protocolo MCP (*Model Context Protocol*), além de praticar desenvolvimento colaborativo com Git e GitHub Flow.

## ⚙️ Tecnologias e Ferramentas Utilizadas

- **Python** — linguagem de programação.
- **Pandas** — carregamento, manipulação e filtragem dos dados.
- **FastMCP** — criação de ferramentas e servidor MCP.
- **Git e GitHub** — versionamento e colaboração.
- **GitHub Flow** — organização do desenvolvimento com branches e Pull Requests.

## 💻 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/IagoRochaDev/recomendador_filmes.git

cd recomendador_filmes
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
```

No Ubuntu/Linux:

```bash
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o servidor MCP

```bash
python chat.py
```

O servidor será iniciado utilizando o transporte `stdio`, ficando disponível para comunicação com um cliente MCP compatível.

## 👥 Colaboradores

| Nome | GitHub |
|---|---|
| Iago Rocha Oliveira | [@IagoRochaDev](https://github.com/IagoRochaDev) |
| Isadora Bicalho | [@IsadoraBicalhoG](https://github.com/IsadoraBicalhoG) |

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de aprendizado colaborativo.

A licença do projeto deverá ser definida pelos colaboradores e registrada em um arquivo `LICENSE`, caso desejem disponibilizar formalmente o código para reutilização.