from __future__ import absolute_import, division, print_function

from six import StringIO
import pytest

try:
    from byte.formats.ijson_yajl import YajlIterativeJsonCollectionFormat, IterativeJsonCollectionReader
except ImportError:
    pass

pytestmark = pytest.mark.yajl


def test_encode_collection():
    fmt = YajlIterativeJsonCollectionFormat()
    buf = StringIO()

    fmt.encode([{'label': 'One', 'value': 1}], buf)

    assert buf.getvalue() == '[{"value": 1, "label": "One"}]'


def test_decode_collection():
    fmt = YajlIterativeJsonCollectionFormat()
    buf = StringIO('[{"value": 1, "label": "One"}]')

    result = fmt.decode(buf)

    assert isinstance(result, IterativeJsonCollectionReader)

    assert list(result.items()) == [
        {'label': 'One', 'value': 1}
    ]
