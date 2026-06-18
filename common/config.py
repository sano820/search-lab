"""Project configuration helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SearchLabConfig:
    """Runtime configuration for search-lab experiments."""

    embedding_model: str = "local"
    chunk_size: int = 800
    chunk_overlap: int = 120
    top_k: int = 10
