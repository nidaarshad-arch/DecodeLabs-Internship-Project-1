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
        elif user_input in {"what is your name", "who are you", "tell me your name", "tell me about yourself", "tell me about you"}:
            print(
                f"{BOT_name}: My name is {BOT_name}! "
                "I'm a rule-based AI chatbot built using Python."
                )
        elif user_input in {"i am fine", "i'm fine", "im fine", "fine","I'm great","good","i am good","im good","great"}:
            print(f"{BOT_name}: That's great to hear! 😊")
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
        elif user_input in {
            "what is ai",
            "what is artificial intelligence",
            "define ai",
            "define artificial intelligence",
            "tell me about ai",
            "tell me about artificial intelligence"
                }:
            print(
            f"{BOT_name}: Artificial Intelligence (AI) is a field of "
            "computer science that enables machines to perform tasks that "
            "normally require human intelligence."
            )
        elif user_input in {
            "what is machine learning",
            "define machine learning",
            "what is ml",
            "tell me about machine learning",
            "tell me about ml"
            }:
            print(
            f"{BOT_name}: Machine Learning (ML) is a branch of AI that "
            "allows computers to lear   n patterns from data and make "
            "predictions or decisions."
            )
        elif user_input in {
            "what is deep learning",
            "define deep learning",
            "tell me about deep learning"
            }:
            print(
                f"{BOT_name}: Deep Learning is a subset of Machine Learning "
                "that uses artificial neural networks with multiple layers "
                "to learn complex patterns from data."
            )
        elif user_input in {
            "what is nlp",
            "define nlp",
            "what is natural language processing",
            "tell me about nlp",
            "tell me about natural language processing"
            }:
            print(
                f"{BOT_name}: Natural Language Processing (NLP) is a field "
                "of AI that helps computers understand, process, and generate "
                "human language."
                )
        elif user_input in {
            "what is a rule based chatbot",
            "what is rule based chatbot",
            "define rule based chatbot"
            }:
            print(
                f"{BOT_name}: A rule-based chatbot responds to users using "
                "predefined rules, conditions, and programmed responses. "
                "It does not learn from data like a Machine Learning model."
                )
        elif user_input in {
            "what is python",
            "define python",
            "tell me about python"
            }:
            print(
                f"{BOT_name}: Python is a high-level, easy-to-read programming "
                "language. It is widely used in web development, data science, "
                "Artificial Intelligence, automation, and many other fields."
                )
        elif user_input in {
            "what is a list",
            "define list",
            "what is list",
            "tell me about list",
            "tell me about list in python"
            }:
            print(
                f"{BOT_name}: A list is a Python data structure used to store "
                "multiple items in a single variable. Lists are ordered and "
                "can be modified."
                )
        elif user_input in {
            "what is a dictionary",
            "define dictionary",
            "what is dictionary",
            "tell me about dictionary",
            "tell me about dictionary in python"
            }:
            print(
            f"{BOT_name}: A dictionary is a Python data structure that "
            "stores data in key-value pairs."
            )
        elif user_input in {
            "what is a loop",
            "define loop",
            "what is loop",
            "tell me about loop",
            "tell me about loop in python"
            }:
            print(
                f"{BOT_name}: A loop is used to repeat a block of code. "
                "Python mainly uses for loops and while loops."
            )
        elif user_input in {
            "what is a function",
            "define function",
            "what is function",
            "tell me about function",
            "tell me about fucntion in python"
            }:
            print(
                f"{BOT_name}: A function is a reusable block of code designed "
                "to perform a specific task."
                )
        elif user_input in {
            "tell me a joke",
            "tell a joke",
            "joke",
            "make me laugh"
            }:
            response = random.choice([
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
                "Why did the Python programmer wear glasses? Because they couldn't C! 🤓",
                "There are 10 types of people in the world: those who understand binary and those who don't! 😂"
                ])

            print(f"{BOT_name}: {response}")
        
        

if __name__ == "__main__":
    run_chatbot()