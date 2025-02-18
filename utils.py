import json


def carregar_config() -> dict:
    """
    Carrega as configurações do sistema.
    
    Retorna um dicionário com as configurações do arquivo "config.json".
    
    Returns:
        dict: Dicionário com as configurações do sistema.

    Notes:
        Se o arquivo "config.json" não for encontrado ou houver um erro ao decodificar o JSON, retorna um dicionário vazio.
    """
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar as configurações: {e}")
        return {}

def menu_bar() -> list:
    """
    Retorna a configuração do menu de navegação.

    Returns:
        list: Lista de dicionários com as configurações do menu de navegação.

    Notes:
        Retorna uma lista vazia caso não encontre "navBar".
    """
    __config = carregar_config()
    return __config.get("navBar_config", []) # retorna [] se não encontrar "navBar"

def cadastro_produtos_config_template() -> dict:
    """
    Retorna a configuração da template de cadastro de produtos.

    Returns:
        list: Lista de dicionários com as configurações para o template de cadastro de produtos.

    Notes:
        Retorna uma lista vazia caso não encontre "cadastroProduto_config".
    """
    __config = carregar_config()
    return __config.get("cadastroProduto_config", {}) # retorna {} se não encontrar "cadastroProduto_config"
