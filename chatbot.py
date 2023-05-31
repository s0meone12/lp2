from tkinter import *
root = Tk()
root.title("Chatbot")
def send():    
    send = "You -> "+e.get()
    txt.insert(END, "n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "n" + "Bot -> Hello")
    elif(e.get() == "how are you"):
        txt.insert(END, "n" + "Bot -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "n" + "Bot -> Great! how can I help you.")
    else:
        txt.insert(END, "n" + "Bot -> Sorry! I dind't got you")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()

# second code
import random

# Define a dictionary of predefined responses
responses = {
    "hello": "Hello!",
    "how are you?": "I'm good, thank you!",
    "what's your name?": "My name is ChatBot.",
    "default": "Sorry, I didn't understand that."
}

# Function to generate a response based on user input
def generate_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

# Main conversation loop
while True:
    # Get user input
    user_input = input("User: ")

    # Generate and print response
    response = generate_response(user_input)
    print("ChatBot:", response)

    # Check if the user wants to exit the conversation
    if user_input.lower() == "bye":
        break


# chatbot third code
# import random

# # Define a dictionary of predefined responses
# responses = {
#     "greeting": ["Hello!", "Hi there!", "Welcome! How can I assist you today?"],
#     "goodbye": ["Goodbye!", "Thank you for visiting. Have a great day!"],
#     "help": ["Sure, I'm here to help. What do you need assistance with?", "How can I assist you today?"],
#     "default": "I'm sorry, I didn't quite understand. Could you please rephrase that?"
# }

# # Function to generate a response based on user input
# def generate_response(user_input):
#     user_input = user_input.lower()
#     if "hello" in user_input or "hi" in user_input:
#         return random.choice(responses["greeting"])
#     elif "bye" in user_input or "goodbye" in user_input:
#         return random.choice(responses["goodbye"])
#     elif "help" in user_input:
#         return random.choice(responses["help"])
#     else:
#         return responses["default"]

# # Main conversation loop
# while True:
#     # Get user input
#     user_input = input("Customer: ")

#     # Generate and print response
#     response = generate_response(user_input)
#     print("ChatBot:", response)

#     # Check if the user wants to end the conversation
#     if "bye" in user_input.lower():
#         break
