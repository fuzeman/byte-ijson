from __future__ import absolute_import, division, print_function

from byte.formats.ijson_python import IterativeJsonCollectionFormat, IterativeJsonCollectionReader

from six import StringIO


def test_encode_collection():
    fmt = IterativeJsonCollectionFormat()
    buf = StringIO()

    fmt.encode([{'label': 'One', 'value': 1}], buf)

    assert buf.getvalue() == '[{"value": 1, "label": "One"}]'


def test_decode_collection():
    fmt = IterativeJsonCollectionFormat()
    buf = StringIO('[{"value": 1, "label": "One"}]')

    result = fmt.decode(buf)

    assert isinstance(result, IterativeJsonCollectionReader)

    assert list(result.items()) == [
        {'label': 'One', 'value': 1}
    ]
