from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repo

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repo.select(row['id'])
        album = Album(row['title'], artist, row['genre'], row['year'])
        albums.append(album)
    return albums

def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre, year) VALUES(%s, %s, %s, %s) RETURNING *"
    values = [album.title, album.artist_id, album.genre, album.year]
    rows = run_sql(sql, values)
    id = rows[0]['id']
    album.id = id
    return album

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    rows = run_sql(sql, values)
    if rows:
        album_info = rows[0]
        artist = artist_repo.select(album_info['artist_id'])
        album = Album(album_info['title'], artist, album_info['genre'], album_info['year'])
    return album

def delete_one(title):
    sql = "DELETE FROM albums WHERE title = %s"
    values = title
    run_sql(sql, values)

def select_by_artist(id):
    album = None
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [id]
    rows = run_sql(sql, values)
    if rows:
        album_info = rows[0]
        artist = artist_repo.select(album_info['artist_id'])
        album = Album(album_info['title'], artist, album_info['genre'], album_info['year'])
    return album