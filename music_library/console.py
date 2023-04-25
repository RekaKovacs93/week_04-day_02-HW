# import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository  
# from db.run_sql import run_sql
import repositories.artist_repository as artist_repository



artist1 = Artist("Jim Morrison")
artist_repository.save(artist1)
artist2 = Artist("Robert Plant")
artist_repository.save(artist2)

album1 = Album("Morrison Hotel", artist1, "psychedelic rock", 1970)
album_repository.save(album1)

artist_repository.select_all()
album_repository.select_all()

print(album_repository.select(1).__dict__)

print(album_repository.select_by_artist(1).__dict__)