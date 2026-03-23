const addItem = document.getElementById('add_item');
const myList = document.querySelector('ul.myList');

function addListItem() {
    const li = document.createElement('li');
    li.texteContent = 'Item';
    myList.appendChild(li);
}

addItem.addEventListener('click', addListItem);
