CREATE TABLE movies (
    id serial,
    movie_title text,
    release_year float,
    genre_id integer,
    overview text,
    popularity integer,
    image_id integer,
    review_id integer
);

CREATE TABLE reviews (
    id serial,
    movie_id integer,
    review_score integer,
    review_comment text,
    users_name text
);

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