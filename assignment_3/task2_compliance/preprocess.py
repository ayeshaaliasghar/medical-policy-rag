from pypdf import PdfReader
import jsonlines, os

os.makedirs("data/processed", exist_ok=True)

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

pdf_folder = "data/pdfs"
output = "data/processed/compliance_docs.jsonl"

docs = []
for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        full_path = os.path.join(pdf_folder, file)
        txt = extract_text_from_pdf(full_path)
        docs.append({"id": file, "text": txt})

with jsonlines.open(output, "w") as w:
    w.write_all(docs)

print("Extracted", len(docs), "PDF documents.")
