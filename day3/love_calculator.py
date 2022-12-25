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
