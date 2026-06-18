"""Parser interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import ParsedDocument, RawDocument


class BaseParser(ABC):
    """Parse raw documents into text documents."""

    @abstractmethod
    def parse(self, document: RawDocument) -> ParsedDocument:
        """Parse one raw document."""
