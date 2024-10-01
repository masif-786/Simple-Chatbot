import random

class ImprovedChatbot:
    def __init__(self):
        self.user_name = None
        self.user_hobby = None
        self.responses = {
            "greeting": ["Hi there!", "Hello!", "Hey!", "Greetings!"],
            "name": ["Nice to meet you, %1!", "Glad to know you, %1!"],
            "hobby": ["That's interesting! I like that too.", "Wow, %1 sounds fun!"],
            "how_are_you": ["I'm just a bunch of code, but I'm doing great! How about you?", 
                             "Feeling good! What about you?"],
            "farewell": ["Goodbye! Have a great day!", "See you later!"],
            "fallback": ["I'm not sure I understand.", "Can you say that differently?"]
        }

    def get_response(self, input_text):
        input_text = input_text.lower()
        
        if "hi" in input_text or "hello" in input_text or "hey" in input_text:
            return random.choice(self.responses["greeting"])
        elif "my name is" in input_text:
            self.user_name = input_text.split("my name is ")[1]
            return random.choice(self.responses["name"]).replace("%1", self.user_name)
        elif "i like" in input_text or "my hobby is" in input_text:
            self.user_hobby = input_text.split("i like ")[1] if "i like" in input_text else input_text.split("my hobby is ")[1]
            return random.choice(self.responses["hobby"]).replace("%1", self.user_hobby)
        elif "how are you" in input_text or "how's it going" in input_text:
            return random.choice(self.responses["how_are_you"])
        elif "quit" in input_text or "bye" in input_text:
            return random.choice(self.responses["farewell"])
        else:
            return random.choice(self.responses["fallback"])

    def start_chat(self):
        print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print(f"ChatBot: {response}")
            if response in self.responses["farewell"]:
                break

if __name__ == "__main__":
    chatbot = ImprovedChatbot()
    chatbot.start_chat()
