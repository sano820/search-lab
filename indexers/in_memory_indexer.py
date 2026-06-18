"""In-memory index for quick experiments."""

from __future__ import annotations

from common.types import Chunk, SearchResult
from indexers.base import BaseIndexer


class InMemoryIndexer(BaseIndexer):
    """Store chunks in memory and perform simple keyword search."""

    def __init__(self) -> None:
        self.chunks: list[Chunk] = []
        self.vectors: list[list[float]] | None = None

    def add(self, chunks: list[Chunk], vectors: list[list[float]] | None = None) -> None:
        self.chunks.extend(chunks)
        if vectors is not None:
            self.vectors = list(vectors)

    def keyword_search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        terms = query.lower().split()
        scored: list[SearchResult] = []
        for chunk in self.chunks:
            text = chunk.text.lower()
            score = sum(text.count(term) for term in terms)
            if score > 0:
                scored.append(SearchResult(id=chunk.id, text=chunk.text, score=float(score), metadata=chunk.metadata))
        return sorted(scored, key=lambda item: item.score, reverse=True)[:top_k]
