"""Crawler interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import RawDocument


class BaseCrawler(ABC):
    """Collect web resources and return raw documents."""

    @abstractmethod
    def crawl(self, url: str) -> list[RawDocument]:
        """Crawl URL and return raw documents."""
