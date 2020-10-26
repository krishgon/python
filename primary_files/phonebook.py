import csv
from sys import argv

fields = []
rows = []

# name = input("Name: ")
# number = input("Number: ")
# with open(argv[1], "a") as file:
#     writer = csv.writer(file)
#     writer.writerow((name,number))
    
with open("phonebook.csv",'r') as cfile:
    reader = csv.reader(cfile)
    fields = next(reader)

    for row in reader:
        rows.append(row)
        # print(row)    

    print(rows)
    print(fields[1:])
    print("Total rows are", reader.line_num)

# print("field names are: ")
# for field in fields: print(field)


for col in rows:
    print("name: ", col[0], end="   ")
    print("num: ", col[1])
