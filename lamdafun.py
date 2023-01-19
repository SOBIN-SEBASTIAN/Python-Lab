a_rect = lambda l, w: l * w
a_square=lambda n: n*n
a_tri = lambda b,h,c: b*h/c
ch=0
while ch==0:
    print("/// Find Area ///\n 1. Rectangle \n 2. Square \n 3. Triangle\n")
    ch=int(input("choose your operation \n"))
    if ch==1:
        a = int(input("Enter the width \n"))
        b = int(input("enter teh height \n"))
        print("Area of rectangle : ",a_rect(a, b))
    elif ch==2:
        a = int(input("Enter the side of square: \n"))
        print("Area of Square: ",a_square(a))
    elif ch==3:
        c = 2
        b = int(input("Base of triangle: \n"))
        h = int(input("height of triangle : \n"))
        print("Area of Triangle : ",a_tri(b, h, c))
    ch=int(input("Do you want to continue \n Press 0 to Continue \n press any key to exit"))