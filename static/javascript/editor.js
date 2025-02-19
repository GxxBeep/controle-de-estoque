


async function fetchData(url, met, attr) {
    
    console.log('Executando fetchData:', url, met, attr);

    try{
        console.log('Enviando os dados:', url, met, attr);
        const response = await fetch(url, {
            method: met,
            headers: {
                'Content-Type': 'text/plain'
            },
            body: attr
        })
        
        console.log('Verificando resposta:', response);
        if(!response.ok) {
            alert('Ocorreu um erro ao enviar a ID. Verifique se o ID foi digitado corretamente.');
        }

        console.log('Resposta:', response);
        return await response.json();

    } catch (error) {
        console.error('Error:', error);
        alert('Houve um erro no banco de dados. Por favor, tente novamente.');
        return null
    }

}





async function sendID(id) {

    var inputValue = document.getElementById("editorInfo-idenInput").value;

    if (inputValue != "") {
        const response = await fetchData("/editar-produto", "POST", inputValue);
        console.log(response)
        
    } else {
        alert("Insira um ID");
    }

    
}