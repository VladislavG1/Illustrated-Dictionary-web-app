

function formingGroupFilterValue(clickedElement) {
    inputValue = document.getElementById('groups_input').value;
    groupSet = new Set(String(inputValue).split(","));
    group = clickedElement.getAttribute('data-category');
    if(clickedElement.classList.contains('inactive-category')) {
        groupSet.add(group);

        clickedElement.classList.remove('inactive-category');
        clickedElement.classList.add('active-category');
    }
    else {
        groupSet.delete(group);

        clickedElement.classList.remove('active-category');
        clickedElement.classList.add('inactive-category');
    }

    if(document.getElementById('groups_input').value) {
        document.getElementById('groups_input').value = Array.from(groupSet).join(',');
    }
    else {
        document.getElementById('groups_input').value = Array.from(groupSet).join('');
    }
}
