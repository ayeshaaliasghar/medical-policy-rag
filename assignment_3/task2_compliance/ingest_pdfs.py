from pypdf import PdfReader
import jsonlines, os

PDF_DIR = "data/pdfs"
OUT_PATH = "data/processed/compliance_docs.jsonl"

os.makedirs("data/processed", exist_ok=True)

def extract_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n"
    return text

docs = []
for fname in os.listdir(PDF_DIR):
    if fname.endswith(".pdf"):
        fpath = os.path.join(PDF_DIR, fname)
        docs.append({
            "id": fname,
            "text": extract_text(fpath)
        })

with jsonlines.open(OUT_PATH, "w") as w:
    w.write_all(docs)

print("Extracted", len(docs), "documents into", OUT_PATH)
