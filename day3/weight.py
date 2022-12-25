h=float(input("Enter your height"))
w=float(input("Enter your weight"))
b=round(w/(h*h))
print()
if(b<18.5) :
   print(f"your bmi is {b}, you are underweight")
elif(b>18.5 and b<25) :
   print(f"your bmi is {b}, you are a normal weight")
elif(b>25 and b<30) :
   print(f"your bmi is {b}, you are overweight")
elif(b>30 and b<35) :
   print(f"your bmi is {b}, you are obese")
else :
   print(f"your bmi is {b}, you are clinically obese")