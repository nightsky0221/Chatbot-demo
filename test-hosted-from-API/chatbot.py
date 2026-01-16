import persona as p
import host

conversations = {"tutor": [], "support": []}

MAX_MEMORY = 6

def chat(user_input, persona="tutor"):
    
    global conversations

    user_msg = {
        "role": "user",
        "persona": persona,
        "content": user_input
    }

    conversations[persona].append(user_msg)

    messages = [
        p.personas[persona],
        *[
            {"role": m["role"], "content": m["content"]}
            for m in conversations[persona]
        ]

        # *conversations[persona]
    ]

    response = host.ollama_llm_call(messages)

    assistant_msg = {
        "role": "assistant",
        "persona": persona,
        "content": response
    }

    conversations[persona].append(assistant_msg)

    conversations[persona] = conversations[persona][-MAX_MEMORY:]

    return response

def reset_conversation():
    for persona in conversations:
        conversations[persona].clear()