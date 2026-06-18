"""Smoke tests for search-lab."""

from chunkers.fixed_size_chunker import FixedSizeChunker
from common.types import ParsedDocument


def test_fixed_size_chunker_creates_chunks() -> None:
    document = ParsedDocument(id="doc", source="test", text="검색 파이프라인 테스트 문서입니다." * 20)
    chunker = FixedSizeChunker(chunk_size=50, overlap=10)
    chunks = chunker.chunk(document)

    assert chunks
    assert chunks[0].document_id == "doc"
