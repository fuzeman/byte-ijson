"""byte-ijson - yajl format module."""
from __future__ import absolute_import, division, print_function

from byte.formats.ijson.base.main import BaseIterativeJsonCollectionFormat

import ijson.backends.yajl as ijson


class IterativeJsonYajlCollectionFormat(BaseIterativeJsonCollectionFormat):
    """Iterative JSON (ijson) collection format with yajl backend."""

    key = 'ijson.yajl:collection'

    def parse(self, stream):
        """Parse stream into events.

        :param stream: Stream
        """
        return ijson.parse(stream)
