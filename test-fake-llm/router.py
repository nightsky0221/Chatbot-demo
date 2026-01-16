def route_persona(user_input):

    text = user_input.lower()

    support_keywords = [
        "crash", "error", "bug", "login", "issue", "problem", "doesn't work", "failed", "help", "support"
    ]

    tutor_keywords = [
        "explain", "what is", "how does", "token", "embedding", "llm", "nlp", "transformer", "attention", "model"
    ]

    if any(k in text for k in support_keywords):
        return "support"
    elif any(k in text for k in tutor_keywords):
        return "tutor"
    else:
        return "other"
