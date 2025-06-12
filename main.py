import json
import random

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)

def get_response(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "I'm not sure how to respond to that."

# Chat loop
print("🤖 Chatbot: Hello! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("🤖 Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("🤖 Chatbot:", response)
