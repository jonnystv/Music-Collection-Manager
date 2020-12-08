from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (album_title, album_genre, album_artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_title, album.album_genre, album.album_artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album
    

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)