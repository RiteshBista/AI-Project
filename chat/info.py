from chat.chat import chat_conversation as chat

def learn(data):

    if "day" in data:
        chat.day()

    elif "news" in data:
        chat.news()

    elif "time" in data:
        chat.current_time()

    elif "temp" in data:
        chat.temp()
    

    elif "exit" in data:
        chat.Exit()

    else:
        print(" Sorry,apologies. I am not trained for it")   
