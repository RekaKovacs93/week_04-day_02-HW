from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repo

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        # album = album_repo.select(row['title'])
        artist = Artist(row['name'])
        artists.append(artist)
    return artists

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        # albums = album_repo.select(result['title'])
        artist = Artist(result['name'])
    return artist

def delete_one(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    rows = run_sql(sql, values)


