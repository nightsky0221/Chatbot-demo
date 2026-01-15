import re

text = """
Header : AI Report 2025

This is the first paragraph.

This is the second paragraph with        extra spaces.
"""

def regula_text(text):
    # seperate_words = re.findall(r"\w+", text)
    text = re.sub(r"[^a-zA-Z0-9\n\s\.\:]", "", text)
    text = re.sub(r"[ \t]+", " ", text) # keep paragraphs removing spaces in one line
    text = re.sub(r"\n+", "\n", text)
    return text.strip()

a = regula_text(text)
print(a)

paragraphs = [p for p in text.split("\n") if p.strip() != ""]
length = len(paragraphs)
print("paragraph count : ", length)