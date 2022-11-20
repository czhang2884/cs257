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

    // User presses enter
    let movie_input1 = document.getElementById('movie_search_box');
    movie_input1.addEventListener("keypress", onEnterPressedMain);

    let movie_input2 = document.getElementById('movie_search_box2');
    movie_input2.addEventListener("keypress", onEnterPressedSub);

}

// Enter press for main search
function onEnterPressedMain(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById('movie_search_button').click();
    }
}

// Enter press for sub search
function onEnterPressedSub(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById('movie_search_button2').click();
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

function onMovieSubmit() {

    // Assign variables to html elements
    let search_elements = document.getElementById("search_elements");
    let results_elements = document.getElementById("results_elements");

    // Checks which search box is being used and gets input. If main search box, hides elements and shows new elements.
    if (results_elements.style.display == "none") {
        search_elements.style.display = "none";
        results_elements.style.display = "block";

        search_box_text = document.getElementById('movie_search_box').value;
    } else {        
        search_box_text = document.getElementById('movie_search_box2').value;
    }

    // Get movies based on what user put into search box
    onMoviesLoad(search_box_text);
}

function onMoviesLoad(movieString) {
    let url = getAPIBaseURL() + '/movies/' + movieString;
    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        let listBody = '<ul class="skeleton_product">';
        for (let k = 0; k < movies.length; k++) {
            let movie = movies[k];
            listBody += '<li class="movie_items"><div class="movie_item_box"><span class="popuptext">' + movie['overview'] + '</span>'
                            + '<img class="img_movie_items" src="' + movie['image_link'] + '">'
                            + '</div><div class="text_movie_items"><a href="/bios/' + movie['id'] + '" target="_blank">'
                            + movie['movie_title'] + '</a> ' + movie['release_year'] + '</div></li>';
        }
        listBody += '</ul>';
        let displayUserInput = document.getElementById("display_user_input");
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

// Displays movie info on bio page
function onMoviesClick(movie_id) {
    let url = getAPIBaseURL() + '/movie_bio/' + movie_id;
    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        let listBody = '<ul>';
        for (let k = 0; k < movies.length; k++) {
            let movie = movies[k];
            listBody += '<li>' + movie['movie_title'] + '</li>'
                        + '<li>' + movie['release_year'] + '</li>'
                        + '<li>' + movie['image_link'] + '</li>'
                        + '<li>' + movie['overview'] + '</li>';
        }
        listBody += '</ul>';
        let movie_bio_box = document.getElementById('movie_bio_box');
        movie_bio_box.innerHTML = listBody;
    })

    .catch(function(error) {
        console.log(error);
    })
}

// Called when bios.html loads
function onBioLoad() {
    queryString = window.location.pathname.replace('/bios/', '');
    movie_bio_string = onMoviesClick(queryString);
}