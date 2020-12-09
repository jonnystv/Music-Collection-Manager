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


def select_all():
    albums=[]

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['album_title'], row['album_genre'], row['album_artist'], row['id'])
        albums.append(album)
    return albums


# def select(id):
#     album = None
#     sql = "SELECT * FROM albums WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         album = Album(result['album_title'], result['album_genre'], result['album_artist'], result['id'])
#     return album