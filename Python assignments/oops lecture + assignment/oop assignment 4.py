class Smart_bot:
    def __init__(self, name, mood):
        self.name = name
        self.mood = mood

    def speak(self):
        print(f"Welcome {self.name}😊")

bot_name1 = Smart_bot("Alexa", "happy")
bot_name2 = Smart_bot("Siri", "happy")

bot_name1.speak()
bot_name2.speak()
