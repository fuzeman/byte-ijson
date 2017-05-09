from __future__ import absolute_import, division, print_function

from byte.formats.core.base import CollectionFormatPlugin, Format
from byte.formats.core.models import CollectionReader

from ijson.common import ObjectBuilder
import ijson
import json


class IterativeJsonCollectionFormat(CollectionFormatPlugin):
    key = 'ijson.python:collection'

    class Meta(CollectionFormatPlugin.Meta):
        content_type = 'application/json'
        extension = 'json'

    def encode(self, value, stream):
        json.dump(value, stream)

    def decode(self, stream):
        return IterativeJsonCollectionReader(ijson.parse(stream))


class IterativeJsonCollectionReader(CollectionReader):
    def __init__(self, events):
        super(IterativeJsonCollectionReader, self).__init__()

        self._events = iter(events)

    @property
    def closed(self):
        return self._events is None

    def items(self):
        container_key, container_type = self._parse_container_start(next(self._events))

        container_end_event = 'end_' + container_type

        # Retrieve items from container
        while True:
            key, event, value = next(self._events)

            # Check if we've reached the end of the container
            if (key, event) == (container_key, container_end_event):
                break

            # Ignore container keys
            if event in ('map_key',):
                continue

            # Build dictionary item
            builder = ObjectBuilder()

            end_key = key
            end_event = event.replace('start', 'end')

            while (key, event) != (end_key, end_event):
                builder.event(event, value)

                key, event, value = next(self._events)

            # Yield item
            yield builder.value

        # Release resources
        self.close()

    def close(self):
        self._events = None

    @staticmethod
    def _parse_container_start((key, event, _)):
        if event not in ('start_map', 'start_array'):
            raise ValueError('Invalid container structure')

        if key != '':
            raise ValueError('Invalid container key')

        return key, event.replace('start_', '')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
