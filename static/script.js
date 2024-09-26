document.getElementById('generateBtn').addEventListener('click', async () => {
    const inputText = document.getElementById('inputText').value;

    if (inputText.trim() === '') {
        alert('Por favor, insira um texto.');
        return;
    }

    // Mostrando um carregando (opcional)
    document.getElementById('outputText').innerText = "Pensando...";

    // Fazer requisição para a API local
    const response = await fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input_text: inputText }),
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('outputText').innerText = data.generated_text;
    } else {
        console.error('Erro na requisição:', response.status);
        document.getElementById('outputText').innerText = "Erro ao gerar texto. Tente novamente.";
    }
});
