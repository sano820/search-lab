"""Minimal end-to-end search pipeline example."""

from __future__ import annotations

from chunkers.fixed_size_chunker import FixedSizeChunker
from common.types import RawDocument
from embedders.dummy_embedder import DummyEmbedder
from evaluators.simple_evaluator import SimpleEvaluator
from indexers.in_memory_indexer import InMemoryIndexer
from parsers.plain_text_parser import PlainTextParser
from preprocessors.basic_cleaner import BasicCleaner
from rankers.identity_ranker import IdentityRanker
from retrievers.keyword_retriever import KeywordRetriever


def main() -> None:
    raw_documents = [
        RawDocument(id="doc-001", source="inline", content="검색 파이프라인은 로딩, 파싱, 전처리, 청킹, 색인, 검색 단계로 구성됩니다."),
        RawDocument(id="doc-002", source="inline", content="Dense retrieval은 임베딩 벡터를 사용하고, BM25는 키워드 기반 검색입니다."),
    ]

    parser = PlainTextParser()
    cleaner = BasicCleaner()
    chunker = FixedSizeChunker(chunk_size=80, overlap=10)
    embedder = DummyEmbedder()
    indexer = InMemoryIndexer()

    chunks = []
    for raw_document in raw_documents:
        parsed = parser.parse(raw_document)
        cleaned = cleaner.process(parsed)
        chunks.extend(chunker.chunk(cleaned))

    vectors = embedder.embed(chunks)
    indexer.add(chunks, vectors)

    retriever = KeywordRetriever(indexer)
    ranker = IdentityRanker()
    evaluator = SimpleEvaluator()

    query = "검색 파이프라인"
    results = ranker.rerank(query, retriever.search(query, top_k=5))

    print("Results:")
    for result in results:
        print(f"- {result.id} | score={result.score} | {result.text}")

    print("Metrics:", evaluator.evaluate(query, results))


if __name__ == "__main__":
    main()
