from __future__ import absolute_import, division, print_function

from byte.formats.ijson_python import IterativeJsonCollectionFormat, IterativeJsonCollectionReader

import ijson.backends.yajl2 as ijson_yajl2


class Yajl2IterativeJsonCollectionFormat(IterativeJsonCollectionFormat):
    key = 'ijson.yajl2:collection'

    class Meta(IterativeJsonCollectionFormat.Meta):
        content_type = 'application/json'
        extension = 'json'

    def decode(self, stream):
        return IterativeJsonCollectionReader(ijson_yajl2.parse(stream))
