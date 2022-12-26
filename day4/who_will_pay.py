import random
names=input("Give names, separated by comma. ")
name=names.split(",")
n=len(name)
#print(n)
m=random.randint(0,n-1)
print(f"{name[m]} should pay the bill!")


