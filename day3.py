print("Welcome to TREASURE ISLAND\n")
question = "Do you want to take Left or Right\n"
response = input(f"{question}").upper()
if response == "RIGHT":
    answer = input("Run or Wait\n").upper()
    if answer == "RUN":
        ans = input("Which car: AUDI, BMW, OR FERRARI\n").upper()
        if ans == "AUDI":
            print("You win!")
        elif ans == "BMW":
            print("Wrong. Game Over!")
        else:
            print("Wrong. Game Over!")
    else:
        print("Run out of oxygen. Game Over!")

else:
    print("Fell into a hole. Game Over!")