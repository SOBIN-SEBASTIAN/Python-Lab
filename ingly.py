s=str(input("Enter String : \n"))
if len(s) > 2:
    if s[-3:] == 'ing':
      s+= 'ly'
    else:
      s+= 'ing'
print(s)