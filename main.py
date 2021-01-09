from replit import clear
from art import logo


print(logo)
print("Welcome to the secret auction program.")

end_of_bidding = False
bidding_dict = {}
highest_bid = 0
highest_bid_key = ""


while not end_of_bidding:

  name = str(input("What is your name? "))
  bid = float(input("What's your bid?  "))
  bidding_dict[name] = bid
  other_bidders = str(input("Are the any other bidders? Type 'Yes' or 'No' .\n")).lower()
  clear()

  if other_bidders == "no":
    end_of_bidding = True


for key in bidding_dict:
  if bidding_dict[key] > highest_bid:
    highest_bid = bidding_dict[key]
    highest_bid_key = key


print(logo)
print(f"The winner is {highest_bid_key}, with a bid of {highest_bid}")