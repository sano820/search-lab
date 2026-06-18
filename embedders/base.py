"""Embedder interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import Chunk


class BaseEmbedder(ABC):
    """Generate vector embeddings for text chunks."""

    @abstractmethod
    def embed(self, chunks: list[Chunk]) -> list[list[float]]:
        """Return one embedding vector per chunk."""
