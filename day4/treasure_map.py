row1=["⬜️","⬜️","⬜️"]
row2=["⬜️","⬜️","⬜️"]
row3=["⬜️","⬜️","⬜️"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
pos=input("Where do u want the treasure?? ")
h=int(pos[0])
v=int(pos[1])
map[v-1][h-1]="X"
print(f"{row1}\n{row2}\n{row3}")

