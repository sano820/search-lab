"""Identity reranker."""

from __future__ import annotations

from common.types import SearchResult
from rankers.base import BaseRanker


class IdentityRanker(BaseRanker):
    """Return input results without modification."""

    def rerank(self, query: str, results: list[SearchResult]) -> list[SearchResult]:
        return results
