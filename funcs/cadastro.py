import os
import json

from .sistema import Database

from flask import Request
from datetime import datetime
from werkzeug.datastructures import ImmutableMultiDict, FileStorage
from utils import cadastro_produtos_config_template


class cadastrarProduto:
    """
    A classe recebe um objeto contendo dados do formulario e arquivos enviados,
    esses dados serão utilizados para cadastrar um novo produto ao banco de dados.
    
    Parameters:
        request (Request): Objeto contendo dados do formulário e arquivos enviados.
        
    Exemplo de uso::

        # Importa a classe
        from funcs.cadastro import cadastrarProduto
        # Cria uma instância da classe
        produto = cadastrarProduto(request=request)
        # Cadastra o produto
        produto.cadastrar()
    """
    
    def __init__(self, request: Request):
        # Recebe os dados do formulário
        self.form: ImmutableMultiDict[str, str] = request.form
        # Recebe os arquivos
        self.files: ImmutableMultiDict[str, FileStorage] = request.files
        # Define o nome da tabela
        self.name_tabela: str = "produtos"
        # Inicia a instância do banco de dados
        self.db = Database()
        

    def __definicao_de_tabela(self) -> list[dict]:
        """
        A função percorre através da função `cadastro_produtos_config_template()`.
        Buscando os dados para a configuração da Template de cadastro.
        
        Returns:
            list[dict]: Uma lista contendo dicionários e cada dicionário com as seguintes chaves:
                - `name` (str): Nome do campo no bando de dados (Ex: `precoVenda`).
                - `type` (str): Tipo do campo no bando de dados (Ex: `TEXT`, `INTEGER`, `REAL` ).
                - `required` (str): Indica se o campo é obrigatório (True) ou opcional (False).
        
        Exemplo de saída::
        
            [
                {"name": "produto",     "type": "TEXT",     "required": "True"},
                {"name": "descricao",   "type": "TEXT",     "required": "False"},
                {"name": "saldo",       "type": "INTEGER",  "required": "True"},
                {"name": "precoVenda",  "type": "REAL",     "required": "True"}
            ]
        """
        return cadastro_produtos_config_template()["configuracao_para_sql"]


    def __verificar_table(self, nome_tabela: str) -> None:
        """
        Verifica se a tabela `nome_tabela` existe no banco de dados.
        Caso não exista, cria uma nova tabela com o nome `nome_tabela` e a definição da mesma.

        Parameters:
            nome_tabela (str): Nome da tabela a ser verificada ou criada.
        
        Observações:
        
            - O campo `name` é definido como (produto, precoVenda, descricao e etc...).
            - O campo `type` é definido como (`TEXT`, `REAL` ou `INTEGER`).
            - O campo `NOT FULL` é obrigatório caso contrário ele é opcional.
            - Os campos são definidos na função `__definicao_de_tabela()`.
        
        Example da template:
        
                id INTEGER PRIMARY KEY,
                name type NOT NULL,
                name type,
        """
        # Verifica se a tabela nao existe
        if not self.db.verificar_tabela(nome_tabela):
            # Busca a definição da tabela
            __template: list[dict] = self.__definicao_de_tabela()
            # Define a estrutura da tabela
            __tabela: str = f"""
                id INTEGER PRIMARY KEY,
                {", ".join(f"{dicts['name']} {dicts['type']} {'NOT NULL' if dicts['required'] else ''}".strip() for dicts in __template)} 
            """
            # Cria a tabela no banco de dados passando o nome e a tabela
            self.db.criar_tabela(nome_tabela=nome_tabela, string_template=__tabela)


    def verificar_repositorio(self, name: str) -> str:
        """
        Cria o repositorio de imagens caso não exista.

        Parameters:
            name (str): Nome do repositorio.

        Returns:
            str: Caminho do repositorio criado.
        """
        _path_: str = f"database/imagens/{name}"
        # Verifica se o repositorio existe
        if not os.path.exists(_path_):
            # Cria o repositorio
            os.makedirs(_path_, exist_ok=True)
        else:
            return _path_
        return _path_


    def extrair_extensao_imagem(self, imagem: str | None) -> str | None:
        """
        Extrai a extensão da imagem.
        
        Parameters:
            imagem (str): Caminho da imagem.
        
        Returns:
            str | None: Retorna a extensão da imagem ou None se a imagem for None.
        """
        if imagem is None:
            return None
        return os.path.splitext(imagem)[1]


    def salvar_imagens(self, name_produto: str) -> str | None:
        """
        Salva as imagens do produto no diretório 'database/imagens' e
        Retorna uma lista com os caminhos das imagens.

        Parameters:
            name_produto (str): Nome do produto para identificar a pasta no diretório.

        Returns:
            str | None: Retorna uma string JSON contendo uma lista com os caminhos das imagens
            ou None se nenhuma imagem for salva.
            
        Exemplo de saída:
        
            '[
            "imagens/NomeDoProduto/1.jpg", 
            "imagens/NomeDoProduto/2.jpg", 
            "imagens/NomeDoProduto/3.jpg"
            ]'
        """
        # Verifica se o formulário possui imagens
        if self.files.getlist('imagens') is None:
            return None 
        else:
            # Verifica se a pasta existe
            pasta: str = self.verificar_repositorio(name=name_produto)
            # Busca a quantidade de imagens
            count: int = len(x) if (x := os.listdir(pasta)) else 0
            # lista para armazenar os caminhos das imagens
            path_list: list = [] 
            
            for index, imagem in enumerate(self.files.getlist('imagens'), start=1):
                # Extrai a extensão da imagem
                extensao: str | None = self.extrair_extensao_imagem(imagem.filename)  
                # Cria o caminho da imagem
                path: str = os.path.join(pasta ,f"{count+index}{extensao}")
                # Salva a imagem
                imagem.save(path)
                # Adiciona o caminho da imagem na lista
                path_list.append(path)
            
            # Remove o prefixo 'database/' e substitui o separador '\\' por '/'
            path_list: list = [i.replace('database/', '').replace('\\', '/') for i in path_list]    
            return json.dumps(path_list)


    def lista_dados_do_formulario(self, path_list: str | None) -> list[tuple]:
        """
        Transforma os dados do formulário em uma lista de tuplas, substituindo valores vazios por `None` e 
        adiciona valores de data e hora atuais e calcula o lucro.
        
        Returns:
            list[tuple]: Lista contendo uma tupla com os dados do formulário.
        
        Exemplo de saída:
        
            [(value1, value2, value3, value4, value5)]
        """
        # Filtra os dados do formulário e adiciona apena os valores na variável `__values`
        __values: list[tuple] = [tuple(value if value else None for _, value in self.form.items())]
        
        for index, value in enumerate(__values):
            # Adiciona lucro, data e hora atuais
            _y:tuple = (
                int(x[-2]) - int(x[-3]),  # type: ignore
                datetime.now().strftime("%d/%m/%Y"),
                datetime.now().strftime("%H:%M:%S"),
                datetime.now().strftime("%d/%m/%Y"),
                datetime.now().strftime("%H:%M:%S"),
                path_list
                )
            # substitui os valores
            __values[index] = value + _y
        return __values


    def __inserir_dados(self, dados: list[tuple]) -> None:
        """
        Função percorre em buscar as configurações de definição da tabela `__definicao_de_tabela()` e
        monta uma query para inserir os dados no banco de dados.

        Parameters:
            dados (list[tuple]): Lista contendo tuplas com os dados do formulário.
        """
        # Obtém a definição da tabela
        config_templete: list[dict] = self.__definicao_de_tabela()
        # Monta a query
        query: str = f"""({", ".join(n["name"] for n in config_templete)}) VALUES ({", ".join("?" * len(config_templete))})"""
        # Insere os dados no bando de dados
        self.db.inserir_dados(
            name_tabela=self.name_tabela,
            template=query,
            dados=dados
            )


    def cadastrar(self):
        # Verifica se a tabela existe
        self.__verificar_table(nome_tabela=self.name_tabela)
        # Busca os dados
        __pathList: str | None = self.salvar_imagens(name_produto=self.form['produto'])
        # Adiciona dados essenciais ao formulário
        __dadosList: list[tuple] = self.lista_dados_do_formulario(path_list=__pathList)
        # Insere os dados
        self.__inserir_dados(dados=__dadosList)