import random
from os import system
from art import logo

def fun():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    p=random.choice(cards)
    return p

def calculate(cards):
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, computer has blackjack"
    elif user_score==0:
        return "You with a blackjack"
    elif user_score>21:
        return "You went over, you lose"
    elif computer_score>21:
        return "Component went over, you win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"
def play_game(): 

    user_card=[]
    computer_cards=[]
    flag=False
    for i in range(2):
        new_card=fun()
        user_card.append(new_card)
        computer_cards.append(fun())
    while not flag:
        user_score=calculate(user_card)
        computer_score=calculate(computer_cards)
        print(f"Your cards: {user_card} ,current score:{user_score}")
        print(f"Computer cards: {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            flag=True
        else:
            h=input("Type 'y' to get another card or 'n' otherwise: ").lower()
            if h=='y':
                user_card.append(fun())
            else:
                flag=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(fun())
        computer_score=calculate(computer_cards)
    print(f"your final score is ={user_score} ")
    print(f'computer final score is ={computer_score}')

    print(compare(user_score,computer_score))
print(logo)
p=input("Do you want to play a game of blackjack? Type 'y' or 'n' ")
while p=='y':
    system("cls")
    play_game()

