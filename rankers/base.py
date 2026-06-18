"""Ranker interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import SearchResult


class BaseRanker(ABC):
    """Rerank candidate search results."""

    @abstractmethod
    def rerank(self, query: str, results: list[SearchResult]) -> list[SearchResult]:
        """Return reranked results."""
