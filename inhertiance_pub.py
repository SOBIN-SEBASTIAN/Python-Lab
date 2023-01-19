class publisher:
    def get_pub_name(self):
        self.__pubname=input("Enter the Publisher name")
    def print_pub(self):
        print("Publisher :" ,self.__pubname)
class book(publisher):
    def get_book(self):
        self.__title=input("Enter the title of book")
        self.__author=input("Enter the author")
    def print_book(self):
        print("Title     :",self.__title)
        print("Author    :",self.__author)
class python(book):
    def get_python(self):
        self.__price=input("Enter the price")
        self.__noofpage=input("Enter the No :of pages:")
    def print_python(self):
        print("Price      :",self.__price)
        print("No.Of Pages:",self.__noofpage)

s=python()
s.get_pub_name()
s.get_book()
s.get_python()
s.print_pub()
s.print_book()
s.print_python()
