# 🎬 Recomendador de Filmes

## 📝 Descrição

Projeto de recomendação e busca de filmes desenvolvido em Python, utilizando o dataset 100k_movies. O sistema utiliza Pandas para manipulação e filtragem dos dados e FastMCP para disponibilizar ferramentas que podem ser utilizadas por agentes de Inteligência Artificial.

O objetivo é explorar a integração entre processamento de dados, agentes de IA, modelos de linguagem e o protocolo MCP, além de praticar desenvolvimento colaborativo com Git e GitHub Flow.

## ⚙️ Tecnologias e Ferramentas Utilizadas

- **Python** — linguagem de programação.
- **Pandas** — carregamento, manipulação e filtragem dos dados.
- **FastMCP** — criação do servidor MCP e disponibilização das ferramentas de busca.
- **MCP (Model Context Protocol)** — protocolo de comunicação entre o agente e as ferramentas.
- **Ollama** — execução local do modelo de linguagem, sem necessidade de utilizar uma API paga.
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

### 4. Instale o Ollama

O Ollama permite executar modelos de linguagem localmente, sem precisar configurar uma chave de API da OpenAI.

No Ubuntu/Linux, execute:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Consulte também o site oficial: https://ollama.com/

### 5. Baixe o modelo de linguagem

O projeto utiliza o modelo Llama 3.2 3B. Para baixá-lo, execute:

```bash
ollama pull llama3.2:3b
```

Confira se o modelo está disponível:

```bash
ollama list
```

**Observação:** o Ollama precisa estar em execução para que o agente consiga acessar o modelo. Dependendo da instalação, ele pode ser iniciado automaticamente ou precisar ser iniciado manualmente.

### 6. Execute o agente

Com o ambiente virtual ativado e o Ollama funcionando, execute:

```bash
python agent.py
```


## 👥 Colaboradores

| Nome | GitHub |
|---|---|
| Iago Rocha Oliveira | [@IagoRochaDev](https://github.com/IagoRochaDev) |
| Isadora Bicalho | [@IsadoraBicalhoG](https://github.com/IsadoraBicalhoG) |

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de aprendizado colaborativo.

A licença do projeto deverá ser definida pelos colaboradores e registrada em um arquivo `LICENSE`, caso desejem disponibilizar formalmente o código para reutilização.