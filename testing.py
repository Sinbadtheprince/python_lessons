import random

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

def user_input():
    while True:
        choice = input("Who has more yellow cards? Type 'A' or 'B': ").upper()
        if choice in ['A', 'B']:
            return choice
        else:
            print("Invalid input. Please type 'A' or 'B'.")

def compare(cards_a, cards_b, user_choice):
    if cards_a > cards_b:
        return user_choice == 'A'
    else:
        return user_choice == 'B'
    
def game():
    print(logo)
    genome_sizes = {
    "Homo sapiens (human)": 3.1e9,        # ~3.1 Gb :contentReference[oaicite:0]{index=0}
    "Mus musculus (mouse)": 2.7e9,        # ~2.7 Gb :contentReference[oaicite:1]{index=1}
    "Canis lupus familiaris (dog)": 2.4e9, # ~2.4 Gb :contentReference[oaicite:2]{index=2}
    "Gallus gallus (chicken)": 1.2e9,     # ~1.2 Gb :contentReference[oaicite:3]{index=3}
    "Drosophila melanogaster (fruit fly)": 1.75e8, # ~175 Mb :contentReference[oaicite:4]{index=4}
    "Caenorhabditis elegans": 1.0e8,       # ~100 Mb :contentReference[oaicite:5]{index=5}
    "Saccharomyces cerevisiae (yeast)": 1.2e7, # ~12 Mb :contentReference[oaicite:6]{index=6}
    "Arabidopsis thaliana": 1.57e8,        # ~157 Mb :contentReference[oaicite:7]{index=7}
    "Oryza sativa (rice)": 5.65e8,          # ~565 Mb :contentReference[oaicite:8]{index=8}
    "Zea mays (maize / corn)": 5.0e9,       # ~5 Gb :contentReference[oaicite:9]{index=9}
    "Triticum aestivum (wheat)": 1.7e10,    # ~17 Gb :contentReference[oaicite:10]{index=10}
    "Fritillaria assyrica (flower)": 1.2e11, # ~120 Gb :contentReference[oaicite:11]{index=11}
    "Elephas maximus (Asian elephant)": 3.38e9, # ~3.38 Gb :contentReference[oaicite:12]{index=12}
    "Loxodonta africana (African elephant)": 3.31e9, # ~3.31 Gb :contentReference[oaicite:13]{index=13}
    "Thunnus maccoyii (southern bluefin tuna)": 7.95e8, # ~795 Mb :contentReference[oaicite:14]{index=14}
    "Amoeba dubia": 6.7e11,                # ~670 Gb :contentReference[oaicite:15]{index=15}
    "Tmesipteris oblanceolata (fork fern)": 1.60e11,   # ~160 Gb (largest known plant genome) :contentReference[oaicite:16]{index=16}
    "Picea abies (Norway spruce)": 2.0e10, # ~20 Gb :contentReference[oaicite:17]{index=17}
    "Axolotl (Ambystoma mexicanum)": 3.2e10, # ~32 Gb :contentReference[oaicite:18]{index=18}
    "Populus trichocarpa (black cottonwood)": 4.8e8, # ~480 Mb :contentReference[oaicite:19]{index=19}
    "Apis mellifera (honey bee)": 2.36e8,   # ~236 Mb :contentReference[oaicite:20]{index=20}
    "Fugu rubripes (pufferfish)": 4.00e8,    # ~400 Mb :contentReference[oaicite:21]{index=21}
    "Danio rerio (zebrafish)": 1.7e9,        # ~1.7 Gb :contentReference[oaicite:22]{index=22}
    "Neurospora crassa (fungus)": 3.99e7,    # ~39.9 Mb :contentReference[oaicite:23]{index=23}
    "Ciona intestinalis (sea squirt)": 1.60e8, # ~160 Mb :contentReference[oaicite:24]{index=24}
    "Musca domestica (housefly)": 6.2e8,     # ~620 Mb (approx) — value from various sources
    "Bos taurus (cow)": 2.7e9,                # ~2.7 Gb :contentReference[oaicite:25]{index=25}
    "Pan troglodytes (chimpanzee)": 3.3e9,     # ~3.3 Gb :contentReference[oaicite:26]{index=26}
    "Gorilla gorilla (gorilla)": 3.0e9,        # ~3.0 Gb (similar ballpark)
    "Equus caballus (horse)": 2.41e9,          # ~2.41 Gb :contentReference[oaicite:27]{index=27}
    "Felis catus (cat)": 2.35e9,               # ~2.35 Gb :contentReference[oaicite:28]{index=28}
    "Sus scrofa (pig)": 2.8e9,                # ~2.8 Gb (approx, commonly cited)
}

    score = 0
    names = list(genome_sizes.keys()) # list of genome names, we are list() to be able to edit it

    # Shuffle the names to randomize the order
    random.shuffle(names)

    player1 = random.choice(names)
    names.remove(player1)
    while len(names) > 0:
        
        player2 = random.choice(names)
        names.remove(player2)

        print(f"Compare A: {player1}")
        print(vs_art)
        print(f"Against B: {player2}")

        choice = user_input()

        cards_a = genome_sizes[player1]
        cards_b = genome_sizes[player2]

        is_correct = compare(cards_a, cards_b, choice)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            if cards_a > cards_b:
                player1 = player1
            else:
                player1 = player2
        else:
            print(f"Sorry, that's wrong. Final score: {score}. {player1} has {cards_a} genes and {player2} has {cards_b} genes.")
            return
    

game()