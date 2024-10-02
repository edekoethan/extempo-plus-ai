document.getElementById("medication-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('/get_instructions', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("response").innerText = `Error: ${data.error}`;
        } else {
            document.getElementById("response").innerText = `Instructions: ${data.data}`;
        }
    })
    .catch(error => {
        document.getElementById("response").innerText = `Error: ${error.message}`;
    });
});
