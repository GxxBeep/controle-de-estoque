import json


class editarProduto:
    def __init__(self, ID) -> None:
        self.id = ID
    
    
    def dados(self):
        with open('database/produtos/estoque.json', 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}
        return data[self.id]
