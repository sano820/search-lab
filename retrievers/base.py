"""Retriever interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import SearchResult


class BaseRetriever(ABC):
    """Retrieve candidate search results."""

    @abstractmethod
    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        """Return top-k candidate results."""
