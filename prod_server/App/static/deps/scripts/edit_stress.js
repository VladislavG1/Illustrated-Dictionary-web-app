document.addEventListener('DOMContentLoaded', function () {

    function addEditForm() {
        // Получаем элемент, в который будем вставлять форму
        const outputElement = document.getElementById('edit_stress');
        outputElement.innerHTML = ''; // Очищаем предыдущее содержимое

        // Создаем форму
        const form = document.createElement('form');

        // Увеличиваем расстояние между буквами
        const letterSpacing = 10; // Значение расстояния в пикселях

        // Функция для обновления формы в реальном времени
        function updateForm(word) {
            // Находим элементы checkbox и span в форме
            const checkboxes = form.querySelectorAll('input[type="checkbox"]');
            const letterSpans = form.querySelectorAll('span');

            // Обновляем значения checkboxes и span
            for (let i = 0; i < word.length; i++) {
                if (i < checkboxes.length) {
                    checkboxes[i].checked = false; // Сбрасываем галочку
                    letterSpans[i].textContent = word[i];
                    for (let j = 0; j < letterSpacing; j++) {
                        letterSpans[i].textContent += ' ';
                    }
                } else {
                    // Создаем новые элементы, если их недостаточно
                    const div = document.createElement('div');
                    div.style.display = 'inline-block';
                    div.style.position = 'relative';

                    if(word[i] !== " ") {
                        const checkbox = document.createElement('input');
                        checkbox.type = 'checkbox';
                        checkbox.style.position = 'absolute';
                        checkbox.style.top = '-15px'; // Позиционируем галочку над буквой
                        checkbox.style.left = '0';
                        checkbox.style.marginLeft = '10px';
                        checkbox.style.marginRight = '8px';
                        checkbox.setAttribute('data-stress-number', i);
                        div.appendChild(checkbox);
                    }

                    const letterSpan = document.createElement('span');
                    letterSpan.textContent = word[i];
                    letterSpan.style.fontSize = '20px'; // Размер шрифта буквы
                    letterSpan.style.margin = '10px';

                    for (let j = 0; j < letterSpacing; j++) {
                        letterSpan.textContent += ' ';
                    }

                    div.appendChild(letterSpan);
                    form.appendChild(div);
                }
            }

            // Удаляем лишние элементы, если слово стало короче
            if (word.length < checkboxes.length) {
                for (let i = word.length; i < checkboxes.length; i++) {
                    form.removeChild(checkboxes[i].parentElement);
                }
            }
        }

        // Получаем поле ввода
        const inputField = document.getElementById('id_name');

        // Добавляем обработчик события input
        inputField.addEventListener('input', function () {
            updateForm(this.value);
        });

        // Вставляем форму в элемент
        outputElement.appendChild(form);

        // Инициализируем форму с начальным значением
        updateForm(inputField.value);
    }

    function setDefaultCheckboxes() {
        stress = document.getElementById('id_stress').value;
        numbers = stress.split('_');
        console.log(numbers);
        for (const number of numbers) {
            checkboxes = document.querySelectorAll('[data-stress-number]');
            for (const checkbox of checkboxes) {
                if (checkbox.getAttribute('data-stress-number') == number) {
                    checkbox.checked = true;
                }
            }
        }
    }

    function updateStress() {
        checkboxes = document.querySelectorAll('[data-stress-number]');
        for (const checkbox of checkboxes) {
            checkbox.addEventListener('change', function () {
                stress = createCheckNumbers();
                console.log(stress);
                document.getElementById('id_stress').value = stress;
            });
        }
    }

    function createCheckNumbers() {
        checkboxes = document.querySelectorAll('[data-stress-number]');
        checkNumbers = "";
        for (const checkbox of checkboxes) {
            if (checkbox.checked) {
                checkNumber = checkbox.getAttribute('data-stress-number');
                checkNumbers += checkNumber + '_';
            }
        }
        checkNumbers = checkNumbers.slice(0, -1);
        return checkNumbers;
    }

    inputName = document.getElementById('id_name');
    if (inputName) {
        console.log(inputName.value);

        addEditForm();
        setDefaultCheckboxes();
        if(inputName.value.trim() == '') {
            let timeoutId;
            inputName.addEventListener('input', function () {
                clearTimeout(timeoutId);
                timeoutId = setTimeout(function () {
                    if (inputName.value.trim() !== '') {
                        updateStress();
                    }
                }, 500);
            });
        }
        else updateStress();
    }
});