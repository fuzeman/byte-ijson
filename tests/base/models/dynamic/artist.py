from byte.model import Model
from byte.property import Property


class Artist(Model):
    id = Property(int, primary_key=True)

    title = Property(str)
