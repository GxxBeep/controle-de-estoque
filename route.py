# TODO: Organizar as importações, importando apenas as funcionalidades em uso.
# 1. Revise todas as importações no arquivo.
# 2. Identifique quais módulos, funções ou classes estão realmente sendo utilizados no código.
# 3. Remova importações desnecessárias ou não utilizadas.
# 4. Se possível, substitua importações globais (como `import modulo`) por importações específicas (como `from modulo import funcao`) para otimizar o código.
# 5. Verifique se o código continua funcionando corretamente após a limpeza das importações.

from flask import Flask, render_template, request, flash, redirect, url_for
from flask.wrappers import Response
from dotenv import load_dotenv
import os

from funcs.cadastro import cadastrarProduto




app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('KEY')


# TODO: Implementar configuração que iriar carregar configurações do json antes de iniciar o servidor
def carregar_configuracoes() -> list:
    # Dados temporários para testes
    categoria: list[str] = ['Blusas', 'Calças', 'Camisas',
                        'Casacos', 'Jaquetas', 'Macacões',
                        'Saias', 'Sapatos', 'Shorts', 'Vestidos']
    
    return categoria

# TODO: index() Pendente a configuração e gerar documentação 
@app.route('/')
def index() -> str:
    return render_template('index.html')

# TODO: Refatorar o Cadastro de Produtos
# 1. Validar se os campos obrigatórios estão preenchidos e se os dados são válidos antes de criar o produto.
# 2. Eliminar código duplicado e melhorar eficiência onde possível.
# 3. Implementar testes para garantir que a funcionalidade de cadastro funcione corretamente.
@app.route('/cadastrar-produto/', methods=('GET', 'POST'))
def cadastrar_produto() -> str:
    """Rota para cadastrar um novo produto.
    
    Se o método for GET, retorna o template de cadastro de produtos.
    
    Se o método for POST, cadastra um novo produto com as informações
    recebidas no formulário e salva no banco de dados. Se o cadastro for
    bem-sucedido, retorna para a URL atual com uma mensagem de sucesso
    e um redirect.
    
    Return:
        Template de cadastro de produtos ou redirect para a URL atual
    """
    if request.method == 'POST':
        # Se o método for POST, cadastra um novo produto,
        # com as informações recebidas no formulário
        produto = cadastrarProduto(
            produto=request.form['produtoNome'],
            categoria=request.form['categoria'],
            publico=request.form['publico'],
            saldo=int(request.form['saldoentrada']),
            tamanha=request.form['tamanhopeca'],
            descricao=request.form['descricao'],
            codigoBarra=request.form['codigoBarra'],
            fornecedor=request.form['fornecedor'],
            precoFornecedor=int(request.form['precoFornecedor']),
            precoVenda=int(request.form['precoVenda']),
            cor=request.form['produtoCor'],
            imagens=request.files.getlist('imagens')
            )
        # produto.salvar() salva os dados do novo produto
        if produto.salvar():
            flash('Cadastrado com sucesso!') # Mensagem de sucesso
            return redirect(request.url)  # retorna para a URL atual
    categoria = carregar_configuracoes() # Carrega a lista de categorias
    # Retorna o template de cadastro de produtos
    return render_template('menu-nav/cadastro.html', categoria=categoria)

# TODO: editar_produto()Pendente a configuração
@app.route('/editar-produto')
def editar_produto() -> str:

    template = render_template('menu-nav/editor.html')

    return template

# TODO: listar_produtos() Pendente a configuração
@app.route('/listar-produtos')
def listar_produtos() -> str:
    template = render_template('menu-nav/list.html')
    return template

# TODO: info_produto() Pendente a configuração
@app.route('/info-produto')
def info_produto() -> str:
    # TODO: Obter dicionário com uma função GET
    dictionary: dict[str, str] = {
        # produto 1
        'titulo': 'Caneta Azul',
        'categoria': 'Azul Caneta',
        'publico': 'Feminino',
        'saldo': '10',
        'tamanho': 'GG',
        'descricao': 'Um texto qualquer.',
        # produto 2
        'codigo': '1234567890',
        'fornecedor': 'Google Ltda',
        'precofornecedor': '1000.00',
        'precovenda': '10.00'
    }
    imagens: list[str] = ["/static/img/image.jpg",
                    "/static/img/image.jpg",
                    "/static/img/image.jpg",
                    "/static/img/image.jpg",
                    "/static/img/image.jpg"]
    template: str = render_template(
        'menu-nav/info.html',
        dictionary=dictionary,
        imagens=imagens)

    return template

# TODO: login() Pendente a configuração
@app.route('/login')
def login() -> str:
    return render_template('login.html')

# TODO: manutencao() Pendente a configuração
@app.route('/manutencao')
def manutencao() -> str:
    title = "Informações do Produto"
    className = 'ClassName = "op-info-produto"'
    description = "Em manutenção..."

    template = render_template(
        'menu-nav/manutencao.html',
        title=title,
        className=className,
        description=description
    )

    return template


if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
