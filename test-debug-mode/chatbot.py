import persona as ps

conversation = []

MAX_MEMORY = 6

def chat(user_input, persona="tutor"):

    global conversation
  
    user_msg = {
        "role": "user",
        "content": user_input
    }

    conversation.append(user_msg)

    messages = [
        ps.personas[persona],
        *conversation
    ]

    print("\n--- PROMPT SENT TO LLM ---\n")
    for m in messages:
        print(f"{m['role'].upper()}: {m['content']}")

    print("--- END PROMPT ---\n")
