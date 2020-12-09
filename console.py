import pdb
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

album_1 = Album("Imagine", "Rock", "John Lennon")
album_repository.save(album_1)

album_2 = Album("Band on the Run", "Rock", "Paul McCartney")
album_repository.save(album_2)

album_3 = Album("Wonderwall Music", "Experimental", "George Harrison")
album_repository.save(album_3)

album_4 = Album("Sentimental Journey", "Jazz", "Ringo Starr")
album_repository.save(album_4)

# pdb.set_trace()
artist_repository.select_all()

# pdb.set_trace()
album_repository.select_all()

# album_repository.select(id)
# pdb.set_trace()

# artist_repository.select(id)
# pdb.set_trace()

# artist_repository.delete_all()

# album_repository.delete_all()