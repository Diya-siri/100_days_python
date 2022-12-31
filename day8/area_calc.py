import math
h=int(input("Enter the height of the wall "))
w=int(input("Enter the width of the wall "))
coverage=5
def paint_calc(height,width,cover):
    a=(height*width)
    n=math.ceil(a/cover)
    print(f"You,ll need {n} cans of paint.")
paint_calc(height=h,width=w,cover=coverage)

