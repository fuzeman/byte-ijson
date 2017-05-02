from __future__ import absolute_import, division, print_function

from byte.formats.ijson_python import IterativeJsonCollectionFormat, IterativeJsonCollectionReader

import ijson.backends.yajl as ijson_yajl


class YajlIterativeJsonCollectionFormat(IterativeJsonCollectionFormat):
    key = 'ijson.yajl:collection'

    class Meta(IterativeJsonCollectionFormat.Meta):
        content_type = 'application/json'
        extension = 'json'

    def decode(self, stream):
        return IterativeJsonCollectionReader(ijson_yajl.parse(stream))
