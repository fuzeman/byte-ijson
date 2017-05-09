"""byte-ijson - main module."""
from __future__ import absolute_import, division, print_function

from byte.formats.ijson.base.tasks import IterativeJsonSelectTask
from byte.formats.json import JsonCollectionFormat


class BaseIterativeJsonCollectionFormat(JsonCollectionFormat):
    """Iterative JSON (ijson) collection format."""

    key = None

    class Meta(JsonCollectionFormat.Meta):
        """Iterative JSON (ijson) collection format metadata."""

        content_type = 'application/json'
        extension = 'json'

    def parse(self, stream):
        """Parse stream into events.

        :param stream: Stream
        """
        raise NotImplementedError

    def select(self, executor, operation):
        """Execute select operation.

        :param executor: Executor
        :type executor: byte.executors.core.base.Executor

        :param operation: Select operation
        :type operation: byte.compilers.core.models.SelectOperation
        """
        return IterativeJsonSelectTask(executor, self, operation).execute()
