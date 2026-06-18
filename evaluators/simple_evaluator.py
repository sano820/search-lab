"""Simple search evaluator."""

from __future__ import annotations

from common.types import SearchResult
from evaluators.base import BaseEvaluator


class SimpleEvaluator(BaseEvaluator):
    """Return basic count-based metrics."""

    def evaluate(self, query: str, results: list[SearchResult]) -> dict[str, float]:
        return {"result_count": float(len(results)), "max_score": max((r.score for r in results), default=0.0)}
