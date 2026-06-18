"""Fixed-size text chunker."""

from __future__ import annotations

from common.types import Chunk, ParsedDocument
from chunkers.base import BaseChunker


class FixedSizeChunker(BaseChunker):
    """Split text into character-based overlapping chunks."""

    def __init__(self, chunk_size: int = 800, overlap: int = 120) -> None:
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document: ParsedDocument) -> list[Chunk]:
        chunks: list[Chunk] = []
        step = self.chunk_size - self.overlap
        for idx, start in enumerate(range(0, len(document.text), step)):
            text = document.text[start : start + self.chunk_size]
            if text:
                chunks.append(Chunk(id=f"{document.id}::chunk-{idx:04d}", document_id=document.id, text=text, metadata={**document.metadata, "chunk_index": idx}))
        return chunks
