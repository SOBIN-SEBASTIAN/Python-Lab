class rectangle():
    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return 2*(self.__length+self.__width)
    def __lt__(self,other):
        if self.area<other.area:

l1=float(input(" Enter the Length of rectangle\n"))
w1=float(input("Enter the width of Rectangle \n"))
l2=float(input(" Enter the Length of rectangle\n"))
w2=float(input("Enter the width of Rectangle \n"))

rect1= rectangle(l1, w1)
rect2=rectangle(l2,w2)
print("Area of rectangle 1 is {} and perimeter is {}".format(rect1.area(),rect1.perimeter()))
print("Area of rectangle 2 is {} and perimeter is {}".format(rect2.area(),rect2.perimeter()))
print(rect1.area()>rect2.area())