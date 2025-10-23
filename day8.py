import string

letters = list(string.ascii_lowercase)



def cipher(option,letters_list):
    
    word = list(input("Type your message:    \n").lower())
    shift = int(input("Type how many to shift:    ")) 

    a_list = []

    if option == "decode":
        shift = -shift
    
    for i in range(len(word)):
        if word[i] not in letters_list:
            a_list.append(word[i])
        else:
            a_list.append(letters_list[(letters_list.index(word[i])+shift) % 26])

    

    print("".join(a_list))

    

     
    
    


game_on = True

while game_on:
    user_choice = input("WeLcOMe To CaEsAr CiPhEr! Type encode or decode:    ").lower()
    if user_choice not in ["encode", "decode"]:
        print("Please only type encode or decode!")
        continue
    cipher(user_choice, letters)

    to_again = input("Type ok to do it again. Type no otherwise.\n").lower()

    if to_again != "ok":
        print("See you!")
        game_on = False
    

        
