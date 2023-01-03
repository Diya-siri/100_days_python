from art import logo
from os import system


def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations={"+":add,"-":sub,"*":mul,"/":div}
def calculator(): 
    print(logo)
    num1=float(input("Whats the first number?"))

    for i in operations:
        print(i)

    flag=True
    while flag:

            
        op_sym=input("Pick an opeartional symbol from above: ")

        num2=float(input("Whats the second number?"))
        calculation=operations[op_sym]
        answer=calculation(num1,num2)
        print(f"{num1} {op_sym} {num2} = {answer}")

        if input(f"type 'y' to continue with {answer},or type 'n' to exit:").lower()=="y":
            num1=answer
        else:
            flag=False
            system('cls')
            calculator()
calculator()
    # op_sym=input("Pick another operation")
    # num3=int (input("Whats the next no?: "))
    # calculation=operations[op_sym]
    # second_answer=calculation(first_answer,num3)
    # print(f"{first_answer} {op_sym} {num3} = {second_answer}")


