import random as r

print("Welcome! I’m your chatbot")
while True:
    a = input("You: ")
    b = a.lower()
    print("ChatBot:" , end=" ")
    if b in ["exit" , "bye" , "goodbye" , "ok bye" , "bye chatbot"]:
        print(r.choice(["Goodbye! Have a great day." , "See you later!" , "Exiting the chat, take care!"]))
        break
    else:
        if b in ["hi" , "hello" , "hey" , "hi there"]:
            print(r.choice(["Hello User! How can I assist you today?" , "Hey there! Nice to see you." , "Hi! What’s up?"]))

        elif b in ["who are you" , "what is your name"]:
            print(r.choice(["I am a simple ChatBot created using Python." , "I’m your friendly Python chatbot." , "Just a basic chatbot, but happy to chat with you!"]))

        elif b in ["how are you" , "what is going on"]:
            print(r.choice(["I’m doing great, thanks for asking!" , "I’m fine, how about you?" , "I’m just a program, but I feel awesome."]))

        elif b in ["what can you do"]:
            print(r.choice(["I can chat with you using simple rules." , "I can answer basic questions, try me!" , "Mostly, I just keep you company."]))

        elif b in ["thanks" , "thank you"]:
            print(r.choice(["You’re welcome!" , "No problem at all!" , "Always happy to help!"]))

        elif b in ["joke" , "tell me a joke"]:
            print(r.choice(["Why do programmers prefer dark mode? Because light attracts bugs.",
                            "Why don’t scientists trust atoms? Because they make up everything!",
                            "I told my computer a joke… but it didn’t get it.",
                            "Why can’t you trust stairs? Because they’re always up to something."]))

        else:
            print(r.choice(["I don’t understand that yet." , "Can you rephrase it?" , "Sorry, I didn’t get that."]))