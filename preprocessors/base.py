"""Preprocessor interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import ParsedDocument


class BasePreprocessor(ABC):
    """Clean and normalize parsed text documents."""

    @abstractmethod
    def process(self, document: ParsedDocument) -> ParsedDocument:
        """Return a cleaned document."""
