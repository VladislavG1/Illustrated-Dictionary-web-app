

function formingLetterFilterValue(clickedElement) {
    inputValue = document.getElementById('letters_input').value;
    letterSet = new Set(String(inputValue).split(""));
    letter = clickedElement.innerHTML.slice(0, 1);
    if(clickedElement.classList.contains('btn-primary')) {
        letterSet.add(letter);
        console.log(letterSet);

        clickedElement.classList.remove('btn-primary');
        clickedElement.classList.add('btn-success');
    }
    else {
        letterSet.delete(letter);
        console.log(letterSet);

        clickedElement.classList.remove('btn-success');
        clickedElement.classList.add('btn-primary');
    }

    document.getElementById('letters_input').value = Array.from(letterSet).join('');
    console.log("Hi, America!");
}

function fillLetterSet() {
    console.log("Hi, America!");
    console.log(letterSet);
}
