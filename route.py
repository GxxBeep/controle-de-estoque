from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar-produto')
def cadastrar_produto():
    title = "Cadastrar Produto"
    className = 'ClassName = "op-cadastro-produto"'
    description = "Em manutenção..."

    template = render_template(
        'menu-nav/manutencao.html',
        title=title,
        className=className,
        description=description
        )

    return template


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


if __name__ == '__main__':
    app.run(debug=True)