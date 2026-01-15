import re
from transformers import AutoTokenizer
from pypdf import PdfReader
from docx import Document

# This is the data cleaning part
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s\.\,\-]", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"\-+", "-", text)
    text = re.sub(r"\,+", ",", text)
    text = re.sub(r"\.+", ".", text)
    
    return text.strip()

# This is the data tokenization part
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def chunks_set(text, max_token_chunks=128):
    tokens = tokenizer(text, add_special_tokens=False)["input_ids"]
    chunks = []

    for i in range(0, len(tokens), max_token_chunks):
        chunk_token = tokens[i:i + max_token_chunks]
        chunk_text = tokenizer.decode(chunk_token, skip_special_tokens=True)
        chunks.append(chunk_text)
    
    return chunks

# This is the function to load a text file

def load_txt_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# This is the function to load a pdf file

def load_pdf_file(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

# This is the function to load doc files

def load_docx_file(file_path):
    doc = Document(file_path)
    text = ""

    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            text += paragraph.text + "\n"
        
    return text

# This is the selection part for the loading file type

file_path = r"D:\MyWork\Self study\2MonthsCourse\Week1\Day-2\1.txt"

if file_path.endswith(".pdf"):
    text = load_pdf_file(file_path)
elif file_path.endswith(".txt"):
    text = load_txt_file(file_path)
elif file_path.endswith(".docx"):
    text = load_docx_file(file_path)
elif file_path.endswith(".doc"):
    text = load_docx_file(file_path)
else:
    raise ValueError("Unsupported file type")

cleaned_text = clean_text(text)
chunks = chunks_set(cleaned_text, max_token_chunks=50)

print(cleaned_text[:500])
print("Number of chunks : ", len(chunks))
print("First chunk : ", chunks[0])