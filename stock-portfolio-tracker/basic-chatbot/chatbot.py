# Basic Chatbot - Python Mini Project
# A simple rule-based chatbot using if-elif, functions, loops and input/output.

# Words that end the conversation
exit_words = ["bye", "exit", "quit", "goodbye"]

# Greeting words
greetings = ["hello", "hi", "hey"]


def show_welcome():
    """Prints the welcome message."""
    print("=" * 45)
    print("WELCOME TO  Iccha's CHATBOT")
    print("=" * 45)
    print("Hello! I am Iccha chatBot, a simple chatbot.")
    print("Type 'bye', 'exit' or 'quit' to end the chat.")
    print("-" * 45)


def get_response(message):
    """Takes the user's message and returns a predefined reply."""
    if message == "":
        return "Please type something so I can reply."
    elif message in greetings:
        return "Hi!"
    elif "how are you" in message:
        return "I'm fine, thanks!"
    elif "your name" in message:
        return "My name is Iccha chatBot."
    elif "what can you do" in message:
        return "I can chat with you, greet you and answer a few simple questions."
    elif "what is python" in message:
        return "Python is a popular, easy-to-learn programming language."
    elif "your purpose" in message:
        return "My purpose is to show how a simple rule-based chatbot works."
    elif "thank" in message:
        return "You're welcome!"
    else:
        return "Sorry, I didn't understand that."


def chatbot():
    """Runs the chat loop until the user wants to quit."""
    show_welcome()

    while True:
        # lower() makes it case-insensitive, strip() removes spaces and ? ! . , at the ends
        user_message = input("You: ").lower().strip(" ?!.,")

        if user_message in exit_words:
            print("Iccha chatBot: Goodbye!")
            break

        reply = get_response(user_message)
        print("Iccha chatBot:", reply)


# Start the chatbot
chatbot()