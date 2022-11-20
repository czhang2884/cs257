
CREATE TABLE movies (
    id numeric,
    movie_title text,
    release_year integer,
    genre text,
    overview text,
    popularity numeric,
    director_id text,
    mubi_url text,
    title_lang text,
    orig_lang text,
    runtime integer,
    adult integer
);

CREATE TABLE reviews (
    rating_id integer,
    user_id integer,
    movie_id integer,
    review_score integer,
    review_comment text,
    timestamp text
);

CREATE TABLE average_reviews (
    movie_id integer,
    average_review float,
    num_reviews integer
);

CREATE TABLE users (
    user_id integer,
    profile_pic text
);

CREATE TABLE profit (
    movie_id integer,
    budget numeric,
    revenue numeric
);

CREATE TABLE voting_average (
    movie_id integer,
    vote_avg float,
    vote_count integer
);

CREATE TABLE genres (
    id serial,
    genre text
);

CREATE TABLE images (
    movie_id integer,
    image_link text
);

CREATE TABLE directors (
    id integer,
    name text,
    director_url text
);


