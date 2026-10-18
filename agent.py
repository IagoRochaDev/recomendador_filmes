
import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

buscador_path = Path(__file__).parent / "buscador.py"

client = MultiServerMCPClient({
    "buscador_filmes": {
        "command": "python",
        "args": [str(buscador_path)],
        "transport": "stdio",
    }
})


async def chat():
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0.5,
    )

    tools = await client.get_tools()

    agent = create_agent(
        model=llm,
        tools=tools,
        checkpointer=InMemorySaver(),
        system_prompt=
            "Você é um agente que ajuda usuários a encontrar e recomendar filmes. "
            "Utilize a ferramenta buscar_filmes para consultar a base de dados. "
            "Não invente títulos, gêneros ou notas que não estejam nos resultados. "
            "Interprete os pedidos do usuário e utilize os filtros adequados. "
            "Quando o usuário informar um gênero em português, converta-o "
            "para o nome correspondente na base MovieLens, em inglês. "
            "Exemplos: ficção científica = Sci-Fi, ação = Action, "
            "comédia = Comedy, drama = Drama, terror = Horror, "
            "romance = Romance, suspense = Thriller, animação = Animation. "
            "Quando o usuário informar uma nota mínima, utilize esse filtro. "
            "Quando o usuário informar o nome de um filme, utilize o filtro "
            "de título para encontrá-lo. "
            "Para recomendações gerais, utilize a ferramenta para buscar "
            "filmes com boas notas médias. "
            "Apresente até 5 filmes por resposta, com título, gênero e nota média. "
            "Explique brevemente por que cada resultado atende ao pedido. "
            "Informe quando nenhum filme for encontrado. "
            "Deixe claro que a nota apresentada é a média das avaliações "
            "registradas na base de dados.",
    )

    print("Recomendador de Filmes")
    print("Exemplo: Quero filmes de ficção científica bem avaliados.")
    print("Digite /q para sair.\n")

    config = {"configurable": {"thread_id": "1"}}

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "/q":
            print("Saindo...")
            break

        if not user_input:
            continue

        try:
            response = await agent.ainvoke(
                {
                    "messages": [
                        {"role": "user", "content": user_input}
                    ]
                },
                config=config,
            )

            print("\nResposta do agente:\n")
            print(response["messages"][-1].content)
            print()

        except Exception as e:
            print(f"Erro ao executar o agente: {e}\n")


if __name__ == "__main__":
    asyncio.run(chat())
