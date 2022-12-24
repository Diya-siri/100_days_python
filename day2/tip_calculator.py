# print("welcome to the tip calculator" )
# bill=input("What was the total bill ")
# bill1=float(bill)
# per=input("What percentage tip would you like to give? 10, 12, or 15?")
# per1=int(per)
# split=input("How many people to split the bill? ")
# split1=int(split)
# r=(per1/100)*bill1
# fbill=bill1+r
# res=round(fbill/split1,2)
# print(f"Each person should pay: {res}")


print("welcome to the tip calculator" )
bill=float(input("What was the total bill $"))
#bill1=float(bill)
per=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
#per1=int(per)
split=int(input("How many people to split the bill? "))
#split1=int(split)
r=(per/100)*bill
fbill=bill+r
res=round(fbill/split,2)
print(f"Each person should pay: ${res}")
