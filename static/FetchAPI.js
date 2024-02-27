async function generateText(prompt) {
    try {
        const response = await fetch('http://localhost:5000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({prompt: prompt}),
        });
        if (!response.ok) { // Check if response is ok (status in the range 200-299)
            throw new Error(`Network response was not ok (status: ${response.status})`);
        }
        const data = await response.json();
        document.getElementById('generated-text').innerText = data.generated_text; // Display text in HTML
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('generated-text').innerText = 'Sorry, an error occurred while generating text.'; // Provide a user-friendly error message
    }
}

function generateUserText() {
    const prompt = document.getElementById('prompt-input').value; // Get user input
    generateText(prompt).catch(error => console.error('Error with generating user text:', error));
}
