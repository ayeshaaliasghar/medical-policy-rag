import jsonlines, os

INP = "data/processed/compliance_docs.jsonl"
OUT = "data/processed/compliance_chunks.jsonl"

def chunk_text(text, size=250, overlap=80):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i+size])
        chunks.append(chunk)
        i += size - overlap
    return chunks

items = []
with jsonlines.open(INP) as r:
    for doc in r:
        chunks = chunk_text(doc["text"])
        for i, c in enumerate(chunks):
            items.append({
                "text": c,
                "metadata": {"source": doc["id"], "chunk_id": i}
            })

with jsonlines.open(OUT, "w") as w:
    w.write_all(items)

print("Chunks saved:", len(items))
