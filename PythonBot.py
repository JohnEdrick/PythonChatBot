import random
import re
import os
from pyjokes import pyjokes
pattern1 = re.compile(r"\bname\b")
pattern2 = re.compile(r"\bjoke\b")
my_list = []
with open("mybot.txt", mode="r") as my_file:
    my_bot = my_file.readlines()
    for sentence in my_bot:
        my_list.append(sentence.strip())

clear = lambda: os.system('cls')
clear()
user_name = input("Enter your Name: ").capitalize()

message = "None"
print(f"Pybot: Hi {user_name}! How may I assist you?")
while message.upper() != "BYE":
    message = input(f"{user_name}: ")
    if pattern1.search(message):
        print("Pybot: Hello, My Name is Pybot!")
    elif pattern2.search(message):
        print(f"Pybot: {pyjokes.get_joke('en')}")
    elif message.upper() == "BYE":
        print(f"Here's my last Joke{pyjokes.get_joke('en')}")
    else:
        print(f"Pybot: {my_list[random.randrange(my_list.__len__())]}")

