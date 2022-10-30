# Prerequisites of this project:
# 1. Create a greeting for your program.
# 2. Take the name and bid amount from the user and store it in a dictionary.
# 3. You can enter any number of names and their bids based on your requirement.
# 4. When adding new name, keep in mind that screen should be cleared so that other users can't see your input.
# 5. After adding all bidders, show the maximum bid amount and bidder name.

# Solution to this project:
from blindAuctionArt import logo
import os

should_continue = True
auction_data = {}


def highest_bidder(bidder_list):
    highest_bid = 0
    winner = ''
    for bidder in bidder_list:
        if bidder_list[bidder] > highest_bid:
            highest_bid = bidder_list[bidder]
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}.')


print(logo)
print('Welcome to the blind auction program.')

while should_continue:
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    auction_data[name] = bid
    result = input("Are there any other bidders? Type 'yes' or 'no'.")
    if result == 'no':
        should_continue = False
        os.system('cls')
        highest_bidder(auction_data)
    elif result == 'yes':
        should_continue = True
        os.system('cls')
