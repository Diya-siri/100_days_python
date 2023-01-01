from os import system
from art import logo
print(logo)
def highest(record):
    max=0
    winner=""
    for bidder in record:
        bid_amt=record[bidder]
        if bid_amt>max:
            max=bid_amt
            winner=bidder
    print(f"The winner is {winner} with a bid amount {max} ")


dict={}
bidd=False
while not bidd:
    name=input("Enter the name: ")
    price=int(input("Enter the bid price: $"))
    dict[name]=price
    flag=(input("Type 'yes' to continue or 'no' to stop\n")).lower()
    if flag=="yes":
        system("cls")
    else:
        bidd=True
        highest(dict)


