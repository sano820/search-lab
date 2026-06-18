"""Indexer interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import Chunk


class BaseIndexer(ABC):
    """Store chunks and vectors in a search index."""

    @abstractmethod
    def add(self, chunks: list[Chunk], vectors: list[list[float]] | None = None) -> None:
        """Add chunks and optional vectors to the index."""
