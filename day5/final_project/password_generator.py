import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
sym=['!','#','$','%','&','(',')','*','+']
print("Welcome to pypassword genertor\n")
l=int(input("enter the no of letters to be included in your password??\n"))
s=int(input("enter the no of symbols in your password?\n"))
n=int(input("enter the no of numbers in your password?\n"))
list1=list()
listf=list()
for i in range(0,l):
    rand=random.randint(0,len(letters)-1)
    list1.append(letters[rand])
for i in range(0,s):
    rand1=random.randint(0,len(sym)-1)
    list1.append(sym[rand1])
for i in range(0,n):
    rand2=random.randint(0,len(num)-1)
    list1.append(num[rand2])
listf=(random.sample(list1,(l+s+n)))
print("Your password is = ")
print("".join(listf))
    


    
