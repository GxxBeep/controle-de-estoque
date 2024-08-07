from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os


UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#
# Pendente a configuraçáo
#
@app.route('/')
def index() -> str:
    return render_template('index.html')


def allowed_file(filename) -> bool:
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#
# Pendente a configuraçáo
#
@app.route('/cadastrar-produto/', methods=('GET', 'POST'))
def cadastrar_produto() -> str:

    categoria: list[str] = ['Blusas', 'Calças', 'Camisas',
                            'Casacos', 'Jaquetas', 'Macacões',
                            'Saias', 'Sapatos', 'Shorts', 'Vestidos']

    # TODO: Espeficar tamanho para cada categoria
    camisa_tam_fem = ''
    camisa_tam_mas = ''

    if request.method == 'POST':
        value = request.form['produtoNome']
        if not value:
            flash('Não foi')
        else:
            print(request.form['produtoNome'])
            print(request.form['categoria'])

            if 'image' not in request.files:
                flash('Sem arquivos')
                return redirect(request.url)

            file = request.files['image']

            if file.filename == '':
                flash('Nenhum arquivo selecionado')
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], file.filename))
                return redirect(request.url)

    template = render_template('menu-nav/cadastro.html', categoria=categoria)

    return template


#
# Pendente a configuraçáo
#
@app.route('/editar-produto')
def editar_produto() -> str:

    template = render_template('menu-nav/editor.html')

    return template


#
# Pendente a configuraçáo
#
@app.route('/listar-produtos')
def listar_produtos() -> str:
    template = render_template('menu-nav/list-product.html')
    return template


#
# Pendente a configuraçáo
#
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
        'menu-nav/info-product.html',
        dictionary=dictionary,
        imagens=imagens)

    return template


@app.route('/login')
def login() -> str:
    return render_template('login.html')


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
