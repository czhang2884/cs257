
'''
    olympics-schema.sql
    Carl Zhang, 12 Oct 2022
'''

CREATE TABLE athletes (
    athlete_id INTEGER,
    fullname TEXT,
    sex TEXT,
    team TEXT,
    noc TEXT,
    sport TEXT
);

CREATE TABLE games (
    id SERIAL,
    game TEXT
);

CREATE TABLE games_traits (
    game_id INTEGER,
    year INTEGER,
    season TEXT,
    city TEXT
);

CREATE TABLE events (
    id SERIAL,
    event TEXT
);

CREATE TABLE event_results (
    athlete_id INTEGER,
    game_id INTEGER,
    event_id INTEGER,
    medal TEXT
);

CREATE TABLE medal_count (
    noc_id integer,
    noc_name TEXT,
    gold integer,
    silver integer,
    bronze integer
);
