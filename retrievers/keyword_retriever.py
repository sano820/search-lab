"""Simple keyword retriever."""

from __future__ import annotations

from common.types import SearchResult
from indexers.in_memory_indexer import InMemoryIndexer
from retrievers.base import BaseRetriever


class KeywordRetriever(BaseRetriever):
    """Retrieve candidates using in-memory keyword matching."""

    def __init__(self, index: InMemoryIndexer) -> None:
        self.index = index

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        return self.index.keyword_search(query=query, top_k=top_k)
