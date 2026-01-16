import router as rt
import persona as ps
import llm as llm

conversations = {"tutor": [], "support": [], "other": []}

global_conversation = []

MAX_MEMORY = 6

def chat(user_input, persona=None):

    if persona is None:
        persona = rt.route_persona(user_input)    

    if persona not in conversations:
        raise ValueError(f"Unknown persona: {persona}")
    
    user_msg = {
        "role": "user",
        "persona": persona,
        "content": user_input
    }

    conversations[persona].append(user_msg)
    global_conversation.append(user_msg)

    messages = [
        ps.personas[persona],
        *conversations[persona]
    ]

    response = llm.fake_llm(messages, persona)

    assistant_msg = {
        "role": "assistant",
        "persona": persona,
        "content": response
    }

    conversations[persona].append(assistant_msg)
    global_conversation.append(assistant_msg)

    conversations[persona] = conversations[persona][-MAX_MEMORY:]

    return response

def reset_conversation():
    for persona in conversations:
        conversations[persona].clear()