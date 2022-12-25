print("welcome to python pizza deliveries")
s=input("What size of pizza do u want? S,M,OR L?")
pep=input("Do u want pepperoni? Y or N?")
cheese=input("Do u want extra cheese? Y or N?")
if s=="S" :
   if pep=="Y" :
       cost=15+2
   else:
       cost=15
elif s=="M" :
   if pep=="Y" :
       cost=20+3
   else:
       cost=20
elif s=="L":
   if pep=="Y" :
       cost=25+3
   else:
       cost=25
if cheese=="Y":
   cost+=1
print(f"your final bill is {cost}")