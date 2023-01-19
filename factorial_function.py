def fact (n):
    i = f = 1
    while i <= n:
        f = f * i
        i = i + 1
    print("Factorial of", n, " is", f)
print("/// Factorial of Number /// \n")
k=int(input("Enter the Number :\n"))
fact(k)