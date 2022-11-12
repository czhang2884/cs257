/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 */

window.onload = initialize;

function initialize() {
    let movies_list = document.getElementById('movies_list')
    if (movies_list) {
        window.onload = onMoviesLoad();
    }
    
    let movie_search_text = document.getElementById('movie_search_box');
    let movie_button = document.getElementById('movie_search_button');
    if (movie_button) {
        // GET INFO FROM SEARCH BOX
        movie_button.onclick = onMoviesLoad(movie_search_text.value);
    }
    
    // Useful for when we want to take user inputs
    /** window.addEventListener("DOMContentLoaded", (e) => {
        let btn = document.querySelector(".searchBtn");
        let input = document.querySelector(".inputSearch");

        btn.addEventListener("click", (e) => {
            searchFunction(input.value);
        });
    }); **/
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

// Get string from search box and calls it with onMoviesload(Search_string)
function onMovieSubmit() {

}

function onMoviesLoad(movieString) {
    let url = getAPIBaseURL() + '/movies/' + movieString;
    
    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        let listBody = '<tr><th>Results for "' + movieString + '"</th></tr>';
        for (let k = 0; k < movies.length; k++) {
            let movie = movies[k];
            listBody += '<li><tr>'
                            + '<td> ' + movie['id'] + ' <td>'
                            + '<td> ' + movie['movie_title'] + ' <td>'
                            + '<td> ' + movie['release_year'] + ' <td>'
                            + '<tr></li>\n';
        }
        let listMovies = document.getElementById('movies_list');
        if (listMovies) {
            listMovies.innerHTML = listBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    })
}

