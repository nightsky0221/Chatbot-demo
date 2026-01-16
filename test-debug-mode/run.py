import chatbot as c


#     response = "Placeholder response from LLM"

#     assis_msg = {
#         "role": "assistant",
#         "content": response
#     }

#     conversation.append(assis_msg)

#     conversation = conversation[-MAX_MEMORY:]

#     return response

# def reset_conversation():
#     global conversation
#     conversation = []

c.chat("Explain tokenization", persona="tutor")
c.chat("What is the capital of France", persona="tutor")