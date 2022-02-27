from text import *
from users import *

ODDLEVAC = "-" * 40

#prihlaseni uzivatele
username = input("username: ").lower()
password = input("password: ")
print(ODDLEVAC)

if username in users.keys():
    if password == users.get(username):
        print(f"Welcome to the app, {username},\nWe have 3 texts to be analyzed.")
    else:
        print(f"Wrong password for user {username}.")
        exit()
else:
    print("Wrong username")
    exit()
print(ODDLEVAC)

#overeni vstupu pro kontrolu textu
number = int(input("Enter a number btw. 1 and 3 to select: "))-1
if 0 > number < len(TEXTS):
    print("There is no text with this number")
    exit()
print(ODDLEVAC)
