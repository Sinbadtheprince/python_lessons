import random
print("Welcome to number guessing game!")
print("I am guessing a number from 1 to 100.")
def number_guess():
    
    level = input("Choose a difficulty. Type 'easy' or 'hard'     ")
    if level not in ["easy", "hard"]:
        print("Please enter 'easy' or 'hard'")
        number_guess()
        return
    attempts = 10
    if level == "hard":
        attempts = 5

    random_number = random.randint(1, 100)
    while attempts > 0:
        print(f"You have {attempts} attempts.")
        user_guess = int(input("Make a guess:    "))
        if user_guess == random_number:
            print("You have won.")
            break
        elif user_guess > random_number:
            print("Too high.")
            attempts -= 1
        elif user_guess < random_number:
            print("Too low")
            attempts -= 1

number_guess()

