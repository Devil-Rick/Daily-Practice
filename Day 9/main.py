from replit import clear
import logo as lg

next_person = "yes"
auction = {}

while next_person == "yes":
    print(lg.logo)
    print("\n\nWelcome to the secret Auction Program.\n ")
    name = input("What is your name ? \n").capitalize()
    bid = int(input("What's you bid ? $"))
    auction[name] = bid
    next_person = input(
        "Are there any other bidders ? Type 'yes' or 'no' \n").lower()
    clear()
else:
    print(lg.logo)
    print("\n\nWelcome to the secret Auction Program.\n ")
    auction_winner = ""
    highest_bid = 0
    for key in auction:
        if highest_bid < auction[key]:
            highest_bid = auction[key]
            auction_winner = key
    print(f"The winner is {auction_winner} with a bid of ${highest_bid}")
