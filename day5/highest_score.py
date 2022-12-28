student=input("enter the list of students").split()
max=0
for i in range(0,len(student)):
    student[i]=int(student[i])
    if student[i]>max:
        max=student[i]
print(f"Highest score is = {max}")