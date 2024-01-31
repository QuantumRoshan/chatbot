import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import requests
from weather import get_weather

def news_data(topic,api_key="c5478591e33b4db5bd341407f9d25567"):
    url="https://newsapi.org/v2/everything"
    paragm={
        "q":topic,
        "pageSize":1,
        "apikey":api_key
        
    }
    response=requests.get(url,params=paragm)
    if response.status_code==200:
        r=response.json()
        for article in r['articles']:
            print("\n")
            print(f"Title: {article['title']}")
            print(f"Author: {article['author']}")
            print(f"Content: {article['content']}")
            print(f"URL: {article['url']}")

    else:
        print("AI: Could not load the information")

def getnews():
    x=input("AI: Enter the topic :")
    news_data(x)

def weather_data(cityname):
    get_weather(cityname)

def getweather():
    y=input("AI: Enter the city :")
    weather_data(y)

def ask_capital(user_input):
    word_token=word_tokenize(user_input)

    pos_tags=pos_tag(word_token)

    nouns=[word for word,pos in pos_tags if pos in ['NN','NNS','NNP','NNPS']]#if pos macthes any of the list then word will  be stored as llist in nouns
    if "capital" in nouns and "france" in nouns:
        print("AI: Paris is the capital of France")
    else:
        print("AI: Sorry! I don't have information about this")

def greeting(user_input):
    
    user_data=word_tokenize(user_input)

    if any(word in user_data for word in Greetings):
        print("AI: Hey! how are you doing :)")
    else:
        print("AI: Sorry! I don't have information about this")

def normal_chat():
    print("AI: Good to hear")

def ask_chatbot():
    print("AI: I am doing great! Thanks for asking :)")

def exit():
    print("AI: Thank you for chatting with me! If you have more questions, feel free to return.")

def gt():
    print("AI: You are welcome!")

if __name__=="__main__":
    Greetings=["hi","hello","hey"]
    Grateful=["thanks","thank you","thank u"]
    print('''Hello I am your personal chatbot and i am programmed to do the following task:
1. Communicate with you
2. Provide you news about the given topic
3. Provide the weather of city
AI: How can i help you ?''')
    while True:
        user_input=input('''You: ''').lower()
        users_inv=word_tokenize(user_input)
        if "news" in users_inv or "2" in users_inv:
            getnews()
        elif "weather" in users_inv or "3" in users_inv:
            getweather()
        elif "capital" in user_input:
            ask_capital(user_input)
        elif any(i in users_inv for i in Greetings):
            greeting(user_input)
        elif "fine" in users_inv:
            normal_chat()
        elif "you" in users_inv and "doing" in users_inv:
            ask_chatbot()
        elif "exit" in users_inv or "bye" in user_input:
            exit()
            break
        elif any(i in users_inv for i in Grateful):
            gt()
        else:
            print("AI: Sorry I could not get your question")






#short but not so accurate method
# from nltk.tokenize import word_tokenize

# def ask_capital(user_input):
#     print("You asked about the capital. I don't have that information.")

# def respond_to_fine(user_input):
#     print("That's good.")

# def respond_to_doing(user_input):
#     print("I am doing great! Thanks for asking :)")

# def farewell(user_input):
#     print("Thank you for chatting with me! If you have more questions, feel free to return.")

# Greetings = ["hi", "hello", "hey"]
# print("Hello! How can I help you?")

# while True:
#     user_input = input('-').lower()
#     users_inv = word_tokenize(user_input)

#     if any(greeting_word in users_inv for greeting_word in Greetings):
#         print("Hello! How can I assist you?")
#     else:
#         response_functions = {
#             "capital": ask_capital,
#             "fine": respond_to_fine,
#             "doing": respond_to_doing,
#             "bye": farewell
#         }

#         for keyword, response_function in response_functions.items():
#             if keyword in users_inv:
#                 response_function(user_input)
#                 break
#         else:
#             print("Sorry, I couldn't understand your question.")
