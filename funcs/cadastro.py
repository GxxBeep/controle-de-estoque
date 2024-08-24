# TODO: Organizar as importações, importando apenas as funcionalidades em uso.
# 1. Revise todas as importações no arquivo.
# 2. Identifique quais módulos, funções ou classes estão realmente sendo utilizados no código.
# 3. Remova importações desnecessárias ou não utilizadas.
# 4. Se possível, substitua importações globais (como `import modulo`) por importações específicas (como `from modulo import funcao`) para otimizar o código.
# 5. Verifique se o código continua funcionando corretamente após a limpeza das importações.

from datetime import datetime
import os
import json


class cadastrarProduto:
    def __init__(self, 
                 produto: str,
                 categoria: str,
                 publico: str,
                 saldo: int,
                 tamanha: str,
                 precoFornecedor: int,
                 precoVenda: int,
                 cor: str,
                 fornecedor: str,
                 descricao: str | None = None,
                 codigoBarra: str | int | None = None,
                 imagens: list | None = None):
        """
        Inicializa a classe cadastro com os dados do produto fornecidos

        Parameters:
            produto (str): nome do produto
            categoria (str): categoria do produto
            publico (str): publico alvo
            saldo (str): saldo de entrada
            tamanha (str): tamanho da peça
            descricao (str): descrição
            cor (str): cor do produto
            codigoBarra (str | int): código de barra
            fornecedor (str): nome do fornecedor
            precoFornecedor (int): preço de compra do fornecedor
            precoVenda (int): preço de venda do produto
            imagens (list[str]): lista de imagens do produto
        """

        self.produto = produto
        self.categoria = categoria
        self.publico = publico
        self.saldo = saldo
        self.tamanha = tamanha
        self.descricao = descricao
        self.cor = cor
        self.codigoBarra = codigoBarra
        self.fornecedor = fornecedor
        self.precoFornecedor = precoFornecedor
        self.precoVenda = precoVenda
        self.imagens = imagens

    def gerar_identificacao(self) -> str:
        """
        Gera um código de identificação único para cada produto, considerando o nome do produto, 
        público alvo, cor e o nome do fornecedor.

        Returns:
            str: Código de identificação único.
        """
        return f"{self.produto[:3]}{self.publico[:3]}-{self.cor[:3]}{self.fornecedor[:3]}".upper()

    def calcular_lucro(self) -> int:
        """
        Calcula o lucro de um produto, subtraindo o preço de venda pelo preço de compra.
        
        Returns:
            int: Valor do lucro.
        """
        return int(self.precoVenda - self.precoFornecedor)
    
    def extrair_extensao_imagem(self, imagem: str) -> str:
        """
        Extrai a extensão de uma imagem.

        Parameters:
            imagem (str): Nome da imagem.

        Returns:
            str: Extensão da imagem.
        """
        return os.path.splitext(imagem)[1]
  
    # TODO: Transcrever esta função para o arquivo 'sistema.py'.
    # 3. Colar a função no local apropriado dentro de 'sistema.py', 
    #   mantendo a estrutura e a formatação correta.
    # 4. Certificar-se de que todas as importações necessárias estão presentes no arquivo 'sistema.py'.
    # 5. Testar a função no novo arquivo para garantir que ela funciona conforme o esperado.
    def repositorio(self, tipo: str) -> str:
        """
        Retorna o caminho do repositório 'database' com o tipo de arquivo especificado.

        Parameters:
            tipo (str): Tipo do arquivo, exemplo 'imagens', 'produto'.

        Returns:
            str: Caminho do repositório.
        """
        repositorio_raiz = os.path.dirname(os.path.dirname(__file__)) # ../controle-de-estoque/
        return os.path.join(repositorio_raiz, 'database', tipo)
  
    # TODO: Implementar funcionalidade para criar pastas usando o 'ID' do produto como nome da pasta.
    # 1. Criar uma pasta com o nome baseado no 'ID' do produto, por exemplo, 'produto_<ID>/'.
    # 2. Salvar os arquivos e dados relacionados ao produto dentro dessa pasta.
    # 3. Verificar se uma pasta com o mesmo 'ID' já existe. Se sim, decidir se ela deve ser reutilizada ou atualizada.
    def salvar_imagens(self, id: str) -> list | None:
        """
        Salva as imagens do produto no diretório 'database/img'
        Retorna uma lista com os caminhos das imagens.

        Parameters:
            id (str): Código de identificação único do produto.

        Returns:
            list: Lista com os caminhos das imagens.
            
        Notes:
            Se a lista de imagens for vazia, retorna uma lista vazio.
        """
        if self.imagens is None:
            return [] # retorna uma lista vazia caso não tenha imagens
        else:
            path_list = [] # lista para armazenar os caminhos das imagens
            len = 1 # contador para nomear as imagens
            for imagem in self.imagens:
                extensao = self.extrair_extensao_imagem(imagem.filename) # extensão da imagem
                path = os.path.join(self.repositorio('imagens') ,f"{id}({len}){extensao}") # caminho da imagem
                imagem.save(path) # salvar imagem
                path_list.append(path) # adicionar caminho da imagem na lista
                len += 1 # incrementar o contador
            return path_list
        
    # TODO: Implementar verificação de dados:
    # 1. Não sobrescrever valores no JSON se o campo correspondente no input estiver vazio, 
    #    mas já houver um valor existente no JSON.
    # 2. Verificar se os valores de entrada contêm números em ponto flutuante (float).
    #    Se forem encontrados na chave 'Lucro', somar os valores em vez de sobrescrevê-los.
    # 3. Caso o dado já exista no JSON, apenas atualizar a chave 'ultimaAlteracao' com a nova data.
    # 4. Implementar suporte para variantes nas chaves 'cor' e 'tamanha', permitindo múltiplas entradas.
    def mondar_dados(self) -> dict:
        """
        Monta um dicionário com os dados do produto, incluindo o código de identificação único, 
        o lucro, a data de criação e a lista de imagens.

        Returns:
            dict: Dicionário com os dados do produto.
        """
        id = self.gerar_identificacao() # gerar código de identificação único
        lucro = self.calcular_lucro() # calcular o lucro do produto
        data = datetime.now().strftime("%d/%m/%Y - %H:%M") # data de criação e última alteração
        path_list = self.salvar_imagens(id) # salvar as imagens e retornar a lista de caminhos
        
        dados = {
            id: { # dicionário com os dados do produto
                'nome': self.produto, # nome do produto
                'categoria': self.categoria, # categoria do produto
                'publico': self.publico, # público alvo do produto
                'saldo': self.saldo, # saldo de entrada do produto
                'tamanha': self.tamanha, # tamanho da peça do produto
                'descricao': self.descricao, # descrição do produto
                'cor': self.cor, # cor do produto
                'codigoBarra': self.codigoBarra, # código de barra do produto
                'fornecedor': self.fornecedor, # nome do fornecedor do produto
                'precos': { # dicionário com os preços do produto
                    'precoFornecedor': self.precoFornecedor, # preço de compra do fornecedor
                    'precoVenda': self.precoVenda, # preço de venda do produto
                    'lucro': lucro # lucro do produto
                },
                "dataCriacao": data, # data de criação do produto
                "ultimaAlteracao": data, # data da última alteração do produto
                'imagens': path_list # lista de imagens do produto
            }
        }
        return dados
    
    # TODO: Alterar resposta se foi bem sucedido ou não.
    def salvar(self) -> bool:
        """
        Salva os dados do produto no arquivo 'database/produtos/estoque.json'.

        Este método abre o arquivo 'database/produtos/estoque.json' em modo de leitura e escrita,
        carrega os dados no formato JSON, atualiza os dados do produto e salva no arquivo.

        Returns:
            bool: True se o salvamento foi bem sucedido, False caso contrário.
        """
        with open('database/produtos/estoque.json', 'r+') as file:
            try:
                # Carrega os dados do arquivo no formato JSON
                data = json.load(file)
            except json.JSONDecodeError:
                # Se o arquivo estiver vazio, cria um dicionário vazio
                data = {}
            # Atualiza os dados do produto
            data.update(self.mondar_dados())
            # Posiciona o ponteiro no início do arquivo
            file.seek(0)
            # Salva os dados no arquivo no formato JSON
            json.dump(data, file, indent=4)
            # Remove os caracteres excedentes do arquivo
            file.truncate()
        return True
