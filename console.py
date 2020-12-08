from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("John", "Lennon")
artist_repository.save(artist_1)

artist_2 = Artist("Paul", "McCartney")
artist_repository.save(artist_2)

artist_3 = Artist("George", "Harrison")
artist_repository.save(artist_3)

artist_4 = Artist("Ringo", "Starr")
artist_repository.save(artist_4)