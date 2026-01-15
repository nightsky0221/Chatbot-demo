from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def chunk_by_token(text, max_tokens=128):
    tokens = tokenizer(text, return_tensors=None)["input_ids"]
    chunks = []

    for i in range(0, len(tokens), max_tokens):
        chunks_token = tokens[i:i + max_tokens]
        chunks_text = tokenizer.decode(chunks_token)
        chunks.append(chunks_text)

    return chunks

sample_text = " ".join(["AI is great and I will use it in my work and life."] * 200)
chunks = chunk_by_token(sample_text, max_tokens=30)

print("Number of Chunks : ", len(chunks))
print(chunks[0])