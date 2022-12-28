height=input("Input a list of students").split()
sum=0
for i in range (0,len(height)):
    height[i]=int(height[i])
    sum=sum+height[i]; 
    avg=sum/len(height)
print(round(avg))