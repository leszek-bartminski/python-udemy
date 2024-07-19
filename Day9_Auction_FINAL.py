from art import logo

def clear():
  print("\033[H\033[J", end="")

diki = {}

print(logo)

print("Welcome to the secret auction program.")

def auction(name1, bid1):
  diki[name1] = bid1

name1 = input("What's your name?: ")
bid1 = int((input("What's your bid?: ")).strip("$"))

diki = {name1: bid1}



choice = input("Are there any other bidders? Type 'y' for YES or 'n' or any other key for NO:\n")

while choice == "y":
  clear()
  name1 = input("What's your name?: ")
  bid1 = int((input("What's your bid?: ")).strip("$"))
  auction(name1, bid1)
  choice = input("Are there any other bidders? Type 'y' for YES or 'n' or any other key for NO:\n")
print(diki)



winner_bid = bid1
winner = name1

for x in diki:  
  
  if diki[x] > winner_bid:
    winner_bid = diki[x]
    winner = x
  # print(winner_bid)

print(f"The winner is {winner} with a bid of ${winner_bid}.")