"""Evaluator interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import SearchResult


class BaseEvaluator(ABC):
    """Evaluate search quality."""

    @abstractmethod
    def evaluate(self, query: str, results: list[SearchResult]) -> dict[str, float]:
        """Return evaluation metrics."""
