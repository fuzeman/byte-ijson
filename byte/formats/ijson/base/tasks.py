"""byte-ijson - tasks module."""
from __future__ import absolute_import, division, print_function

from byte.formats.ijson.base.decoder import IterativeJsonDecoder
from byte.formats.json.tasks import JsonSelectTask, JsonReadTask


class IterativeJsonSelectTask(JsonSelectTask):
    """Select task."""

    def __init__(self, executor, fmt, operation):
        """Create select task.

        :param executor: Executor
        :type executor: byte.executors.core.base.Executor

        :param fmt: Format
        :type fmt: byte.formats.ijson.base.main.BaseIterativeJsonCollectionFormat

        :param operation: Select operation
        :type operation: byte.compilers.core.models.SelectOperation
        """
        super(IterativeJsonSelectTask, self).__init__(executor, operation)

        self.format = fmt

    def open(self):
        """Open task."""
        super(JsonReadTask, self).open()

        # Create decoder
        self.decoder = IterativeJsonDecoder(self.format.parse(self.stream))

    def decode(self):
        """Decode items."""
        return self.decoder.items()
