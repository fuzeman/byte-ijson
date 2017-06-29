from tests.base.models.dynamic.artist import Artist

from byte.table import Model, Property


class Album(Model):
    class Options:
        slots = True

    id = Property(int, primary_key=True)
    artist = Property(Artist)

    title = Property(str)
