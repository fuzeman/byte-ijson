from tests.base.models.dynamic.album import Album
from tests.base.models.dynamic.artist import Artist

from byte.table import Model, Property


class Track(Model):
    class Options:
        slots = True

    id = Property(int, primary_key=True)
    artist = Property(Artist)
    album = Property(Album)

    title = Property(str)
