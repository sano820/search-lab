"""Common data types for the search pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class RawDocument:
    """Raw loaded or crawled document."""

    id: str
    source: str
    content: bytes | str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ParsedDocument:
    """Parsed text document."""

    id: str
    source: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Chunk:
    """Chunked text unit used for embedding and indexing."""

    id: str
    document_id: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SearchResult:
    """Search result returned by retrievers or rankers."""

    id: str
    text: str
    score: float
    metadata: dict[str, Any] = field(default_factory=dict)
