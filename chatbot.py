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
        if user_input in {"exit","quit","bye","goodbye","ok bye","ok goodbye","okay bye","okay goodbye"}:
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

        elif user_input in {"how are you", "how are you?", "how r you","how are u","how are u?","how r u","how r u?"}:
            response = random.choice([
                "I'm doing great! Thanks for asking. ",
                "I'm functioning perfectly and ready to help!",
                "I'm great! How about you?"
                ])
            print(f"{BOT_name}: {response}")
        elif user_input in {"thank you", "thanks", "thankyou"}:
            response = random.choice([
                "You're welcome! 😊",
                "Happy to help!",
                "Anytime! Feel free to ask me more questions."
                ])
            print(f"{BOT_name}: {response}")
        elif user_input in {"what is your name", "who are you", "tell me your name","Tell me about yourself","tell me about you"}:
            print(
                f"{BOT_name}: My name is {BOT_name}! "
                "I'm a rule-based AI chatbot built using Python."
                )
        elif user_input in {"i am fine", "i'm fine", "im fine", "fine","I'm great","good","i am good","im good","great"}:
            print(f"{BOT_NAME}: That's great to hear! 😊")
        elif user_input == "help":
            print(f"""{BOT_name}: Here are some things you can ask me
            • Greetings: hello, hi, hey
            • Small talk: how are you
            • About me: who are you, what is your name
            • AI topics: what is AI, machine learning
            • Python topics: what is Python
            • Fun: tell me a joke
            • Time and date: what time is it, what is the date
            • Exit: exit, quit, bye
            """)
        

if __name__ == "__main__":
    run_chatbot()