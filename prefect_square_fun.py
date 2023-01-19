def prefect (s,e):
    ls = []
    for i in range(s, e):
        for j in range(1, i):
            if j * j == i:
                ls.append(i)
    return (ls)
k= int(input("enter the 4 digit Starting range :\n"))
l=int(input("enter the 4 digit Ending range :\n"))
e=prefect(k,l)
print("Prefect Square between",k,"and",l,": \n",e)