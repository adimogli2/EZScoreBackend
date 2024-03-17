document.getElementById('submit').addEventListener('click', function() {
    var paragraph = document.getElementById('paragraph').value;
    var rubric = document.getElementById('rubric').value;

    fetch('/grade', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ paragraph: paragraph, rubric: rubric }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.feedback;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});