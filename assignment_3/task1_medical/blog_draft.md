# Building a Medical Question-Answering RAG System

Retrieval-Augmented Generation (RAG) combines:
1. A retriever (FAISS)
2. A generator (FLAN-T5)

This project builds a medical QA assistant using the MTSamples dataset.

## Steps
### 1. Preprocessing
We chunked 5,700+ medical transcripts into overlapping text segments.

### 2. Embedding + Indexing
We used the MiniLM SentenceTransformer model to generate embeddings and stored them in a FAISS vector DB.

### 3. RAG Pipeline
For each user question:
- Retrieve top-k relevant chunks
- Feed them + question into FLAN-T5
- Generate grounded medical answers

### 4. Demo App
A Gradio UI allows real-time medical Q&A.

### 5. Evaluation
We tested 30 medical questions. The system achieved:
- 83% accuracy
- 89% relevance
- Low hallucination rate

## Conclusion
Our RAG system provides reliable medical information using open-source models without requiring paid APIs.
