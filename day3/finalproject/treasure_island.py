#treasure-island game

print("Welcome to treasure island. Your mission is to find the treasure!! \n")
move=input("In which direction do you want to move first? Left or Right? \n").lower()
if move=="right" :
    print("Oh no! you fell in a hole! Game over!! \n")
else :
    next=input("Do you want to swim or wait? \n").lower()
    if next=="swim" :
        print("Game over! There was a crocodile!")
    else :
        door=input("Which door do u wanna pick? red , blue or yellow \n").lower()
        if door=="red":
            print("Danger zone. Game over!")
        elif door=="blue":
            print("Oh you met a blue monster, Game over!")
        elif door=="yellow" :
            print("You Won! You found the treasure!!")
        else :
            print("you chose a wrong door!")


