function removeDuplicates(list) {
    const uniqueValues = {};

    for(const li of list) {
        const value = li.textContent;

        if(uniqueValues[value]) {
            li.remove();
        }
        else {
            uniqueValues[value] = true;
        }
    }
}

const liList = document.querySelectorAll('li#group_list_element');
removeDuplicates(liList);