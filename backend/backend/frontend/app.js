async function analyze() {
    const desc = document.getElementById('description').value;
    const resultElement = document.getElementById('result');

    if (!desc.trim()) {
        resultElement.innerText = 'Veuillez entrer une description.';
        return;
    }

    try {
        const response = await fetch('https://ro-classifier.onrender.com/predict', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({description: desc})
        });

        const data = await response.json();

        if (data.error) {
            resultElement.innerText = 'Erreur : ' + data.error;
        } else {
            resultElement.innerText = 'Règle d’Or prédite : ' + data.RO;
        }
    } catch (error) {
        resultElement.innerText = 'Impossible de contacter le serveur. Vérifiez votre connexion.';
    }
}
