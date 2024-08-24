const imagens_selecionadas = []; // Array para armazenar as imagens selecionadas.
/**
 * Adiciona as imagens no campo de exibição.
 * 
 * @event change - dispara quando ocorre o evento de seleção das imagens
 * @this {HTMLInputElement} - referencia ao elemento <input type="file">
 * @return {void} - Retorna nada
 */
document.getElementById('cadastroBntImage').addEventListener('change', function () {
    // Elemento de saída para exibir as imagens selecionadas.
    const output = document.getElementById('cadastroOutputImagens');
    // Cria uma array das imagens selecionadas.
    Array.from(this.files).forEach(file => {
        // Adiciona a imagem selecionada na array.
        imagens_selecionadas.push(file);
        // Cria um elemento <img> para cada imagem selecionada.
        const img = document.createElement('img');
        // Define o caminho da imagem como URL para o elemento <img>.
        img.src = URL.createObjectURL(file);
        // Define o atributo alt como o nome da imagem.
        img.alt = file.name;
        // Adiciona o elemento <img> ao elemento <div>.
        output.appendChild(img);
    });
    // Limpa o campo de seleção de arquivos.
    this.value = '';
});

/**
 * Envia as imagens selecionadas e o formulário para o servidor ao enviar o formulário de cadastro.
 * 
 * @event submit - dispara quando o formulário de cadastro é enviado
 * @this {HTMLFormElement} - referência ao elemento <form>
 * @return {void} - Retorna nada
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


// TODO: CRIAR FUNCIONALIDADE PARA RETIRAR A IMAGEM SELECIONADA.