logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\
'''

import os
print(logo)
bids = {}
bid_finished = False

def find_highest_bidder(Bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in Bidding_record:
    bid_amount = int(Bidding_record[bidder])
    if bid_amount > highest_bid:
     winner = bidder
     highest_bid = bid_amount
  print(f"The winner is {winner} with a bidding amount {highest_bid}")


while not bid_finished :
  name = input("Enter your name :\n").lower()
  price = input("What is your bidding amount $ \n")
  bids[name] = price
  should_continue  = input('Are there any other bidder type "yes" or "no"').lower()
  if should_continue == "no":
    bid_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    os.system('clear')
  