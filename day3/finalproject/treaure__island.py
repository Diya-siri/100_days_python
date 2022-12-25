#treasure-island game
print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')



print("Welcome to treasure island. Your mission is to find the treasure!! \n")
move=input("In which direction do you want to move first? Left or Right? \n").lower()
if move=="right" :
    print("Oh no! you fell in a hole! Game over!! \n")
elif move=="left":
    next=input("Do you want to swim or wait? \n").lower()
    if next=="swim" :
        print("Game over! There was a crocodile!")
    elif next=="wait" :
        door=input("Which door do u wanna pick? red , blue or yellow \n").lower()
        if door=="red":
            print("Danger zone. Game over!")
        elif door=="blue":
            print("Oh you met a blue monster, Game over!")
        elif door=="yellow" :
            print("You Won! You found the treasure!!")
        else :
            print("you chose a wrong door!")
    else:
        print("Wrong choice!")
else:
    print("Wrong direction")