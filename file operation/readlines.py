# program to read file and store it into a list
# using read lines

# without strip
read_file=open('newtext.txt','r')
file_lines=read_file.readlines()
print("File contents :-")
print(file_lines)

# using strip
print("\n")
print("After removing New line character form File Content ")
file_lines=[Y.strip() for Y in file_lines ]
print([Y.strip() for Y in file_lines ])
read_file.close()