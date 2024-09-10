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
    memoryMenu();
}


/**
 * Armazena um valor booleano na memória.
 * 
 */
function memoryMenu() {
    const elements = document.querySelectorAll('.op-hidden');
    if (elements.length > 0){
        sessionStorage.setItem('menu', false);
    }
    else {
        sessionStorage.setItem('menu', true);
    }
}

/**
 * Inicia a classe hidden nas tags caso haja valor armazenado na memória.
 * 
 */
function startMenu() {
    let store = sessionStorage.getItem('menu');
    if (store == 'true') {
        const elements = document.querySelectorAll('.op-word');
        elements.forEach((element) => {
            if (elements.length > 0) {
                element.classList.toggle('op-hidden');
            }
        });
    }
}

startMenu();
