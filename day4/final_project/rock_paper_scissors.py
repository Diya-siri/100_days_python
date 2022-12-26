import random


rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to rock papaer & scissors!!")
list=[rock,paper,Scissors]
n=int(input("What do u choose? Type 0 for rock,1 for paper or 2 for scissors. "))
print(list[n]+"\n")
r=random.randint(0,2)
print("computer chose : ")
print(list[r])

if n==r :
    print("Its a draw!")
elif n==2 and r==0:
    print("You lose")
elif n==0 and r==2 :
    print("you win")
elif n>r:
    print("You win")
elif r>n:
    print("You lose")
elif n>=3:
    print("Wrong choice!")


    