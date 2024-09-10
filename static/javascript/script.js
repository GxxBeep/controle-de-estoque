/* TODO: CADASTRO 3 - EXIBIR IMAGENS AO ADICIONAR,
    E ADICIONAR DESCRIÇÃO DA IMAGEM 
*/

/* TODO: Criar função para redimencionar imagens no grid
    Cadastro de Protudo, ElementoID: cadastroProduto-3
    Exemplo: 
        width = (Altura / 10)
        heigth = (Largura / 10) 
*/

/**
 * Altera a visibilidade do menu.
 * 
 */
function holdMenu() {
    const elements = document.querySelectorAll('.op-word');

    elements.forEach((element) => {
        if (elements.length > 0) {
            element.classList.toggle('op-hidden');
        }
    });
}

/* TODO: Adicionar funcionalidade para quando trocar de página,
não desfaça a mudança feita pela função holdMenu(). */
