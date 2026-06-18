# search-lab

검색 및 정보 검색 파이프라인 구현을 위한 모듈형 코드 저장소입니다.

## 목적

`search-lab`은 문서/웹/API/DB 등 다양한 소스에서 데이터를 수집하고,
파싱·정제·청킹·임베딩·색인·검색·랭킹·평가까지 이어지는 검색 파이프라인을
실험하기 위한 저장소입니다.

## 디렉터리 구조

```text
search-lab/
├── loaders/          # 파일/API/DB 로딩
├── crawlers/         # 웹 수집
├── parsers/          # PDF, HWP, DOCX 등 문서 파싱
├── preprocessors/    # 텍스트 정제 및 표준화
├── chunkers/         # 문서 청킹
├── embedders/        # 임베딩 생성
├── indexers/         # Elasticsearch, FAISS, Milvus 등 색인
├── retrievers/       # BM25, Dense Retrieval 등 검색
├── rankers/          # Reranker
├── evaluators/       # 검색 성능 평가
├── common/           # 공통 타입, 설정, 유틸
├── examples/         # 사용 예제
└── tests/            # 테스트 코드
```

## 기본 파이프라인

```text
load → crawl/parse → preprocess → chunk → embed → index → retrieve → rerank → evaluate
```

## 빠른 시작

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
python examples/basic_pipeline.py
```
