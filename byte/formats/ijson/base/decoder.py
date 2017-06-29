"""byte-ijson - iterative json decoder module."""
from __future__ import absolute_import, division, print_function

from ijson.common import ObjectBuilder


class IterativeJsonDecoder(object):
    """JSON Decoder."""

    def __init__(self, events):
        """Create JSON Decoder."""
        self.events = events

    @property
    def closed(self):
        """Retrieve boolean representing the decoder "closed" status."""
        return self.events is None

    def items(self):
        """Retrieve item iterator."""
        container_key, container_type = self._parse_container_start(next(self.events))

        container_end_event = 'end_' + container_type

        # Retrieve items from container
        while True:
            key, event, value = next(self.events)

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

                key, event, value = next(self.events)

            # Yield item
            yield builder.value

    def close(self):
        """Close decoder."""
        if self.events is None:
            return

        self.events = None

    @staticmethod
    def _parse_container_start(event):
        key, event, _ = event

        if event not in ('start_map', 'start_array'):
            raise ValueError('Invalid container structure')

        if key != '':
            raise ValueError('Invalid container key')

        return key, event.replace('start_', '')

    def __enter__(self):
        """Enter decoder context."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit decoder context (close decoder)."""
        self.close()
