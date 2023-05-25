# Variaveis de texto
TEXT_BEM_VINDO = """
--- Bem-Vindo a Locadora do Guilherme ---

-> Faça seu cadastro para continuar!
    
"""
TEXT_MENU_FILMES = """
=============================
[1] Comprar filmes
[2] Alugar filmes
[3] Adicionar filmes
============================="""


# Variáveis para guardas dados
DADOS_CADASTRO = []
FILMES_SELECIONADOS = []
FILMES_ALUGADOS = []

# Variáveis com informações salvas
LISTA_FILMES = {
    "AÇÃO": [
        "Nada de Novo no Front (2022)",
        "Assalto ao Poder (2016)",
        "Athena (2022)"
    ],
    "ROMANCE": [
        "Esposa de Aluguel (2022)",
        "Uma Garota de Muita Sorte (2022)",
        "Persuasão (2022)"
    ],
    "COMÉDIA": [
        "Uma Quedinha de Natal (2022)",
        "Dolittle (2020)",
        "Esticando a Festa (2021)"
    ],
    "TERROR": [
        "O Telefone do Sr. Harrigan (2022)",
        "Lar dos Esquecidos (2022)",
        "A Caçada (2020)"
    ]
}

TEXT_GENEROS = """
============================
    Gêneros existentes
[1] AÇÃO
[2] ROMANCE
[3] COMÉDIA
[4] TERROR
=============================
"""

TEXT_ESTRUTURA_1 = """
- Escreva da seguinte forma:
            (espaço)
(Nome do filme) + (Ano de lançamento)
*************** + *******************
"""