import sqlite3
from tempfile import TemporaryFile

from jinja2 import Template





class Database:
    def __init__(self, db='database/database.db') -> None:
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        
        
        
        
        
        
    def criar_tabela(self, nome_tabela: str, string_template: str):
        """
        Cria uma nova tabela no banco de dados se a mesma não existir.

        Args:
            nome_tabela (str): Nome da tabela a ser criada.
            string_template (str): Template da tabela, contendo os nomes dos campos e seus tipos.
        
        Observações:
            - A tabela sera criada caso não exista no banco de dados (`IF NOT EXISTS`).
            - O parâmetro `string_template` deve seguir a sintaxe SQL correto
            - Assim que a tabela é criada, a operação é commitada
        """
        
        # Cria a tabela
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({string_template})")
        # Commit
        self.connection.commit()









    def verificar_tabela(self, nome_tabela: str) -> bool:
        """
        Verifica se a tabela `nome_tabela` existe no banco de dados.
        Caso não exista, gera um retorno False

        Args:
            nome_tabela (_type_): _description_

        Returns:
            bool: True se a tabela existir, False caso contrario.
        """
        try:
            # Verifica se a tabela nao existe
            self.cursor.execute(f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name={nome_tabela}
            """)
            # Retorna True se a tabela existir
            return self.cursor.fetchone() is not None 
        except:
            # Caso nao exista, retorna False
            return False


































    def inserir_dados(self, name_tabela: str, template: str, dados: list[tuple]) -> None:
        
        query = f"INSERT INTO {name_tabela} {template}", dados
        print("SQL Gerado:", query)  # Debug para verificar a query

        self.cursor.executemany(f"INSERT INTO {name_tabela} {template}", dados)
        self.connection.commit()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def atualizar_dados(self, id ,dados: list[tuple]) -> None:
        
        #('saldo', '150', 'descricao', 'camisa azul masculina', 'publico', 'masculino', 'precoVenda', '220')
        
        
        self.cursor.execute(f"""
                       UPDATE produtos 
                       SET {", ".join([f"{dados[i]} = '{dados[i+1]}'" for i in range(0, len(dados), 2)])}
                       WHERE id = {id}
                       """)
        
        
        self.connection.commit()




































    def consultar_dados(self) -> list:
        
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()


































    def deletar_dados(self, id) -> None:
        
        self.cursor.execute("""
                            DELETE FROM produtos 
                            WHERE ? = ?
                            """)
        self.connection.commit()























    def fechar_conexao(self):
        self.connection.close()
        
#db = Database()