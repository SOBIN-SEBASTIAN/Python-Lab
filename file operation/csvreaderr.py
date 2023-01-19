#read each row from a csv  file and print  it
import csv
#open csv file
with open('infos.csv','r')as file:
    #creating csv reader
    reader=csv.reader(file)

    for row in reader:#to iteate over the rows in csv file
        #print the row as a list of string
        print(row)