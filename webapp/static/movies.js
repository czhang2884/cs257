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
    onMoviesLoad(search_box_text, 0);
}

function onMoviesLoad(movieString, page) {
    let url = getAPIBaseURL() + '/movies/' + movieString + '/' + page;
    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(movies) {
        let listBody = '<ul class="skeleton_product">';
        for (let k = 0; k < movies.length && k < 50; k++) {
            let movie = movies[k];
            listBody += '<li class="movie_items"><div class="movie_item_box"><span class="popuptext">' + movie['overview'] + '</span>'
                            + '<img class="img_movie_items" src="' + movie['image_link'] + '">'
                            + '</div><div class="text_movie_items"><a href="/bios/' + movie['id'] + '" target="_blank">'
                            + movie['movie_title'] + '</a> ' + movie['release_year'] + '</div></li>';
        }
        listBody += '</ul>';
        // Insert results into html
        let displayUserInput = document.getElementById('display_user_input');
        let listMovies = document.getElementById('movies_list');
        if (listMovies) {
            displayUserInput.innerHTML = "Results for '" + movieString + "'";
            listMovies.innerHTML = listBody;
        }

        // Insert numbers into bottom of html
        let resultsBody = '';
        let index = movies.length / 50;
        for (let j = 0; j < index; j++) {
            if (j == page) {
                resultsBody += '| ' + (j + 1) + ' '
            } else {
                resultsBody += "| " + '<a href="#" onclick="onMoviesLoad(\'' + movieString + '\', \'' + j + '\');">' + (j + 1) + '</a>' + ' ';
            }
        }
        // resultsBody += '| ' + '<a href="#" onclick="onMoviesLoad(' + movieString + ', ' + (j + 1) + ');return false;">' + (j + 1) + '</a>' + ' ';
        resultsBody += '|'
        let results_page_numbers = document.getElementById('results_page_numbers');
        if (results_page_numbers) {
            results_page_numbers.innerHTML = resultsBody;
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

    // .then(function(movies) {
    //     let listBody = '<ul>';
    //     for (let k = 0; k < movies.length; k++) {
    //         let movie = movies[k];
    //         listBody += '<li>' + movie['movie_title'] + '</li>'
    //                     + '<li>' + movie['release_year'] + '</li>'
    //                     + '<li>' + movie['image_link'] + '</li>'
    //                     + '<li>' + movie['overview'] + '</li>';
    //     }
    //     listBody += '</ul>';
    //     let movie_bio_box = document.getElementById('movie_bio_box');
    //     movie_bio_box.innerHTML = listBody;
    // })

    .then(function(movies) {
        let movie = movies[0];
        let director_id_array = movie['director_id'].split(", ");
        for (let m = 0; m < director_id_array.length; m++) {
            getDirectors(director_id_array[m]);
        }

        // Text for movie_bio_box
        let listBody = '<h1 style="margin:10px; text-align:center">' + movie['movie_title'] + '</h1>' 
                    + '<h2 style="margin:10px; text-align:center">Release Year: ' + movie['release_year'] + '</h2>' 
                    + '<img class="bio_img" src="' + movie['image_link'] + '">' 
                    + '<h4 style="margin:10px">Overview</h4>'
                    + '<p style="margin:10px">' + movie['overview'] + '</p>' 
        let movie_bio_box = document.getElementById('movie_bio_box');
        movie_bio_box.innerHTML = listBody;

        // Text for budget
        let budgetBody = '<li>' + movie['budget'] + '</li>';
        let budgetList = document.getElementById('budget_list');
        budgetList.innerHTML = budgetBody;

        // Text for revenue
        let revenueBody = '<li>' + movie['revenue'] + '</li>';
        let revenueList = document.getElementById('revenue_list');
        revenueList.innerHTML = revenueBody;

        // Text for runtime
        let runtimeBody = '<li>' + movie['runtime'] + ' minutes</li>';
        let runtimeList = document.getElementById('runtime_list');
        runtimeList.innerHTML = runtimeBody;


        // listBody += '<h1 style="margin:10px; text-align:center">' + movie['movie_title'] + '</h1>' 
        // + '<h2 style="margin:10px; text-align:center">Release Year: ' + movie['release_year'] + '</h2>' 
        // + '<img class="bio_img" src="' + movie['image_link'] + '">' 
        // + '<h4 style="margin:10px">Overview</h4>'
        // + '<p style="margin:10px">' + movie['overview'] + '</p>' 
        // + '<h4 style="margin:10px">Other Info</h4>'
        // + '<p style="margin:10px">Language of Movie Title: ' + movie['title_lang'] + '<br>'
        // + 'Language of Original Movie: ' + movie['title_lang'] + '<br>'
        // + 'Budget: ' + movie['budget'] + ' Revenue: ' + movie['revenue'] + '<br>'
        // + 'Runtime: ' + movie['runtime'] + '<br>'
        // + 'Adult Movie' + movie['adult'] + '</p>';

        // 'mubi_url':row[4],
        // 'title_lang':row[5],
        // 'orig_lang':row[6],
        // 'runtime':row[7],
        // 'adult':row[8],
        // 'budget':int(row[9]),
        // 'revenue':int(row[10])

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

// Get directors
function getDirectors(director_id) {
    let url = getAPIBaseURL() + '/directors/' + director_id;
    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(directors) {
        let listBody = '';
        for (let k = 0; k < directors.length; k++) {
            let director = directors[k];
            listBody += '<li><a href="' + director['director_url'] + '" target="_blank">' + director['name'] + "</a></li>";
        }
        let directors_list = document.getElementById('directors_list');
        directors_list.insertAdjacentHTML('beforeend', listBody);
    })

    .catch(function(error) {
        console.log(error);
    })
}