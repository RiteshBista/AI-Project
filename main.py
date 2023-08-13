from chat.chat import chat_conversation
from chat.info import learn 

def main():
    chat_conversation.greeting()
    while True:
        data = input(f'You: ')
        learn(data)
    

if __name__ == "__main__":
    main()