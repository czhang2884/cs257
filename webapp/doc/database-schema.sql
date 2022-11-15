CREATE TABLE movies (
    id serial,
    movie_title text,
    release_year integer,
    genre_id integer,
    overview text,
    popularity integer,
    image_id integer,
    review_id integer
);

/*
CREATE TABLE movies (
    id numeric,
    movie_title text,
    release_year integer,
    genre text,
    overview text,
    popularity float
);
*/

CREATE TABLE reviews (
    id serial,
    movie_id integer,
    review_score integer,
    review_comment text,
    users_name text
);

/*
CREATE TABLE reviews (
    id integer,
    movie_id integer,
    review_score integer,
    review_comment text,
    users_name text
);
*/

CREATE TABLE average_reviews (
    movie_id integer,
    average_review float
);

CREATE TABLE genres (
    id serial,
    genre text
);

CREATE TABLE images (
    id serial,
    movie_id integer,
    image_link text
);

/*
CREATE TABLE images (
    movie_id integer,
    image_link text
);
*?