from sentence_transformers import SentenceTransformer
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
import jsonlines, os

st = SentenceTransformer("all-MiniLM-L6-v2")

class STEmb:
    def embed_documents(self, docs):
        return st.encode(docs, convert_to_numpy=True).tolist()
    def embed_query(self, q):
        return st.encode([q], convert_to_numpy=True)[0].tolist()

emb = STEmb()

items = []
with jsonlines.open("data/processed/compliance_chunks.jsonl") as r:
    items = list(r)

texts = [x["text"] for x in items]
metas = [x["metadata"] for x in items]

docs = [Document(page_content=t, metadata=m) for t,m in zip(texts, metas)]

db = FAISS.from_documents(docs, emb)
db.save_local("data/index")

print("FAISS index saved.")
