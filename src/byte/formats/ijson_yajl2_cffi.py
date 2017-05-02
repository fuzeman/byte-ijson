from __future__ import absolute_import, division, print_function

from byte.formats.ijson_python import IterativeJsonCollectionFormat, IterativeJsonCollectionReader

import ijson.backends.yajl2_cffi as ijson_yajl2_cffi


class Yajl2CffiIterativeJsonCollectionFormat(IterativeJsonCollectionFormat):
    key = 'ijson.yajl2_cffi:collection'

    class Meta(IterativeJsonCollectionFormat.Meta):
        content_type = 'application/json'
        extension = 'json'

    def decode(self, stream):
        return IterativeJsonCollectionReader(ijson_yajl2_cffi.parse(stream))
