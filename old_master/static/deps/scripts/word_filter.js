

function formingLetterFilterValue(clickedElement) {
    inputValue = document.getElementById('letters_input').value;
    letterSet = new Set(String(inputValue).split(""));
    letter = clickedElement.innerHTML.slice(0, 1);
    if(clickedElement.classList.contains('alphabet-letter-inactive')) {
        letterSet.add(letter);

        clickedElement.classList.remove('alphabet-letter-inactive');
        clickedElement.classList.add('alphabet-letter-active');
    }
    else {
        letterSet.delete(letter);

        clickedElement.classList.remove('alphabet-letter-active');
        clickedElement.classList.add('alphabet-letter-inactive');
    }

    document.getElementById('letters_input').value = Array.from(letterSet).join('');
}
