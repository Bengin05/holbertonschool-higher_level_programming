document.addEventListener('DOMContentLoaded', init);

function init() {
  const hello = document.getElementById('hello');
  fetchHello(hello);
}

function fetchHello(element) {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      element.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching hello:', error);
    });
}
