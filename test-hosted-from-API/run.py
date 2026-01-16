import persona as p
import chatbot as c

c.chat("Explain tokenization", persona="tutor")
c.chat("What is the capital of France", persona="tutor")
c.chat("My app crashes on login", persona="support")

for persona, msgs in c.conversations.items():
    print(f"\nPersona: {persona}")
    for m in msgs :
        print(f"{m['role']} : {m['content']}")