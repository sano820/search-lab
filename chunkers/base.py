"""Chunker interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import Chunk, ParsedDocument


class BaseChunker(ABC):
    """Split parsed documents into retrievable chunks."""

    @abstractmethod
    def chunk(self, document: ParsedDocument) -> list[Chunk]:
        """Return chunks for one parsed document."""
