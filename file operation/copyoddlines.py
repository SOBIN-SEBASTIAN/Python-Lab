#Program to copy odd lines of one file  to another
in_file=open("file_01.txt")
out_file=open("write_data.txt",'w')

#copying data fromfirst file
copy_data=in_file.readlines()
print("\n File_01 Content is:-")
print(copy_data,"\n")

for j in range(0,len(copy_data)):
    if j%2==0:
        out_file.write(copy_data[j])
    else:
        pass
#closing file after writing
out_file.close()
#opening file after writing
out_file=open("write_data.txt")
print("\n Odd Lines are:")
#
print(out_file.read())
in_file.close()
out_file.close()