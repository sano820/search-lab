# search-lab
검색 및 정보 검색 파이프라인 구현을 위한 모듈형 코드 저장소 (크롤링, 파싱, 전처리, 벡터 색인, 검색)


```
search-lab/
├── loaders/          # 파일/API/DB 로딩
├── crawlers/         # 웹 수집
├── parsers/          # PDF, HWP, DOCX ...
├── preprocessors/    # 정제
├── chunkers/         # 청킹
├── embedders/        # 임베딩 생성
├── indexers/         # ES, FAISS, Milvus
├── retrievers/       # BM25, Dense Retrieval
├── rankers/          # Reranker
├── evaluators/       # 검색 성능 평가
├── common/
└── examples/
```
