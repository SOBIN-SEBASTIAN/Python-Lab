class time:
    def __init__(self ,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def __add__(self, other):
        return "time is:"+ str(self.__hour + other.__hour)+ ":"+str(self.__minute + other.__minute)+":"+str(self.__second+other.__second)
    def __lt__(self,other):
        if(self.__hour<other.__hour):
            return ("True")
        elif(self.__hour==other.__hour):
            if(self.__minute<other.__minute):
                return ("True")
            elif (self.__minute == other.__minute):
                if (self.__second < other.__second):
                    return ("True")
                else:
                    return ("False")
        else:
            return("False")


h=int(input("Enter the hour"))
m=int(input("enter the minute"))
s=int(input("Enter the Second"))
h1= int(input("Enter the hour"))
m1 = int(input("enter the minute"))
s1= int(input("Enter the Second"))
t1=time(h,m,s)
t2=time(h1,m1,s1)
print(t1+t2)
print(" if T1 <T2 :-")
print(t1<t2)
