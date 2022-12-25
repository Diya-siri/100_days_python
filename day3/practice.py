# #3.1
# n=int(input("Enter the number"))
# if n%2==0 :
#     print("even number")
# else :
#     print("odd number")

#3.2
# h=float(input("Enter your height"))
# w=float(input("Enter your weight"))
# b=round(w/(h*h))
# print()
# if(b<18.5) :
#     print(f"your bmi is {b}, you are underweight")
# elif(b>18.5 and b<25) :
#     print(f"your bmi is {b}, you are a normal weight")
# elif(b>25 and b<30) :
#     print(f"your bmi is {b}, you are overweight")
# elif(b>30 and b<35) :
#     print(f"your bmi is {b}, you are obese")
# else :
#     print(f"your bmi is {b}, you are clinically obese")

#3.3
# year=int(input("Enter the year"))
# if (year%4)==0 :
#     if(year%100)==0 :
#         if(year%400)==0 :
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year") 


#3.4
# print("welcome to python pizza deliveries")
# s=input("What size of pizza do u want? S,M,OR L?")
# pep=input("Do u want pepperoni? Y or N?")
# cheese=input("Do u want extra cheese? Y or N?")
# if s=="S" :
#     if pep=="Y" :
#         cost=15+2
#     else:
#         cost=15
# elif s=="M" :
#     if pep=="Y" :
#         cost=20+3
#     else:
#         cost=20
# elif s=="L":
#     if pep=="Y" :
#         cost=25+3
#     else:
#         cost=25
# if cheese=="Y":
#     cost+=1
# print(f"your final bill is {cost}")



#3.5
print("welcome to love calculator")
n1=input("enter your name \n")
n2=input("enter their name \n")
n=n1+n2
name=n.lower()
r=name.count("t")+name.count("r")+name.count("u")+name.count("e")
s=name.count("l")+name.count("o")+name.count("v")+name.count("e")
print(f"{r} {s}")
score=str(r)+str(s)
fscore=int(score)
if fscore<10 or fscore>90:
    print(f"Your score is {fscore}, you go together like coke and mentos.")
elif fscore>=40 and fscore<=50 :
    print(f"Your score is {fscore},you are alright together.")
else:
    print(f"Your score is {fscore}")



    
