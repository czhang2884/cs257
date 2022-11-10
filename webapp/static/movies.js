/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 */

window.onload = initialize;

function initialize() {

    let element = document.getElementById('movie_button');
    if (element) {
        element.onclick = onMoviesButton;
    }
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
        let tableBody = '';
        for (let k = 0; k < movies.length; k++) {
            let movie = movies[k];
            tableBody += '<ul><tr>'
                            + '<td> ' + movie['id'] + ' <td>'
                            + '<td> ' + movie['movie_title'] + ' <td>'
                            + '<td> ' + movie['release_year'] + ' <td>'
                            + '<tr></ul>\n';
        }

        let moviesTable = document.getElementById('movies_table');
        if (moviesTable) {
            moviesTable.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    })
}


