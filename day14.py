import random # to randomize player selection
# Art from: https://textart.io/
logo = ("""
    __  _         __ 
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/      """)
vs_art = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""
# ask a or b
# validate input
def user_input():
    while True: # loop until valid input
        choice = input("Who has more yellow cards? Type 'A' or 'B': ").upper()
        if choice in ['A', 'B']: # valid input
            return choice
        else:
            print("Invalid input. Please type 'A' or 'B'.") # prompt again
# compare cards
def compare(cards_a, cards_b, user_choice):
    if cards_a > cards_b: # A has more cards
        return user_choice == 'A' # True if user chose A, else False
    else:
        return user_choice == 'B' # True if user chose B, else False
# main game function
    
def game():
    print(logo)
    # Dictionary of football players with their country, club, and yellow card count
    football_players = {
    "Joao Palhinha": ["Portugal", "Fulham", 33],
    "Marcos Senesi": ["Brazil", "Bournemouth", 31],
    "Douglas Luiz": ["Brazil", "Aston Villa", 35],
    "Nelson Semedo": ["Portugal", "Wolverhampton Wanderers", 36],
    "Joao Gomes": ["Brazil", "Wolverhampton Wanderers", 34],
    "Moises Caicedo": ["Ecuador", "Chelsea", 30],
    "Flynn Downes": ["England", "West Ham United", 27],
    "Sasa Lukic": ["Serbia", "Fulham", 29],
    "Liam Delap": ["England", "Stoke City", 21],
    "Manuel Ugarte": ["Uruguay", "Chelsea", 28],
    "Will Hughes": ["England", "Crystal Palace", 3],
    "Dan Burn": ["England", "Newcastle United", 6],
    "Ryan Yates": ["England", "Nottingham Forest", 23],
    "Lucas Paqueta": ["Brazil", "West Ham United", 18],
    "Joelinton": ["Brazil", "Newcastle United", 11],
    "Facundo Medina": ["Argentina", "Lens", 15],
    "Yvan Neyou": ["Cameroon", "Leganés", 17],
    "Abdelhamid Sabiri": ["Morocco", "Sampdoria", 14],
    "Alexis Mac Allister": ["Argentina", "Liverpool", 9],
    "Alvaro Carreras": ["Spain", "Real Betis", 13],
    "Éderson": ["Brazil", "Manchester City", 5],
    "José Giménez": ["Uruguay", "Atlético Madrid", 7],
    "Julien Le Cardinal": ["France", "Sampdoria", 8],
    "Leon Goretzka": ["Germany", "Bayern Munich", 12],
    "Nuno Mendes": ["Portugal", "Paris Saint-Germain", 16],
    "Alvaro Fernandez": ["Spain", "Benfica", 10],
    "Mario Lemina": ["Gabon", "Wolverhampton Wanderers", 19]
    }
    score = 0 # initialize score
    names = list(football_players.keys()) # list of player names, we are list() to be able to edit it

    # Shuffle the names to randomize the order
    random.shuffle(names)

    player1 = random.choice(names) # select first player
    names.remove(player1) # remove to avoid repetition
    while len(names) > 0: # while there are players left to compare
        
        player2 = random.choice(names) # select second player
        names.remove(player2) # remove to avoid repetition

        print(f"Compare A: {player1}, a {football_players[player1][0]} footballer, playing for {football_players[player1][1]}.")
        print(vs_art)
        print(f"Against B: {player2}, a {football_players[player2][0]} footballer, playing for {football_players[player2][1]}.")

        choice = user_input()

        cards_a = football_players[player1][2] # get yellow card counts
        cards_b = football_players[player2][2] # get yellow card counts

        is_correct = compare(cards_a, cards_b, choice) # check if user was correct

        if is_correct:  # If user was correct
            score += 1
            print(f"You're right! Current score: {score}.")
            if cards_a > cards_b:
                player1 = player1 # player1 stays
            else:
                player1 = player2 # player2 becomes new player1
        else:
            print(f"Sorry, that's wrong. Final score: {score}. {player1} has {cards_a} yellow cards and {player2} has {cards_b} yellow cards.")
            return # end game
    print(f"Congratulations! You've compared all players. Final score: {score}.")
    

game()