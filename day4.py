import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n"))
comp_choice = random.choice([0, 1, 2])
print(f"Computer chose {comp_choice}")
if user_choice == comp_choice:
    print("It is a Draw")
elif user_choice not in [0, 1, 2]:
    print("Invalid input. You lose")
elif user_choice == 0 and comp_choice == 2:
    print("You win!")
elif user_choice == 2 and comp_choice == 0:
    print("You lose!")
elif comp_choice > user_choice:
    print("You lose!")
elif user_choice > comp_choice:
    print("You win!")

   