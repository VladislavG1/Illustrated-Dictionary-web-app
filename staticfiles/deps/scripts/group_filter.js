

function formingGroupFilterValue(clickedElement) {
    inputValue = document.getElementById('groups_input').value;
    groupSet = new Set(String(inputValue).split(","));
    group = clickedElement.value;
    if(clickedElement.classList.contains('btn-primary')) {
        groupSet.add(group);

        clickedElement.classList.remove('btn-primary');
        clickedElement.classList.add('btn-success');
    }
    else {
        groupSet.delete(group);

        clickedElement.classList.remove('btn-success');
        clickedElement.classList.add('btn-primary');
    }

    if(document.getElementById('groups_input').value) {
        document.getElementById('groups_input').value = Array.from(groupSet).join(',');
    }
    else {
        document.getElementById('groups_input').value = Array.from(groupSet).join('');
    }
}
