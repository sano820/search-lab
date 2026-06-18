"""Basic text cleaning utilities."""

from __future__ import annotations

import re
from common.types import ParsedDocument
from preprocessors.base import BasePreprocessor


class BasicCleaner(BasePreprocessor):
    """Normalize whitespace and remove empty lines."""

    def process(self, document: ParsedDocument) -> ParsedDocument:
        text = document.text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"[ \t]+", " ", text)
        text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
        return ParsedDocument(id=document.id, source=document.source, text=text, metadata=document.metadata)
