n=input("Enter the COLOURS in list 1 separated by comma ::\n")
l=input("Enter the COLOURS in list 2 separated by comma ::\n")
cl1=n.split(',')
cl2=l.split(',')
st1=set(cl1)
st2=set(cl2)
print("Colours from List 1 not contained in List 2\n",st1-st2)