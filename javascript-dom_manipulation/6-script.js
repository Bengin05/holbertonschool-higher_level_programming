const character = document.getElementById('character');

function fetchCharacter() {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      character.textContent = data.name;
    })
    .catch(error => {
      console.error('Error fetching character:', error);
    });
}

fetchCharacter();
