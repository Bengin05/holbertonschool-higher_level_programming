const listMovies = document.getElementById('list_movies');

function fetchMovies() {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      data.results.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        listMovies.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error fetching movies:', error);
    });
}

fetchMovies();
