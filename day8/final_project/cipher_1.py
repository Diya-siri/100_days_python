from logo import art
print(art)
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dir=input("Type 'encode' to encrypt or 'decode' to decrypt\n")
def encrypt(text,shift):
    cipher=""
    for i in text:
        x=alphabets.index(i)
        y=x+shift
        letter=alphabets[y]
        cipher+=letter
    print(f"The encoded text is= {cipher}\n")
def decrypt(text,shift):
    plain=""
    for j in text:
        x=alphabets.index(j)
        y=x-shift
        letter=alphabets[y]
        plain+=letter
    print(f"The decoded text is= {plain}\n")
if dir=='encode':
    text=input("Enter your message\n").lower()
    shift=int(input("Enter the shift number\n"))
    encrypt(text,shift)
if dir=='decode':
    cipher=input("Enter the text to decode\n").lower()
    shift=int(input("Enter the shift number\n"))
    decrypt(cipher,shift)

m=True
while m is True:

    flag=input("Type 'yes' to continue to 'no' oterwise\n")
    if flag=='yes':
        dir=input("Type 'encode' to encrypt or 'decode' to decrypt\n")
        if dir=='decode':
            cipher=input("Enter the text to decode\n").lower()
            shift=int(input("Enter the shift number\n"))
            decrypt(cipher,shift)
        elif dir=='encode':
            text=input("Enter your message\n").lower()
            shift=int(input("Enter the shift number\n"))
            encrypt(text,shift)
        else:
            print("Wrong input!")

    elif flag=='no':
        m=False
        print("Goodbye")
    else:
        print("Wrong input!")
    



    



