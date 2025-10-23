import random


# Sports-themed words for Hangman
sports_words = [
    "football",
    "basketball",
    "tennis",
    "cricket",
    "baseball",
    "hockey",
    "golf",
    "rugby",
    "boxing",
    "swimming",
    "cycling",
    "volleyball",
    "badminton",
    "wrestling",
    "karate",
    "judo",
    "skiing",
    "snowboarding",
    "surfing",
    "archery",
    "fencing",
    "rowing",
    "gymnastics",
    "marathon",
    "triathlon"
]

word_to_guess = random.choice(sports_words)


def play_hangman(word):
    print("Welcome to Hangman Sports Names!")

    lives = 6
    word_list = list(word)
    blanks = ["_" for i in range(len(word))]
    correct_letters = []
    
    

    while lives > 0:
        print(f"Your lives {lives}")
        print(f"Sport to guess:   {" ".join(blanks)}")
        guessed_letter = input("Guess a letter:    ").lower()
        if len(guessed_letter) > 1:
            print("Please only enter a single letter!")
            continue
        if guessed_letter in correct_letters:
            print(f"You have already guessed {guessed_letter}")
        if guessed_letter not in word:
            lives -= 1
            print(f"You guessed {guessed_letter}. You lose a life.")

        else:
            for i in range(len(word)):
                if word_list[i] == guessed_letter:
                    blanks[i] = guessed_letter
                    correct_letters += guessed_letter
            print(*blanks)

            
            
        if "".join(blanks) == word:
            print("You win!")
            break
        elif lives == 0:
            print(f"You lose. The word was {word}")
            break
        else:
            continue

play_hangman(word_to_guess)
        



