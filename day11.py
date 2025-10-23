import random

def random_card():
    return random.randint(1, 11)

def is_game_over(l):
    if sum(l) == 21 or sum(l) > 21:
        return True
    return False

def compare_scores(a, b):
    c1 = sum(a)
    c2 = sum(b)


    if c2 > 21:
        print(f"You win with a total of {sum(a)}, while computer's hand: {b}")
    elif c1 == c2:
        print(f"It is draw. Your hand: {a} and Computer's hand: {b}")
    elif c1 < 21:
        print(f"You lose. Computer's hand: {b}")
    elif c1 > c2:
        print(f"You win with a total of {sum(a)}, while computer's hand: {b}")
    else:
        print(f"You lose. Computer's hand: {b}")
def blackjack():

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n':    ") == "y":
        user_hands = [random_card() for i in range(2)]
        comp_hands = [random_card() for i in range(2)]
        print(f"Your cards: {user_hands}, current score: {sum(user_hands)}")
        print(f"Computer's first card: {comp_hands[0]}")

        is_on = True
        while is_on:
            next_card = input("Type 'y' to get another card, type 'n' to pass:    ")
            if next_card == "y":
                user_hands.append(random_card())
                while 11 in user_hands and sum(user_hands) > 21:
                    user_hands[user_hands.index(11)] = 1
                is_on = not is_game_over(user_hands)
                if not is_on:
                    player_busted = True
                    break


            if not player_busted:
                while sum(comp_hands) < 17:
                    while 11 in comp_hands and sum(comp_hands) > 21:
                        comp_hands[comp_hands.index(11)] = 1
                    comp_hands.append(random_card())
                is_on = not is_game_over(comp_hands)

        compare_scores(user_hands, comp_hands)
        
    else:
        return


blackjack()