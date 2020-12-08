DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(255),
    first_name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    album_title VARCHAR(255),
    album_genre VARCHAR(255),
    album_artist VARCHAR(255)
);