import string
import random

letters = list(string.ascii_uppercase)
symbols = list(string.punctuation)
numbers = list(string.digits)

user_letter = int(input("How many letters do you want?\n"))
user_symbol = int(input("How many symbols do you want?\n"))
user_number = int(input("How many numbers do you want?\n"))

a_list = []

for i in range(user_letter):
    a_list.append(random.choice(letters))

for k in range(user_symbol):
    a_list.append(random.choice(symbols))

for m in range(user_number):
    a_list.append(random.choice(numbers))
print(a_list)

random.shuffle(a_list)

print(*a_list, sep="")