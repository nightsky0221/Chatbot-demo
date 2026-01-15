from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# text = "AI is changing the world we work"
text = [
    "AI is amazing, it changes all those thing we are doing now. It affects heavily our life and the world we live in now is developing by AI power, so I think we should improve our AI skill by the trend, everything only works when it is curratable.",
    "Artificial Intelligence is great, it is really perfect now.",
    "AI is good, 🤖"
]

for t in text:
    print(tokenizer(t))
    print(t, "->", len(tokenizer(t)["input_ids"]))
# tokens = tokenizer(text)

# print(tokens)
# print("token counts:", len(tokens["input_ids"]))