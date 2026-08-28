# Rule-Based AI Chatbot

### Project 1 — DecodeLabs Industrial Training Kit | Batch 2026

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![AI Type](https://img.shields.io/badge/AI%20Type-Rule--Based-00C853?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-2ea44f?style=for-the-badge)

---

## Overview

This project is a Rule-Based AI Chatbot developed using Python as part of Project 1 of the DecodeLabs Industrial Training Kit, Batch 2026.

The chatbot uses predefined rules and `if-elif-else` decision-making to respond to user inputs. It runs continuously until the user chooses to exit.

The purpose of this project is to understand the fundamentals of control flow, decision-making, user interaction, and rule-based Artificial Intelligence systems.

---

## Project Goal

The goal of this project is to build a chatbot that simulates basic human conversation using predefined rules and responses.

The chatbot can:

* Handle greetings and casual conversation
* Respond to common questions
* Answer basic Artificial Intelligence questions
* Answer basic Python questions
* Provide the current time, date, and day
* Tell random jokes
* Respond to emotional and casual inputs
* Handle unknown inputs using fallback responses
* Exit the conversation using predefined commands

---

## Key Concepts

### Rule-Based AI

A rule-based system follows predefined instructions to make decisions.

The basic structure used in this project is:

```text
User Input
    |
    v
Input Sanitization
    |
    v
Rule Matching
    |
    v
if-elif-else Decision Making
    |
    v
Chatbot Response
```

Unlike Machine Learning systems, this chatbot does not learn from data. Every response is based on rules explicitly programmed by the developer.

---

## Features

### Greetings

The chatbot can respond to greetings such as:

```text
hello
hi
hey
good morning
good evening
```

---

### Natural Conversation

The chatbot supports common conversational inputs such as:

```text
what's up
how's it going
good
great
not good
i am fine
i am sad
i am bored
i am tired
okay
lol
haha
```

---

### Chatbot Information

Users can ask questions such as:

```text
who are you
what is your name
what can you do
```

---

### Artificial Intelligence Concepts

The chatbot can provide basic information about:

```text
Artificial Intelligence
Machine Learning
Deep Learning
Natural Language Processing
Rule-Based Chatbots
```

Example questions:

```text
what is ai
what is machine learning
what is deep learning
what is nlp
what is a rule based chatbot
```

---

### Python Concepts

The chatbot can answer basic Python-related questions about:

```text
Python
Lists
Dictionaries
Loops
Functions
```

Example questions:

```text
what is python
what is a list
what is a dictionary
what is a loop
what is a function
```

---

### Fun Features

The chatbot can also provide entertainment through:

* Random programming jokes
* Fun facts
* Motivational responses
* Compliments

Example:

```text
tell me a joke
tell me a fact
motivate me
compliment me
```

The chatbot uses Python's `random` module to provide different responses for the same type of question.

---

### Time and Date

The chatbot can display live system information.

Example questions:

```text
what time is it
what is the date
what day is it
```

The `datetime` module is used to retrieve the current time, date, and day.

---

### Input Sanitization

User input is cleaned before processing using:

```python
.lower().strip()
```

This allows the chatbot to handle different capitalization and unnecessary spaces.

For example:

```text
HELLO
Hello
hello
   hello
```

All of these inputs are processed consistently.

---

### Empty Input Handling

If the user presses Enter without entering any text, the chatbot asks the user to provide an input instead of producing an error.

---

### Fallback Response

If the chatbot does not recognize a user's input, it provides a fallback response.

For example:

```text
You: What is quantum computing?

ByteBot: I'm sorry, I don't understand that yet. Try typing 'help' to see what I can do.
```

This ensures that the chatbot can handle unknown inputs gracefully.

---

### Exit Commands

The chatbot can be closed using commands such as:

```text
exit
quit
bye
goodbye
```

---

## Technologies Used

| Technology   | Purpose                               |
| ------------ | ------------------------------------- |
| Python       | Core programming language             |
| random       | Generates varied responses            |
| datetime     | Provides current time and date        |
| if-elif-else | Implements rule-based decision making |
| while True   | Maintains continuous conversation     |

---

## Project Structure

```text
DecodeLabs-Internship-Project-1/
│
├── chatbot.py
└── README.md
```

### File Description

#### chatbot.py

Contains the main implementation of the Rule-Based AI Chatbot.

#### README.md

Provides complete documentation for the project.

---

## How It Works

The chatbot follows a continuous conversation loop.

```text
Start Chatbot
      |
      v
Display Welcome Message
      |
      v
Receive User Input
      |
      v
Clean Input
      |
      v
Is Input Empty?
   /          \
 Yes          No
  |            |
  v            v
Ask User    Check Exit
Again       Command
               |
               v
         Match Rules
               |
               v
       Generate Response
               |
               v
        Wait for Input
```

The chatbot continues running until the user enters an exit command.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/nidaarshad-arch/rule-based-ai-chatbot.git
```

### Move into the Project Directory

### Run the Chatbot

```bash
python chatbot.py
```

## Sample Conversation

```text
=================================================================
ByteBot - Rule-Based AI Chatbot
=================================================================

ByteBot: Hello! I am ByteBot, your rule-based AI assistant.
You can ask me about AI, Machine Learning, Python, or simply have
a conversation with me.

Type 'help' to see available topics.
Type 'exit' anytime to end the conversation.

You: hello

ByteBot: Hello! How can I help you today?

You: what is ai

ByteBot: Artificial Intelligence is a field of computer science
that enables machines to perform tasks that normally require
human intelligence.

You: tell me a joke

ByteBot: Why was the computer tired? It had too many tabs open!

You: what time is it

ByteBot: The current time is 08:50 PM.

You: i am bored

ByteBot: Let's fix that! Want a joke, a fun fact, or some motivation?

You: exit

ByteBot: Goodbye! Keep learning, keep building, and never stop exploring.
```

---

## Key Skills Demonstrated

This project demonstrates the following programming and Artificial Intelligence fundamentals:

* Control flow
* Conditional statements
* `if-elif-else` logic
* Loops
* Functions
* User input handling
* Input sanitization
* Python sets
* Lists
* Random response generation
* Date and time handling
* Rule-based decision making
* Basic conversational AI concepts

---

## Limitations

This chatbot is a deterministic, rule-based system. It can only respond to inputs and patterns that have been explicitly programmed.

Unlike Large Language Models or Machine Learning-based chatbots, ByteBot:

* Does not learn from conversations
* Does not understand complex context
* Cannot generate completely new answers
* Is limited to predefined rules and responses

These limitations are expected in a basic rule-based chatbot and help demonstrate the difference between traditional rule-based AI and modern learning-based AI systems.

---

## Future Improvements

Possible future improvements include:

* Keyword-based intent matching
* Dictionary-based response management
* Conversation history
* User name recognition
* Basic calculator functionality
* Weather API integration
* GUI using Tkinter
* Web interface using Flask or Streamlit
* Machine Learning-based intent classification
* Natural Language Processing integration

---

## Learning Outcomes

Through this project, I learned how to:

* Build a continuous interactive Python application
* Use `while True` loops effectively
* Apply `if-elif-else` decision-making
* Handle different types of user input
* Create predefined conversational responses
* Use the `random` module for response variety
* Use the `datetime` module for dynamic information
* Implement fallback handling
* Understand the fundamentals of rule-based Artificial Intelligence

---

## Author

**Nida Arshad**

BS Information Technology Student
AI Engineering Intern

---

## About the Project

This project was developed as part of the DecodeLabs Industrial Training Kit, Batch 2026.

Project 1 focuses on building a Rule-Based AI Chatbot using control flow and decision-making logic as a foundation for understanding Artificial Intelligence concepts.

---

## License

This project is created for educational and internship purposes.
