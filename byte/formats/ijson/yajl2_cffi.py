"""byte-ijson - yajl2-cffi format module."""
from __future__ import absolute_import, division, print_function

from byte.formats.ijson.base.main import BaseIterativeJsonCollectionFormat

import ijson.backends.yajl2_cffi as ijson


class IterativeJsonYajl2CffiCollectionFormat(BaseIterativeJsonCollectionFormat):
    """Iterative JSON (ijson) collection format with yajl2_cffi backend."""

    key = 'ijson.yajl2_cffi:collection'

    def parse(self, stream):
        """Parse stream into events.

        :param stream: Stream
        """
        return ijson.parse(stream)
