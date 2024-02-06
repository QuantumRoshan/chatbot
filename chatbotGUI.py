from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from tkinter import *
from testchatbot import *
from tkinter import ttk
import os


root=Tk()
Features='''Hello I am your personal chatbot and i am programmed to do the following task:
1. Communicate with you
2. Provide news about the given topic
3. Provide the weather of city
4. Provide detail of movies'''

Greetings=["hi","hello","hey","hlo"]
Grateful=["thanks","thank you","thank u"]

def greetingtk(event=None):
    user_input=e.get().lower()
    tokenize_user_input=word_tokenize(user_input)

    if any(i in Greetings for i in tokenize_user_input):
        text.insert(END,"\n"+f"You: {user_input}")#end behaves as append in the text widget
        text.insert(END,"\n"+"AI: Hey! how are you doing 😊")

    elif "fine" in tokenize_user_input:
        text.insert(END,"\n"+f"You: {user_input}")
        text.insert(END,"\n"+"AI: Good to hear 😊") 

    elif any(i in Grateful for i in tokenize_user_input):
        text.insert(END,"\n"+f"You: {user_input}")
        text.insert(END,"\n"+"AI: You are welcome 😊") 

    elif "news" in tokenize_user_input:
                text.insert(END,"\n"+f"You: {user_input}")
                topic=tokenize_user_input[-1]
                news= news_data(topic)
                text.insert(END,"\n"+f"AI: Sure here is the news about {topic}:")
                text.insert(END,"\n"+f"{news}")

    elif "movie" in tokenize_user_input or "detail" in tokenize_user_input:
                movie=tokenize_user_input[-1]
                movie_detail=get_movie_details(movie)
                text.insert(END,"\n"+f"You: {user_input}")
                text.insert(END,"\n"+f"AI: Here are the details of movie {movie} ")
                text.insert(END,"\n"+f"{movie_detail}")
    elif "weather" in tokenize_user_input:
          place=tokenize_user_input[-1]
          weatherX=get_weather(place)
          text.insert(END,"\n"+f"You: {user_input}")
          text.insert(END,"\n"+f"AI: {weatherX}")
               
    elif "bye" in tokenize_user_input or "exit" in tokenize_user_input:
         root.destroy()

    else:
         text.insert(END,"\n"+f"You: {user_input} ")
         text.insert(END,"\n"+f"AI: Sorry couldn't get your question ☹️")


def show_info_window():
    info_window = Toplevel(root)# Create a new Toplevel window (popup)
    info_window.title("AI Information")# Set the title of the popup window
    
    info_label = Label(info_window, text=Features)
    info_label.pack(padx=20, pady=20)
    ok_button = ttk.Button(info_window, text="OK", command=info_window.destroy)
    ok_button.pack(pady=10)    
    
def save_chat_history():
    project_directory="D:\\programs\\vs code python\\projects\\chatbot"
    chat_history_path=os.path.join(project_directory,"chat_history.txt")
    with open(chat_history_path, "a", encoding="utf-8") as file:#used encoding bcz used emoji
        file.write(text.get(1.0, END))

def exittk():
    root.destroy() 

def clear_chat():
    text.delete(1.0, END)

info_button =ttk.Button(root, text="AI Info", command=show_info_window)
info_button.grid(row=0, column=0, columnspan=2)

text=Text(root,width=100)
text.grid(row=1,column=0,columnspan=1)

e=Entry(root,width=143)
e.grid(row=2,column=0)

enter_button=ttk.Button(root,text="Enter",command=greetingtk)
enter_button.grid(row=2,column=1)

exit_button=ttk.Button(root,text="exit",command=exittk)
exit_button.grid(column=0,row=3,columnspan=1)

    
clear_button = ttk.Button(root, text="Clear", command=clear_chat)
clear_button.grid(row=3, column=1)

history_button = ttk.Button(root, text="Save Chat History", command=save_chat_history)
history_button.grid(row=4, column=1)

scrollbar = Scrollbar(root, command=text.yview)
scrollbar.grid(row=1, column=1, sticky='nsew')
text.config(yscrollcommand=scrollbar.set)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
text.config(font=("Georgia", 12), fg="#555555", bg="#D3D3D3")

e.insert(0, "Type your message here...")
e.bind("<FocusIn>", lambda event: e.delete(0, END))


# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Display it in your GUI
datex=Label(root,text= f"{current_datetime}")
datex.grid(column=1,row=0)

root.resizable(False,False)

root.bind('<Return>', greetingtk)#root: This is the Tkinter window or frame to which the binding is applied.
# .bind: This is a method in Tkinter that is used to bind an event to a function.
# '<Return>': This specifies the event to bind, in this case, the "Return" key, which corresponds to the "Enter" key on the keyboard.
# greetingtk: This is the function that will be called when the specified event occurs.
root.title("AI")
root.mainloop()