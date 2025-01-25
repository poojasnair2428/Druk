def chatbot():
    print("Chatbot: Hi , you can call me Druk :)....I am a friendly chatbot hee hee....")

    print("Chatbot: You can type exit..to say bye to me!")

    while True:
        user_in= input("You: ").lower()

        if user_in=="exit" or user_in=="bye":
            print("Chatbot: Goodbye! i felt nice talking to you buddy :)")
        elif "hello"in user_in or "hi" in  user_in:
            print("Chatbot: how are you buddy ?")
        elif "bored" in user_in or "lazy" in user_in:
            print("Chatbot: Oh no !...hmm try watching some fun movie or new project ????")
        elif "fine" in user_in or "good" in user_in:
            print("Chatbot: Nice to hear that dear:)...can u share some incidents from today ?(ok/no need)")
        elif "great" in user_in or "amazing" in user_in:
            print("Chatbot: Ok dude..that's great!!....do you have something to share with me?(ok/no need")
        elif "sorry" in user_in or "no need" in user_in:
            print("Chatbot: It's ok dear...i hope you are ok. Don't pressurise yourself..goodthings take time :)")
        elif "thankyou" in user_in:
            print("Chatbot: ok buddy! i am always here for you as friend :)")
        else:
            print("okkkkkkk")