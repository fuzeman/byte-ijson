from tests.base.core.fixtures import get_fixture_uri
from tests.base.models.dynamic.album import Album
from tests.base.models.dynamic.artist import Artist
from tests.base.models.dynamic.city import City
from tests.base.models.dynamic.track import Track

from byte.table import Table
from hamcrest import *
import byte.compilers.operation
import byte.executors.file
import byte.formats.ijson.python
import pytest

pytestmark = pytest.mark.python


def test_all():
    with get_fixture_uri('databases/music/artists.json') as artists_uri:
        artists = Table(Artist, artists_uri, plugins=[
            byte.compilers.operation,
            byte.executors.file,
            byte.formats.ijson.python
        ])

        # Fetch artists, and validate properties
        assert_that(list(artists.all().iterator()), all_of(
            has_length(5),

            has_items(
                has_properties({
                    'id': 1,
                    'title': 'Gorillaz'
                }),
                has_properties({
                    'id': 2,
                    'title': 'Daft Punk'
                }),
                has_properties({
                    'id': 3,
                    'title': 'Friendly Fires'
                }),
                has_properties({
                    'id': 4,
                    'title': 'Miike Snow'
                }),
                has_properties({
                    'id': 5,
                    'title': 'LCD Soundsystem'
                })
            )
        ))


def test_create():
    with get_fixture_uri('databases/music/artists.json') as artists_uri:
        artists = Table(Artist, artists_uri, plugins=[
            byte.compilers.operation,
            byte.executors.file,
            byte.formats.ijson.python
        ])

        # Create artist
        artists.create(id=123, title='Fenech-Soler')

        # Fetch artist, and validate properties
        assert_that(artists.get(Artist['id'] == 123), has_properties({
            'id': 123,
            'title': 'Fenech-Soler'
        }))


def test_get_basic():
    with get_fixture_uri('databases/music/artists.json') as artists_uri:
        artists = Table(Artist, artists_uri, plugins=[
            byte.compilers.operation,
            byte.executors.file,
            byte.formats.ijson.python
        ])

        # Fetch artist, and validate properties
        assert_that(artists.get(Artist['id'] == 1), has_properties({
            'id': 1,
            'title': 'Gorillaz'
        }))


def test_get_relations():
    with get_fixture_uri((
        'databases/music/artists.json',
        'databases/music/albums.json',
        'databases/music/tracks.json'
    )) as (
        artists_uri,
        albums_uri,
        tracks_uri
    ):
        # Artists
        artists = Table(Artist, artists_uri, plugins=[
            byte.compilers.operation,
            byte.executors.file,
            byte.formats.ijson.python
        ])

        # Albums
        albums = Table(Album, albums_uri, plugins=[
            byte.compilers.operation,
            byte.executors.file,
            byte.formats.ijson.python
        ])

        albums.connect(
            artist=artists
        )

        # Tracks
        tracks = Table(Track, tracks_uri, plugins=[
            byte.compilers.operation,
            byte.executors.file,
            byte.formats.ijson.python
        ])

        tracks.connect(
            artist=artists,
            album=albums
        )

        # Fetch track, and ensure relations can be resolved
        assert_that(tracks.get(Track['id'] == 1), has_properties({
            'id': 1,
            'title': 'Ascension (feat. Vince Staples)',

            'artist': has_properties({
                'id': 1,
                'title': 'Gorillaz'
            }),

            'album': has_properties({
                'id': 1,
                'title': 'Humanz',

                'artist': has_properties({
                    'id': 1,
                    'title': 'Gorillaz'
                })
            })
        }))


def test_where():
    with get_fixture_uri('collections/cities.json') as cities_uri:
        cities = Table(City, cities_uri, plugins=[
            byte.compilers.operation,
            byte.executors.file,
            byte.formats.ijson.python
        ])

        # Fetch cities, and validate properties
        items = list(cities.select().where(City['country'] == 'New Zealand').iterator())

        assert_that(items, all_of(
            has_length(35),

            has_items(
                has_properties({
                    'id': '2179537',
                    'name': 'Wellington',

                    'country': 'New Zealand',
                    'subcountry': 'Wellington'
                }),
                has_properties({
                    'id': '2179670',
                    'name': 'Wanganui',

                    'country': 'New Zealand',
                    'subcountry': 'Manawatu-Wanganui'
                }),
                has_properties({
                    'id': '2181133',
                    'name': 'Timaru',

                    'country': 'New Zealand',
                    'subcountry': 'Canterbury'
                }),
                has_properties({
                    'id': '2181742',
                    'name': 'Taupo',

                    'country': 'New Zealand',
                    'subcountry': 'Waikato'
                }),
                has_properties({
                    'id': '2184155',
                    'name': 'Pukekohe East',

                    'country': 'New Zealand',
                    'subcountry': 'Auckland'
                }),
            )
        ))
