import os

# def auction(bids_dict):
#     print(f"Before {bids_dict}")
#     user_name = input("What is your name?\n").lower()
#     user_bid = int(input("What is your bid?\n"))
#     bids_dict[user_name] = user_bid
#     print(f"After: {bids_dict}")
#     max = 0
#     max_bidder = ""

#     for key, value in bids_dict.items():
#         if value > max:
#             max = value
#             max_bidder = key
    
#     return max_bidder, max
# # print(auction({"a":15, "b":788, "c":89}))
# # action_on = True
# bids = {}
# # while action_on:
    
# #     auction(bids)
# #     to_continue = input("Are there any other bidders? Type yes or no.\n").lower()
# #     print("hi")
# #     if to_continue != "yes":
# #         print("dlakjf")
# #         print(f"The winner is {auction(bids)[0]} with a bid of {auction(bids)[1]}")
        

# auction(bids)
# more_bidders = input("Are there more bidders. Type yes or no.    ").lower()
# print(f"The winner is {auction(bids)[0]} with a bid of {auction(bids)[1]}")
# print("Hi")
# if more_bidders == "yes":
#     os.system("cls")
#     auction(bids)
# else:
#     print(f"The winner is {auction(bids)[0]} with a bid of {auction(bids)[1]}")


    
    

def getinfo():
    name = input("What is your name?    ")
    bid = int(input("What is your bid?    "))
    return name, bid

def to_continue(switch):
    others = input("Are there other bidders? Type yes or no.\n").lower()
    if others != "yes":
        switch = False
    else:
        os.system("cls" if os.name == "nt" else "clear")
    return switch

def max_bid(name, bid, bid_dict):
    bid_dict[name] = bid
    max_value = 0
    max_bidder = ""
    for key, value in bid_dict.items():
        if value > max_value:
            max_value = value
            max_bidder = key
    return max_bidder, max_value



bids = {}
game_switch = True
print("Welcome to the Auction!")
while game_switch:
    user_name, user_bid = getinfo()
    game_switch = to_continue(True)
    winner, amount = max_bid(user_name, user_bid, bids)


print(f"The winner is {winner} with a {amount}")


    



