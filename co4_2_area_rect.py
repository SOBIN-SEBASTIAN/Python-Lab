class rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*(self.length+self.width)

l1=float(input(" Enter the Length of rectangle\n"))
w1=float(input("Enter the width of Rectangle \n"))
l2=float(input(" Enter the Length of rectangle\n"))
w2=float(input("Enter the width of Rectangle \n"))

rect1= rectangle(l1, w1)
rect2=rectangle(l2,w2)
print("Area of rectangle 1 is {} and perimeter is {}".format(rect1.area(),rect1.perimeter()))
print("Area of rectangle 2 is {} and perimeter is {}".format(rect2.area(),rect2.perimeter()))
print(rect1.area()>rect2.area())