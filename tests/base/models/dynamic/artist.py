from byte.table import Model, Property


class Artist(Model):
    id = Property(int, primary_key=True)

    title = Property(str)
