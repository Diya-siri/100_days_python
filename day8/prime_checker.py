n=int(input("Enter a number to check if it is prime or not "))
def prime(num):
    flag=0
    if num==0 or num==1:
        flag=1
    for i in range(2,num):
        if num%i==0:
            flag=1
    if flag==1:
        print("Not a prime number" )
    if flag==0:
        print("It is a Prime number")
    
prime(num=n)
