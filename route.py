# TODO: Organizar as importações, importando apenas as funcionalidades em uso.
# 1. Revise todas as importações no arquivo.
# 2. Identifique quais módulos, funções ou classes estão realmente sendo utilizados no código.
# 3. Remova importações desnecessárias ou não utilizadas.
# 4. Se possível, substitua importações globais (como `import modulo`) por importações específicas (como `from modulo import função`) para otimizar o código.
# 5. Verifique se o código continua funcionando corretamente após a limpeza das importações.


from flask import Flask, render_template, request

from funcs.cadastro import cadastrarProduto
from funcs.editor import editarProduto

from utils import menu_bar, cadastro_produtos_config_template

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    Retorna a página principal do sistema de estoque.

    Returns:
        str: HTML renderizado do template 'index.html'.

    Notes:
        A barra de navegação é gerada dinamicamente a partir de 'menu_bar()'.
    """
    return render_template("index.html", navBar=menu_bar())











































# 2. Eliminar código duplicado e melhorar eficiência onde possível.
# 3. Implementar testes para garantir que a funcionalidade de cadastro funcione corretamente.
@app.route("/cadastrar-produto/", methods=("GET", "POST"))
def cadastrar_produto() -> str:
    """
    Rota para cadastrar novo produto ao banco de dados.

    Se o método for GET, retorna o template de cadastro de produtos.

    Se o método for POST, cadastra um novo produto com as informações
    recebidas no formulário e salva no banco de dados.

    Return:
        HTML renderizado do Template de cadastro de produtos.
        
    Observações:
    
        - 'menu-nav/cadastro.html' é o template
        - 'template', 'categoria' e 'saldoEntrada' são alimentados dinamicamente a partir de 'cadastro_produtos_config_template()'.
        - A barra de navegação é gerada dinamicamente a partir de 'menu_bar()'.
    """
    if request.method == "POST":
        # Se o método for POST, cadastra um novo produto,
        # com as informações recebidas no formulário
        produto = cadastrarProduto(request=request)
        produto.cadastrar()
        
    # Retorna o template de cadastro de produtos se o método for GET
    return render_template(
        "menu-nav/cadastro.html",
        template=cadastro_produtos_config_template()["template"],
        categoria=cadastro_produtos_config_template()["categoria_options"],
        saldoEntrada=cadastro_produtos_config_template()["saldoEntrada"],
        navBar=menu_bar(),
    )


























































# TODO: editar_produto()Pendente a configuração
@app.route("/editar-produto", methods=("GET", "POST"))
def editar_produto():

    if request.method == "POST":
        if request.content_type == "text/plain":

            print()
            print(request.data.decode("utf-8"))
            print()

            produto = editarProduto(request.data.decode("utf-8"))
            return produto.dados()

    template = render_template("menu-nav/editor.html")

    return template




# TODO: listar_produtos() Pendente a configuração
@app.route("/listar-produtos")
def listar_produtos() -> str:
    template = render_template("menu-nav/list.html")
    return template


# TODO: info_produto() Pendente a configuração
@app.route("/info-produto")
def info_produto() -> str:
    # TODO: Obter dicionário com uma função GET
    dictionary: dict[str, str] = {
        # produto 1
        "titulo": "Caneta Azul",
        "categoria": "Azul Caneta",
        "publico": "Feminino",
        "saldo": "10",
        "tamanho": "GG",
        "descricao": "Um texto qualquer.",
        # produto 2
        "codigo": "1234567890",
        "fornecedor": "Google Ltda",
        "precofornecedor": "1000.00",
        "precovenda": "10.00",
    }
    imagens: list[str] = [
        "/static/img/image.jpg",
        "/static/img/image.jpg",
        "/static/img/image.jpg",
        "/static/img/image.jpg",
        "/static/img/image.jpg",
    ]
    template: str = render_template(
        "menu-nav/info.html", dictionary=dictionary, imagens=imagens
    )

    return template


# TODO: login() Pendente a configuração
@app.route("/login")
def login() -> str:
    return render_template("login.html")


# TODO: manutencao() Pendente a configuração
@app.route("/manutencao")
def manutencao() -> str:
    title = "Informações do Produto"
    className = 'ClassName = "op-info-produto"'
    description = "Em manutenção..."

    template = render_template(
        "menu-nav/manutencao.html",
        title=title,
        className=className,
        description=description,
    )

    return template


if __name__ == "__main__":
    app.run(debug=True)
