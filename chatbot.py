import random
from datetime import datetime

BOT_name='ByteBot'

def display_welcome():
    print("="*65)
    print(f"{BOT_name} - Rule-Based AI Chatbot")
    print("="*65)
    print(f"\n{BOT_name}:Hello! I am {BOT_name}","your rule-based AI assistant.")
    print("You can ask me about AI, Machine Learning, Python, or simply have a small" \
    "conversation with me.")
    print("\n Type 'help' to see available topics.")
    print("Type 'exit' anytime to end the conversation.\n")



def run_chatbot():
    display_welcome()
    while True:
        user_input=input("You: ").lower().strip()
        if not user_input:
            print(f"{BOT_name}: Please type something so I can help you.")
            continue
        if user_input in {"exit","quit","bye","goodbye"}:
            print(f"{BOT_name}: Goodbye! Keep learning, keep building, and never stop exploring.")
            break
        if user_input in {"hello", "hi", "hey", "good morning", "good evening"}:
            response = random.choice([
                "Hello! How can I help you today?",
                "Hi there! Nice to talk with you.",
                "Hey! What would you like to know?",
                "Hello! I'm happy to assist you."
                ])
            print(f"{BOT_name}: {response}")
        

if __name__ == "__main__":
    run_chatbot()