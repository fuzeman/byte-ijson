"""byte-ijson - python format module."""
from __future__ import absolute_import, division, print_function

from byte.formats.ijson.base.main import BaseIterativeJsonCollectionFormat

import ijson


class IterativeJsonCollectionFormat(BaseIterativeJsonCollectionFormat):
    """Iterative JSON (ijson) collection format."""

    key = 'ijson.python:collection'

    def parse(self, stream):
        """Parse stream into events.

        :param stream: Stream
        """
        return ijson.parse(stream)
