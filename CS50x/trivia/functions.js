function checkAnswer(button, correctness)
{
    if (correctness === 'correct')
    {
        button.style.backgroundColor = 'green';
        document.getElementById('part1-result').textContent = 'Correct!';
    }

    else
    {
        button.style.backgroundColor = 'red';
        document.getElementById('part1-result').textContent = 'Incorrect';
    }

}

function checkFreeResponse() {
    const input = document.getElementById('name');
    const result = document.getElementById('part2-result');
    if (input.value.toLowerCase() === 'j.r.r. tolkien' || input.value.toLowerCase() === 'jrr tolkien' || input.value.toLowerCase() === 'john ronald reuel tolkien' || input.value.toLowerCase() === 'tolkien')
    {
        input.classList.add('correct');
        result.textContent = 'Correct!';
    }
    else
    {
        input.classList.add('incorrect');
        result.textContent = 'Incorrect';
    }
}
