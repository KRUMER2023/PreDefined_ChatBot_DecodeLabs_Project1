import os
import json

class PredefinedChatBot:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(dir_path, "predefined_responses.json")

        try:
            with open(json_path, "r", encoding="utf-8") as file:
                self.predefined_responses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.predefined_responses = {
                "hi": "How can I help you?",
                "hello": "Hello! How can I help you today?",
                "hey": "Hey there! How can I help you?",
                "good morning": "A very good morning to you sir, how can I help you?",
                "good afternoon": "Good afternoon! How can I help you?",
                "good evening": "Good evening! How can I help you?",
                "how are you": "I'm doing great, thank you! How can I help you?"
            }

    def get_help(self):
        print("==========================================================================")
        print("       This is a Predefined ChatBot.")
        print("       It Only Understand the Following Commands:\n")

        for k, v in self.predefined_responses.items():
            print(f"{k}{" "*(33-len(k))} : {v}")
        
        print("\n      You Can Continue using Chat Bot Using Above Commands.")
        print("      OR Can Exit by : 'quit' / 'exit' / 'bye' / 'goodbye' .")
        print("==========================================================================\n")

    def get_response(self, user_input):
        cleaned_inp = user_input.strip().lower().rstrip("?.!")
        if cleaned_inp == "help":
            return "help"
        return self.predefined_responses.get(cleaned_inp, "I'm sorry, I don't understand that command. Try saying 'help' for a list of things I can do.")

    def say_bye(self):
        print(
            """
            ========================================================
              Thank You For using the Chat Bot, Bye, See you Again    
            ========================================================    
            """
        )

    def run(self):
        Stopper = {"exit", "quit", "bye", "goodbye"}
        
        print("     ==========================================================================")
        print("           I'm a Predefined ChatBot! How can I assist you today?")
        print("     ==========================================================================\n")

        while True:
            inp = input("===> Ask ChatBot : ")
            cleaned_inp = inp.strip().lower().rstrip("?.!")
            
            if cleaned_inp in Stopper:
                break
            
            response = self.get_response(inp)
            
            if response == "help":
                self.get_help()
                continue

            print("==========================================================================\n")
            print("User Said :")
            print(inp)
            print("\nResponse:")
            print(response + "\n")
            print("==========================================================================")

        self.say_bye()

if __name__ == "__main__":
    Chatbot = PredefinedChatBot()
    try:
        print("Connecting to Chatbot..........\n")
        Chatbot.run()
    except Exception as e:
        print("Something went Wrong...... ChatBot Not Available for now")
        print(e)