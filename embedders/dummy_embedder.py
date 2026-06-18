"""Dummy embedder for local tests."""

from __future__ import annotations

import hashlib
import random
from common.types import Chunk
from embedders.base import BaseEmbedder


class DummyEmbedder(BaseEmbedder):
    """Generate deterministic pseudo vectors without external APIs."""

    def __init__(self, dim: int = 16) -> None:
        self.dim = dim

    def embed(self, chunks: list[Chunk]) -> list[list[float]]:
        vectors: list[list[float]] = []
        for chunk in chunks:
            seed = int(hashlib.sha256(chunk.text.encode("utf-8")).hexdigest(), 16)
            rng = random.Random(seed)
            vectors.append([rng.random() for _ in range(self.dim)])
        return vectors
