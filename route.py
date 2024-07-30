from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os


UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/cadastrar-produto/', methods=('GET', 'POST'))
def cadastrar_produto():

    categoria = ['Blusas', 'Calças', 'Camisas',
                'Casacos', 'Jaquetas', 'Macacões', 
                'Saias', 'Sapatos', 'Shorts', 'Vestidos']
    
    #TODO: Espeficar tamanho para cada categoria
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
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                return redirect(request.url)
    
                

    template = render_template('menu-nav/cadastro.html', categoria=categoria)

    return template






































#
# Pendente a configuraçáo
#
@app.route('/editar-produto')
def editar_produto():
    title = "Editar informações do Produto"
    className = 'ClassName = "op-editor-produto"'
    description = "Em manutenção..."

    template = render_template(
        'menu-nav/manutencao.html',
        title=title,
        className=className,
        description=description
        )

    return template


#
# Pendente a configuraçáo
#
@app.route('/remover-produto')
def remover_produto():
    title = "Remover um Produto"
    className = 'ClassName = "op-remover-produto"'
    description = "Em manutenção..."

    template = render_template(
        'menu-nav/manutencao.html',
        title=title,
        className=className,
        description=description
        )

    return template


#
# Pendente a configuraçáo
#
@app.route('/listar-produtos')
def listar_produtos():
    title = "Listar todos os Produtos"
    className = 'ClassName = "op-list-produto"'
    description = "Em manutenção..."

    template = render_template(
        'menu-nav/manutencao.html',
        title=title,
        className=className,
        description=description
        )

    return template


#
# Pendente a configuraçáo
#
@app.route('/info-produto')
def info_produto():
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










@app.route('/login')
def login():
    return render_template('login.html')







if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, host='26.43.221.95')