responses={
    "courses" : "we offer python, Ai  and web development.",
    "fee" : "the course fee is rs. 15000",
    "duration" : "Course duration is 3 month.",
    "locaton"  : "brain college Lahore",
    "contact"  : "call us at ......",
    "hi"  :  "Hello, im chatbot how can i help you"
}

print("brain collage chatbot")
print("ask about course, fee, duration, location")
print("type exist to quit")

while True:
    user = input("you : ").lower()

    if user== "exist" :
        print("Bot : thank you for visiting.")
        break
    elif user in responses:
        print("bot : ", responses[user])

    else:
        print("bot : please ask about course , fee, duration, or location.")
