from text import *
from users import *

ODDLEVAC = "-" * 40
count_title = 0                     #počet slov začínajících velkým písmenem
count_upper = 0                     #počet slov psaných velkými písmeny
count_lower = 0                     #počet slov psaných malými písmeny
count_number = 0                    #počet čísel (ne cifer)
count_sum = 0                       #suma všech čísel (ne cifer) v textu

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
    print("unregistered user, terminating the program..")
    exit()
print(ODDLEVAC)

#overeni vstupu pro kontrolu textu
index = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))-1
if 0 > index or index > len(TEXTS):
    print("There is no text with this number")
    exit()
print(ODDLEVAC)

text = TEXTS[index]

#analýza textu
words_list = text.split()
len_dict = {}
i = 0                               #pomocný index
for word in words_list:
    word = word.strip(" ,;.\n")     #ocisteni slova
    if word.istitle():              #pocitani
        count_title += 1
    elif word.isupper():
        count_upper += 1
    elif word.islower():
        count_lower += 1
    elif word.isnumeric():
        count_number += 1
        count_sum += int(word)
    words_list[i] = word
    i += 1
    len_dict[len(word)] = len_dict.get(len(word), 0) + 1

print(f"There are {len(words_list)} words in the selected text.")
print(f"There are {count_title} titlecase words.")
print(f"There are {count_upper} uppercase words.")
print(f"There are {count_lower} lowercase words.")
print(f"There are {count_number} numeric strings.")
print(f"The sum of all the numbers {count_sum}")
print(ODDLEVAC)

#sloupcový graf
tab = int(max(list(len_dict.values())))         #delka prostredniho sloupce pocitana podle nejdelsiho slova
if tab % 2 != 0:                                #oprava je delka liche cislo
    tab += 1
print(f"LEN|{' ' * ((tab-9)//2)}OCCURENCES{' ' * ((tab-9)//2)}|NR.")
set_len = sorted(set(len_dict))
for j in set_len:
    print(f"{' ' * (3 - len(str(j)))}{j}|{'*' * len_dict.get(j)}{' ' * (tab - len_dict.get(j))}|{len_dict.get(j)}")
