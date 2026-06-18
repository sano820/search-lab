"""Simple text file loader."""

from __future__ import annotations

from pathlib import Path
from common.types import RawDocument
from loaders.base import BaseLoader


class TextFileLoader(BaseLoader):
    """Load `.txt` files from a directory."""

    def __init__(self, directory: str | Path, pattern: str = "*.txt") -> None:
        self.directory = Path(directory)
        self.pattern = pattern

    def load(self) -> list[RawDocument]:
        documents: list[RawDocument] = []
        for path in sorted(self.directory.glob(self.pattern)):
            documents.append(
                RawDocument(
                    id=path.stem,
                    source=str(path),
                    content=path.read_text(encoding="utf-8"),
                    metadata={"filename": path.name},
                )
            )
        return documents
