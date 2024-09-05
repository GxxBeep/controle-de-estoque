/* TODO: CADASTRO 3 - EXIBIR IMAGENS AO ADICIONAR,
    E ADICIONAR DESCRIÇÃO DA IMAGEM */

/* TODO: Criar função para redimencionar imagens no grid
    Cadastro de Protudo, ElementoID: cadastroProduto-3
    Exemplo: 
        width = (Altura / 10)
        heigth = (Largura / 10) */

/* Esconde o menu lateral. */
function holdMenu() {
    if (document.getElementsByClassName("op-hidden").length > 0) {
        elements = document.getElementsByClassName("op-word");
        for (let i = 0; i < elements.length; i++) {
            elements[i].classList.remove("op-hidden");
        }
    } else {
        elements = document.getElementsByClassName("op-word");
        for (let i = 0; i < elements.length; i++) {
            elements[i].classList.add("op-hidden");
        }
    }
}

/* TODO: Adicionar funcionalidade para quando trocar de página,
não desfaça a mudança feita pela função holdMenu(). */
