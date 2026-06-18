"""Loader interfaces."""

from __future__ import annotations

from abc import ABC, abstractmethod
from common.types import RawDocument


class BaseLoader(ABC):
    """Load raw documents from files, APIs, databases, or other sources."""

    @abstractmethod
    def load(self) -> list[RawDocument]:
        """Return raw documents."""
