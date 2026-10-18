import pandas as pd
from pathlib import Path
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("buscador_filmes")

base_filmes = Path(__file__).parent / "100k_Movies_dataset.csv"

@mcp.tool()
def buscador(genero: str, duracao: int, ano_lancamento: int, csv_path = base_filmes):
    """
    Descrição:
        Função para buscar filmes dentro de uma base de dados 
        a partir do gênero, duração em minutos e ano de lançamento.
            -O gênero deve ser passado em inglês

    Args: 
        genero(string): nome do genero(inglês)
        duracao (int): duração em minutos do filme
        ano_lancamento (int): ano de lançamento do filme
        csv_path: caminho para a base de dados

    Returns:
        dataframe: filmes encontrados com as colunas: 
            'title', 'released_year', 'ratings', 'runtime', 'genre', 'Description'
    """

    base = pd.read_csv(base_filmes, encoding = 'utf-8')

    base['runtime'] = base['runtime'].str.extract(r'(\d+)', expand=False).astype('Int64')
    base['released_year'] = base['released_year'].astype('Int64')
    base['ratings'] = base['ratings'].astype(float)

    if duracao < 100:
        filtro_duracao = base['runtime'] < 100
    else:
        filtro_duracao = base['runtime'] >= 100

    base = base[(base['genre'].str.contains(genero, case=False)) &
                (filtro_duracao) &
                (base['released_year']==ano_lancamento)]
    
    if len(base) > 100:
        base_8 = base[base['ratings']>8]

        if len(base_8) > 0:
            base = base_8

    base = base.sort_values(by = 'ratings', ascending=False)

    result = base[['title', 'released_year', 'ratings', 'runtime', 'genre', 'Description']].head(10).to_dict(orient='records')

    return result

@mcp.tool()
def buscar_por_nome(titulo: str):
    """
        Descrição:
            Função para buscar filmes dentro de uma base de dados 
            a partir do nome.
                -O nome deve ser passado em inglês
    
        Args: 
            titulo (str): nome do filme (inglês)
    
        Returns:
            dict: informações do filme:
                'released_year', 'director', 'cast', 'genre', 'ratings', 'runtime', 'Description'
    """
    base = pd.read_csv(base_filmes, encoding='utf-8')

    base = base[base['title'].str.contains(titulo, case=False, na=False)]

    result = base[['title', 'released_year', 'ratings', 'director', 'runtime', 'genre', 'Description']].to_dict(orient='records')

    return result


if __name__ == '__main__':

    """    
    termo_busca = input("Nome do filme: ")
    
    resultados = buscar_por_nome(termo_busca)
    
    if resultados:
        for filme in resultados:
            print(filme)
            print()
    else:
        print("Não existe.")
    """

    mcp.run(transport = 'stdio')

