import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import requests

def get_movie_details(movie_name,api_key="370a353"):
    base_url = "http://www.omdbapi.com/"
    params = {
        'apikey': api_key,
        't': movie_name
    }

    response = requests.get(base_url, params=params)
    movie_data = response.json()

    if movie_data.get('Response') == 'True':
        # Handle the movie details, including reviews, in the 'movie_data' variable
        v=f'''Title: {movie_data['Title']}
Released: {movie_data['Released']}
Language: {movie_data['Language']}
Writer: {movie_data['Writer']}
Director: {movie_data['Director']}
Plot: {movie_data['Plot']}'''
        return v
    else:
        return(f"Error: {movie_data.get('Error')}")



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
            a= f'''Title  : {article["title"]}
Author : {article["author"]}
Content: {article["content"]}'''
            return a


            # print(f"Title: {article['title']}")
            # print(f"Author: {article['author']}")
            # print(f"Content: {article['content']}")
            # print(f"URL: {article['url']}")
            # print("-" * 40)

    else:
        print("AI: Could not load the information")

def get_weather(city,api_key="9f50f3822dea043fdba999378ac25cb3"):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        return(f"Weather in {city} is {weather_data['weather'][0]['description']}")
    else:
        return(f"Error: {weather_data['message']}")



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
        a="AI: Hey! how are you doing :)"
        print(a)
        return a
    else:
        print("AI: Sorry! I don't have information about this")

def normal_chat():
    a="AI: Good to hear"
    print(a)
    return a
    

def ask_chatbot():
    print("AI: I am doing great! Thanks for asking :)")

def exit():
    print("AI: Thank you for chatting with me! If you have more questions, feel free to return.")

def gt():
    print("AI: You are welcome!")

# if __name__=="__main__":
#     Greetings=["hi","hello","hey"]
#     Grateful=["thanks","thank you","thank u"]
#     print('''Hello I am your personal chatbot and i am programmed to do the following task:
# 1. Communicate with you
# 2. Provide you news about the given topic
# 3. Provide the weather of city
# AI: How can i help you ?''')
Greetings=["hi","hello","hey"]
Grateful=["thanks","thank you","thank u"]
def plzwork(user_input):
        # user_input=input('''You: ''').lower()
        users_inv=word_tokenize(user_input)
        if "Dhoni" in users_inv or "2" in users_inv:
                topic="Dhoni"
                api_key="c5478591e33b4db5bd341407f9d25567"
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
                        a=f''' "Title: {article['title']}"
                        f"Author: {article['author']}"
                        f"Content: {article['content']}"
                        f"URL: {article['url']}"'''
                        print(a)
                        return a
                    

                else:
                    print("AI: Could not load the information")
        elif "weather" in users_inv or "3" in users_inv:
            getweather()
        elif "capital" in user_input:
            ask_capital(user_input)
        elif any(i in users_inv for i in Greetings):
            a="AI: Hey! how are you doing :)"
            return a
        
            # if a=="hi":
    #     text.insert(END,f"You: {a}")
    #     text.insert(END,"\n"+"AI: hi how are you")
        elif "fine" in users_inv:
                a="AI: Good to hear"
                print(a)
                return a

            # normal_chat()
        elif "you" in users_inv and "doing" in users_inv:
            ask_chatbot()
        elif "exit" in users_inv or "bye" in user_input:
            exit()
        elif any(i in users_inv for i in Grateful):
            gt()
        else:
            a="AI: Sorry I could not get your question"
            print(a)
            return a
            

                       


def xyz(a):
    z=f"hi{a}"
    print(z)
    return z

# def xyz(user_input):
#     # Your main logic goes here
#     output = f"Received input: {user_input}"
#     print(output)
#     return output

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
