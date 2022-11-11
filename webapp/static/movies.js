/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 */

window.onload = initialize;

function initialize() {

    let element = document.getElementById('movie_search_button');
    if (element) {
        element.onclick = onMoviesButton;
    }

    let movies_list = document.getElementById('movies_list')
    if (movies_list) {
        movies_list.onload = onResultsLoad;
    }
    
    // Useful for when we want to take user inputs
    window.addEventListener("DOMContentLoaded", (e) => {
        let btn = document.querySelector(".searchBtn");
        let input = document.querySelector(".inputSearch");

        btn.addEventListener("click", (e) => {
            searchFunction(input.value);
        });
    });
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

function onMoviesButton() {
    let url = getAPIBaseURL() + '/movies/';
    
    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        let listBody = '';
        for (let k = 0; k < movies.length; k++) {
            let movie = movies[k];
            listBody += '<li><tr>'
                            + '<td> ' + movie['id'] + ' <td>'
                            + '<td> ' + movie['movie_title'] + ' <td>'
                            + '<td> ' + movie['release_year'] + ' <td>'
                            + '<tr></li>\n';
        }
        // NEED TO CALL onResultsLoad IN SOME WAY
        // NEEDS TO SAVE listBody AND CALL IT WHEN WEBPAGE LOADS
    })

    .catch(function(error) {
        console.log(error);
    })
}

function onResultsLoad(string) {

        let listMovies = document.getElementById('movies_list');
        if (listMovies) {
            listMovies.innerHTML = string;
        }
}

