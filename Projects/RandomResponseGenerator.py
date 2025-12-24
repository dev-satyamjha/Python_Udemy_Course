import json
import random

BASE_RESPONSES = [
    ("Hello!", ["hello", "hi", "hey", "sup", "heyo"], []),
    ("See you!", ["bye", "goodbye", "later", "cya"], []),
    ("I'm doing fine, and you?", ["how", "are", "you", "doing"], ["how"]),
    ("You're welcome!", ["thank", "thanks", "thx"], []),
    ("Same!", ["i", "love", "coding"], ["love", "coding"]),
    ("Good morning!", ["good", "morning"], ["morning"]),
    ("Good night!", ["good", "night"], ["night"]),
    ("Nice to meet you!", ["nice", "meet", "you"], ["meet"]),
    ("Absolutely!", ["yes", "sure", "absolutely"], []),
    ("I don’t think so.", ["no", "not", "really"], [])
]

def generate_responses(n: int = 100000): #You can set your response generation limit here
    responses = []

    for i in range(n):
        text, words, required = random.choice(BASE_RESPONSES)

        responses.append({
            "response": f"{text}",
            "words": random.sample(words, k=random.randint(1, len(words))),
            "required_words": random.sample(required, k=random.randint(0, len(required)))
        })

    return responses


if __name__ == "__main__":
    data = generate_responses()

    with open("responses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Generated 100000 responses → responses.json")
