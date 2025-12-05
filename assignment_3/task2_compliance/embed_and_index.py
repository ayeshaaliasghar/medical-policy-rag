import jsonlines, os
from sentence_transformers import SentenceTransformer
from langchain.schema import Document
from langchain_community.vectorstores import FAISS

INP = "data/processed/compliance_chunks.jsonl"
OUT = "data/index"

os.makedirs(OUT, exist_ok=True)

embedder = SentenceTransformer("all-MiniLM-L6-v2")

class EMBS:
    def embed_documents(self, docs):
        return embedder.encode(docs, convert_to_numpy=True).tolist()
    def embed_query(self, q):
        return embedder.encode([q], convert_to_numpy=True)[0].tolist()

emb = EMBS()

items = list(jsonlines.open(INP))

docs = [Document(page_content=i["text"], metadata=i["metadata"]) for i in items]

db = FAISS.from_documents(docs, emb)
db.save_local(OUT)

print("FAISS index saved to", OUT)
