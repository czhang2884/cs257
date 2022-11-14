/*
 * movies.js
 * Carl Zhang and Alex Falk
 * 11/12/2022
 */

window.onload = initialize;

function initialize() {
    
    // Main submit button
    let movie_button = document.getElementById('movie_search_button');
    movie_button.onclick = onMovieSubmit;

    // Secondary submit button
    let movie_button2 = document.getElementById('movie_search_button2');
    movie_button2.onclick = onMovieSubmit;

}

// Returns the base URL of the API, onto which endpoint
// components can be appended.
function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}

function onMovieSubmit() {

    let search_elements = document.getElementById("search_elements");
    let results_elements = document.getElementById("results_elements");

    if (results_elements.style.display == "none") {
        search_elements.style.display = "none";
        results_elements.style.display = "block";

        search_box_text = document.getElementById('movie_search_box').value;
    } else {
        search_box_text = document.getElementById('movie_search_box2').value;
    }
    onMoviesLoad(search_box_text);

}

function onMoviesLoad(movieString) {
    let url = getAPIBaseURL() + '/movies/' + movieString;
    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        let listBody = '';
        for (let k = 0; k < movies.length; k++) {
            let movie = movies[k];
            listBody += '<li><tr>'
                            + '<td> ' + movie['id'] + ' <td>'
                            + '<td><a href="/bios"> ' + movie['movie_title'] + ' </a><td>'
                            + '<td> ' + movie['release_year'] + ' <td>'
                            + '<tr></li>\n';
        }

        let displayUserInput = document.getElementById("display_user_input")
        let listMovies = document.getElementById('movies_list');
        if (listMovies) {
            displayUserInput.innerHTML = "Results for '" + movieString + "'";
            listMovies.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    })
}


