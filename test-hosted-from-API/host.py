import os
from huggingface_hub import InferenceClient
import ollama
from openai import OpenAI

# This is huggingface host

hf_client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("HF_TOKEN")
)

def Hugging_Face_llm_call(messages):
    user_content = messages[-1]["content"]
    prompt = f"<s>[INST] {user_content} [/INST]"
    return hf_client.text_generation(prompt, max_new_tokens=300)

# This is ollama host

def ollama_llm_call(messages):
    response = ollama.chat(
        model = "llama3",
        messages=messages
    )
    return response["message"]["content"]

# This is OpenAI host

openai_client = OpenAI(api_key="YOUR_API_KEY")

def OpenAI_llm_call(messages):
    response = openai_client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=messages,
        temperature=0.3
    )
    return response.choices[0].message.content