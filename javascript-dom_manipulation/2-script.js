const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');

function addRedClass() {
  header.classList.add('red');
}

redHeader.addEventListener('click', addRedClass);
