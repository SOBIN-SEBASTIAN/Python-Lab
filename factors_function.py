def factor(k):
    print("Factors of : ", k)
    for i in range(1, k+1):
        if k % i == 0:
            print(" ",i)
print("All Factors of a Number \n")
n=int(input("Enter the number: \n"))
factor(n)