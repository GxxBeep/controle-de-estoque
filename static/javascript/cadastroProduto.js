const imagens_selecionadas = []; // Array para armazenar as imagens selecionadas.

/**
 * Manipula a seleção de imagens pelo usuário, exibindo-as na tela e permitindo a remoção individual.
 * 
 * @event change - Disparado quando o usuário seleciona novas imagens no input file.
 * @this {HTMLInputElement} - Referência ao elemento <input type="file">.
 * @return {void} - Esta função não retorna valores, apenas manipula o DOM e a array de imagens.
 */
document.getElementById('cadastroBntImage').addEventListener('change', function () {
    const output = document.getElementById('cadastroOutputImagens'); // Elemento onde as imagens serão exibidas
    
    // Converte a lista de arquivos em um array e processa cada imagem.
    Array.from(this.files).forEach((file, index) => {
        imagens_selecionadas.push(file); // Adiciona a imagem ao array

        // Cria um elemento <div> para cada imagem.
        const _div = document.createElement('div');
        _div.className = "imgContainer";

        // Cria um elemento <img>.
        const _img = document.createElement('img');
        _img.src = URL.createObjectURL(file); // Gera um URL temporário para a visualização
        _img.alt = file.name; // Define o atributo alt para o nome da imagem

        // Cria um botão para remover a imagem
        const _removeButton = document.createElement('button');
        _removeButton.className = "removeImg";
        _removeButton.textContent = "X";

        /** Evento de clique para remover a imagem
        * @event click - Disparado quando o botão "X" é clicado
        */
        _removeButton.onclick = function () {
            const imgToRemove = imagens_selecionadas.indexOf(file); // Encontra a imagem na array
            if (imgToRemove > -1) {imagens_selecionadas.splice(imgToRemove, 1);} // Remove a imagem da array
            output.removeChild(_div); // Remove o elemento <div> da tela
        };

        // Adiciona os elementos ao container
        output.appendChild(_div);
        _div.appendChild(_img);
        _div.appendChild(_removeButton);
    });
    // Limpa o campo de seleção de arquivos.
    this.value = '';
});


/**
 * Envia as imagens selecionadas e o formulário para o servidor ao enviar o formulário de cadastro.
 * 
 * @event submit - Dispara quando o formulário de cadastro é enviado
 * @this {HTMLFormElement} - Referência ao elemento <form>
 * @return {void} - Retorna uma Promise que representa a finalização do envio dos dados.
 */
document.getElementById('cadastroForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Previne o envio padrão do formulário.
    // Obtém o formulário de cadastro.
    const form = document.getElementById('cadastroForm'); 
    // Cria um objeto FormData com os dados do formulário.
    const formData = new FormData(form);
    // Adiciona as imagens selecionadas ao objeto FormData.
    imagens_selecionadas.forEach(image => {
        formData.append('imagens', image);
    });
    // Envia o objeto FormData para o servidor.
    fetch(this.action, {
        method: 'POST',
        body: formData // passa o objeto FormData como corpo da requisição.
    }).then(response => {
        if (!response.ok) {
            throw new Error('Ocorreu um problema ao enviar as imagens. Por favor, tente novamente.');
        } else {
            // Redireciona para a rota cadastro de produtos.
            window.location.href = response.url;
        }
    }).catch(error => {
        console.error('Error:', error);
    });
});