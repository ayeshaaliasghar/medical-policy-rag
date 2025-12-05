import pandas as pd
import jsonlines
import os

def chunk_text(text, size=300, overlap=150):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i+size])
        chunks.append(chunk)
        i += size - overlap
    return chunks

def preprocess(csv_path="data/mtsamples.csv",
               out_path="data/processed/medical_chunks.jsonl"):

    df = pd.read_csv(csv_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    all_chunks = []
    for idx, row in df.iterrows():
        text = row["transcription"]
        if isinstance(text, str) and text.strip():
            for i, ch in enumerate(chunk_text(text)):
                all_chunks.append({
                    "text": ch,
                    "source": f"mtsample_{idx}",
                    "chunk_id": i
                })

    with jsonlines.open(out_path, "w") as w:
        w.write_all(all_chunks)

    print(f"✔ Created {len(all_chunks)} chunks → {out_path}")

if __name__ == "__main__":
    preprocess()
