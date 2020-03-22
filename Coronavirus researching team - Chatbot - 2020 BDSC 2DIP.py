#Coronavirus Researching team
#2020 BDSC 2DIP
#Sunny Huang
#Alan Nguyen 
#Phoenix Wong 
#Jordan Wu 
#This programme can respond to greetings and coronavirus-related contents


#----------------------------------------------------------------------------------------------------------------------------------------------------
import random

greeting_input = ["hi", "hey", "hello", "yo"]
greeting_responses = ["Hi!", "Hello!", "Yo!"]
corona = ["virus", "corona", "coronavirus", "infection", "symptoms", "symptom", "cough", "fever"]
you = ""
you_lower = ""
you_split = ""


#Functions-------------------------------------------------------------------------------------------------------------------------------------------
def check_greeting_questions():
    check_greeting_questions.response = ""
    for words in you_split:
        if words in greeting_input:
            check_greeting_questions.response = random.choice(greeting_responses)
            print("Chatbot(Sunny): " + check_greeting_questions.response) 
    
def check_corona_questions():
    for words in you_split:
        if words in corona:
            check_corona_questions.response = True
            print("Chatbot(Sunny): Want to know more about coronavirus? Please enter the index one of the following topics: ")
            print("Chatbot(Sunny): 1: General information of coronavirus.")
            print("Chatbot(Sunny): 2: Symptoms of coronavirus.")
            print("Chatbot(Sunny): 3: Impacts on the world.")
            print("Chatbot(Sunny): 4: How to protect yourself from coronavirus.")  
            print("chatbot(sunny): 5: how the coronavirs spreads.")
            print('Chatbot(Sunny): Type "exit" to exit coronavirus mode. ')
                      
def check_if_can_not_respond():
    if check_greeting_questions.response == "" and check_corona_questions.response == False:
        print("Chatbot(Sunny): Sorry I don't understand.")        


#Main------------------------------------------------------------------------------------------------------------------------------------------------
check_corona_questions.response = False
print("Chatbot(Sunny): Hi! I'm Sunny, a chatbot that can provide you the basic information fpr coronavirus. Please ask me a question. ")

while True:
    you = input("You: ")
    you_lower = you.lower()
    you_split = you_lower.split()

    if check_corona_questions.response == False:
        check_greeting_questions()
        check_corona_questions()
        check_if_can_not_respond()

    elif check_corona_questions.response == True:
        for words in you_split:
            if words == "1":
                print("Chatbot(Sunny):  Covid 19 is a virus of the coronavirus family,") 
            elif words == "2":
                print("Chatbot(Sunny): The effects of Corona Virus on human body, symptoms include respiratory symptoms, fever, cough, shortness of breath and breathing difficulties. In more severe cases Corona Virus can also cause Pneumonia, severe acute respiratory syndrome, kidney failure that eventually can lead to death. It can also cause flu-like symptoms on Human Body such as coughing, sore throat and fatigue.")  
            elif words == "3":
                print("Chatbot(Sunny): Corona virus has impacted China downgrading its emerging market (EM) growth from 4.5% to 4.1%. China itself accounts for the largest part of our downgrade (down 0.5 percentage points to 5.5%). As well as France and Itlay seeing a reduction in tourism due to the virus spreading around the world, and lastly impacting global inflation that remains relatively benign in the forecast, ticking up to 2.6% this year before declining to 2.3% in 2021.")
            elif words == "4":
                print("Chatbot(Sunny): To protect yourself from coronavirus ,you need to wash your hand with soap frequently, try to maintain social distancing, avoid touching your eyes mouth and nose ") 
            elif words == "5":
                print("Chatbot(Sunny): The first infections were linked to a live animal market, but the virus is now spreading from person-to-person.The virus seems to be spreading easily and sustainably in the community with people being infected and some who are not sure if they have become infected")
            elif words == "exit":
                check_corona_questions.response = False
                print("Chatbot(Sunny): Exit coronavirus mode. ")
            else:
                print("Chatbot(Sunny): Sorry I don't understand. Please type \"1\" or \"2\" or \"3\" or \"4\" or \"5\" or \"exit\". ")