#Crie um dicionário para armazenar informações de um livro, 
#incluindo título, autor e ano de publicação. Imprima cada informação. 

from typing import Dict, Any 

livro_01: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "Desconhecido",
    "Ano":2008
}
livro_02: Dict[str, Any] = {
    "Titulo": "Game of Thrones 2",
    "Autor": "Desconhecido",
    "Ano": 2010
}

lista_de_livros = []

lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

print(lista_de_livros)


lista_de_livros_usando_dict: dict = {
    "livro_01": {"Titulo": "Game of Thrones",
    "Autor": "Desconhecido",
    "Ano":2008},

    "livro_02": {"Titulo": "Game of Thrones 2",
    "Autor": "Desconhecido",
    "Ano": 2010}
}

print(lista_de_livros_usando_dict["livro_01"]["Titulo"])