#read specific columns
import csv
columns_to_read = [0,2] #selecting 0th and 2nd columns
#open csv file
with open('book.csv','r')as file:
    #creating csv reader
    clnm_reader=csv.reader(file)

    for row in  clnm_reader:#to iteate over the rows in csv file
        #print the contents of  specified columns
        print([ row[i] for i in columns_to_read ])