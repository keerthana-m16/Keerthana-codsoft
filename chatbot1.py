def Chatbot():
    print("Hello! I am a simple Chatbot.Type'quit' to exit.")

    while True:
        user_input = input("you:").lower()

        if user_input == 'quit':
            print("Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How are you doing today?")
        elif "how are you?" in user_input:
            print("Chatbot: I'm doing well, thanks for asking! I'm a large language model, so I don't have feelings or emotions like humans do, but I'm always happy to chat and help with any questions or topics you'd like to discuss! How about you??")
        elif "are you a human or robot" in user_input:
            print("Chatbot: I am a robot, specifically a computer program designed to simulate conversation and answer questions to the best of my ability. I'm a type of artificial intelligence (AI) called a large language model, which means I've been trained on a massive dataset of text to generate human-like responses. So, while I'm designed to communicate in a way that feels natural and conversational, I'm definitely a machine!")
        elif "i have a doubt?" in user_input:
            print("Chatbot: Go ahead and ask away! What's on your mind?")
        elif "exit" in user_input:
            print("Chatbot: It was nice chatting with you. Feel free to come back and ask me anything if you need assistance in the future. Have a great day! Goodbye!")
        elif "thankyou" in user_input:
            print("Chatbot: You're welcome! It was a pleasure chatting with you. Take care!")  
        else:
            print("Chatbot: Sorry, I dont understand that. Can you ask me something else?")


#Start the chatbot
Chatbot()
