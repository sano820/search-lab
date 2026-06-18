"""Plain text parser."""

from __future__ import annotations

from common.types import ParsedDocument, RawDocument
from parsers.base import BaseParser


class PlainTextParser(BaseParser):
    """Parse raw text-like documents."""

    def parse(self, document: RawDocument) -> ParsedDocument:
        text = document.content.decode("utf-8", errors="replace") if isinstance(document.content, bytes) else document.content
        return ParsedDocument(id=document.id, source=document.source, text=text, metadata=document.metadata)
