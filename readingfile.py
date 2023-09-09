# Open our file in read mode
f = open("data/flatland01.txt", mode="r")

# Read and display text file
print(f.read())

# Close our file resource
f.close()

print("\n")

# Open our file
f = open("data/flatland01.txt", mode="r")
text = f.read()
print(text)
f.close()

# Open our file
f = open("data/flatland01.txt", mode="r")
print(f.read(100))
f.close()


def head(filepath, num_char):
    f = open(filepath, mode="r")
    output = f.read(num_char)
    f.close()
    return output


text = head("IncidentTicket.txt", 20)

print(text)

# Open file
f = open("IncidentTicket.txt", "r")  # read file in read mode.
print(f.readline())  # read first line
print(f.readline())  # read second line
print(f.readline())  # read third line
print(f.readline())  # read fourth line

f.close()


def readthefile(filepath, num_lines):
    f = open(filepath, mode="r")
    lines = ""
    for x in range(num_lines):
        lines = f.readline()
    f.close()
    return lines


# return the first 3 lines in the file
text = readthefile("IncidentTicket.txt", 3)

print(text)

# --------
f = open("data/flatland01.txt", "r")
for line in f:
    print(line)
f.close()


# Line starts with
def linestartswith(filepath, fchar):
    f = open(filepath, mode="r")
    output = ""
    for line in f:
        if fchar == line[0]:
            output += line
    return output


text = linestartswith("IncidentTicket.txt", "I")

# WRITE TO A FILE

f = open("data/test_file.txt", "a")
f.write("Hello Jesse")
f.close()

# ------------------------------------------------
customers = [
    "Ax Lodevick", "Frank Prys", "Ania Hearle",
    "Justus Bodker", "Clementius Druce", "Ganny Penwright",
    "Alick Rens", "Gwen Drewitt", "Jessie Wychard",
    "Brina Elliss", "Derril Damiral", "Jade Cutajar",
    "Brannon Goldsmith", "Valentin Salmons", "Tull Rennix",
    "Quintina Whanstall", "Lev Frunks", "Doris Heskin",
    "Idalina Moro", "Gillie Ledram"]


def writelisttwofile(inputlist, inputfilepath):
    f = open(inputfilepath, "a")
    for name in inputlist:
        name = "\n" + name
        f.write(name)
    f.close()


writelisttwofile(customers, "Customers.txt")

# -----------------------------------------------


import os

if os.path.exists("data/missing_file.txt"):
    print("The file exists.")
else:
    print("The file doesn't exist.")

# PROCESSING CSV FILES

import csv

with open('data/stocks_short.csv') as f:
    # Use the reader class under the csv module to
    # read the file using comma as the delimiter

    csv_file = csv.reader(f, delimiter=',')
    row = f.readline()  # Read the firstline of the .csv
    print(row)
    row = f.readline()  # Read the firstline of the .csv
    print(row)

#
with open('data/stocks_short.csv') as theread:
    csvfile = csv.reader(f, delimiter=', ')
    f.readline()
    for row in csvfile:
        print(row)

#

with open('data/stocks_short.csv') as f:
    csv_file = csv.reader(f, delimiter=',')

    for row in csv_file:
        print(row[0], " - ", row[1])

#

with open('data/stocks_short.csv') as f:
    csv_file = csv.reader(f, delimiter=',')
    f.readline()

    sum = 0
    count = 0

    for row in csv_file:
        sum += float(row[1])
        count += 1

    print(sum / count)

#

with open('data/stocks_short.csv') as f:
    csv_file = csv.DictReader(f, delimiter=',')

    # csv_file is an iterable object that we can iterate on using a for loop
    for row in csv_file:
        print(row)

#

with open('data/stocks.csv') as f:
    csv_file = csv.DictReader(f, delimiter=',')
    vol = None
    max_vol = None

    for row in csv_file:
        vol = int(row["Volume"])
        if max_vol == None or max_vol < vol:
            max_vol = vol

    print(max_vol)


#

def read_csv(filepath, delimiter=","):
    import csv
    dataset = list()
    with open(filepath) as f:
        # use the DictReader function of the csv module to
        # read the file using the same delimiter
        csv_file = csv.DictReader(f, delimiter=delimiter)

        # csv_file is an iterable object that we can iterate on using a for loop
        for row in csv_file:
            dataset.append(row)

    return dataset


dataset = read_csv("data/stocks_short.csv")
print(len(dataset))  # number of rows in the dataset
print("----")
print(dataset[0])  # print first row in the dataset
print("----")
print(dataset)


#

def read_csv(filepath, delimiter=","):
    import csv
    dataset = list()
    with open(filepath) as f:
        csv_file = csv.DictReader(f, delimiter=delimiter)
        for row in csv_file:
            dataset.append(row)
    return dataset


dataset = read_csv("data/stocks.csv")
total = 0
for row in dataset:
    total += float(row["Close"])
    print("Close: " + str(row["Close"]))
    print("----")
    print(total)

#

row_1 = ["employee_id", "first_name", "last_name"]  # header row
row_2 = ["EMP2345235636", "robert", "balti"]  # first row
row_3 = ["EMP2498799899", "mark", "smith"]  # second row
row_4 = ["EMP2498989890", "mary", "caldwell"]  # third row

with open('data/employee.csv', 'w') as csv_file:  # open file in write mode
    # use the writer class to create a writer object
    # that we will use to write data into the file
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(row_1)  # writing the header row
    writer.writerow(row_2)  # writing the first row
    writer.writerow(row_3)  # writing the second row
    writer.writerow(row_4)  # writing the third row

f = open('data/employee.csv', 'r')
print(f.read())
f.close()

#

with open('user_input.csv', 'w', newline='') as csv_file:
    while True:
        user_input = input("Please enter text to add to file [enter quit to exit]: ")
        if user_input.lower() == 'quit':
            break
        else:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([user_input])

f = open('user_input.csv', 'r')
print(f.read())
f.close()

#

row_1 = ["EMP4564576566", "rodney", "evans"]  # first row
row_2 = ["EMP9807976875", "lesa", "clapper"]  # second row
row_3 = ["EMP4564564566", "mario", "cruz"]  # third row

# open file in append mode, which will add the data at the end of the file
with open('data/employee.csv', 'a') as csv_file:
    # use the writer class to create a writer object
    # that we will use to write data into the file
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(row_1)  # writing the first row
    writer.writerow(row_2)  # writing the second row
    writer.writerow(row_3)  # writing the third row

f = open('data/employee.csv', 'r')
print(f.read())
f.close()

#

while True:
    if os.path.exists('data/user_input.csv'):
        user_prompt = input("The file exists, what data would you like to append? [type quit to exit]: ")
        if user_prompt.lower() == 'quit':
            break
        else:
            with open('data/user_input.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow([user_prompt])  # writing the first row
    else:
        f = open('data/user_input.csv', 'w')
        print("The file data/user_input.csv does not exist. It has been created.")

f = open('data/user_input.csv', 'r')
print(f.read())
f.close()

#

dataset = [["EMP9807976877", "vicki", "gallegos"], ["EMP9807976872", "hector", "bowen"],
           ["EMP4564564598", "cassandra", "wang"]]

# open file in append mode, which will add the data at the end of the file

with open('data/employee.csv', 'a') as csv_file:
    # use the writer class to create a writer object
    # that we will use to write data into the file
    writer = csv.writer(csv_file, delimiter=',')
    # write multiple rows at once using writerows
    writer.writerows(dataset)

f = open('data/employee.csv', 'r')
print(f.read())
f.close()

#

# create three rows of data; item order is not important because each dictionary
# uses keys to identify each value
row_1 = {"employee_id": "EMP4564576566", "first_name": "rodney", "last_name": "evans"}
row_2 = {"first_name": "lesa", "last_name": "clapper", "employee_id": "EMP9807976875"}
row_3 = {"employee_id": "EMP4564564566", "last_name": "cruz", "first_name": "mario"}

fieldnames = ["employee_id", "first_name", "last_name"]

with open('data/employee.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(row_1)  # write the first row
    writer.writerow(row_2)  # write the second row
    writer.writerow(row_3)  # writethe third row

f = open('data/employee.csv', 'r')
print(f.read())
f.close()

#

count = 0
filename = 'data/transactions.csv'
dataset = {}

trans_date = input("Please the transaction date: ")
customer = input("Enter the customer: ")
merchant = input("Enter the merchant name: ")
total = input("Enter the total of the transaction: ")

input_data = {"trans_date": trans_date, "customer": customer,
              "merchant": merchant, "total": total}
print(input_data)

fieldnames = ["trans_date", "customer", "merchant", "total"]

# Open file in append mode, which will add the data at the
# end of the  file
if os.path.exists(filename):
    with open(filename, 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(input_data)
else:
    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(input_data)

# Print out the data in the file:
f = open('data/transactions.csv', 'r')
print(f.read())
f.close()

# PROCESSING JSON FILES


# Create a list of dictionaries
import json


data = []
data.append({"name":"Andre Richards","DOB":"10/10/1979"})
data.append({"name":"Melinda Jefferson","DOB":"12/31/1979"})

with open('data/person.json', 'w') as outfile:
    json.dump(data, outfile)

# Print the file’s contents
f = open('data/person.json', 'r')
print(f.read())
f.close()



#

json_dict = {
    "first_name": "Robert",
    "last_name": "Balti",
    "role": ["Manager", "Lead Developer"],
    "age": 34
}

# convert a dictionary into a string object that we can display.
json_data = json.dumps(json_dict)

print(json_dict)       # dict
print(type(json_dict))

print(json_data)       # string
print(type(json_data))



#

json_dict = {
    "first_name": "Robert",
    "last_name": "Balti",
    "role": ["Manager", "Lead Developer"],
    "age": 34
}

json_data = json.dumps(json_dict,indent = 4)

print(json_data)
print(type(json_data))


#

json_dict = {
    "first_name": "Robert",
    "last_name": "Balti",
    "role": ["Manager", "Lead Developer"],
    "age": 34
}

# Convert a dictionary into a JSON formatted string object.
json_data = json.dumps(json_dict)
print(json_data)
print(type(json_data)) # string

# Convert a JSON encoded object into a python dictionary.
python_dict = json.loads(json_data)
print(python_dict)
print(type(python_dict)) # dict


#

x = """{
    "Name": "Cheyanne Kemp",
    "Contact Number": 7867567898,
    "Email": "ckemp@gmail.com",
    "Services":["Checking", "Savings", "Auto Loan"]
}"""

user_data = json.loads(x)
print(user_data['Email'])



#

with open('data/prize.json','r') as jsonfile:
    # use the json module with the load function
    # to read the entire content of the json file
    data = json.load(jsonfile)

# iterate through the file and display each json object separately.
for k in data['prizes']:
    print(k)


#

filename = 'data/bank_transactions.json'

with open(filename,'r') as jsonfile:
  data = json.load(jsonfile)

for each in data:
  if each['WITHDRAWAL AMT'] != '':
    val = float(each['WITHDRAWAL AMT'])
    if val > 650000:
      print(each['Account No'], "===>", val)



#

filename = 'data/bank_transactions.json'

with open(filename,'r') as jsonfile:
  data = json.load(jsonfile)

total = 0
total_balance = 0

for each in data:
  if each['WITHDRAWAL AMT'] != '':
    total +=  float(each['WITHDRAWAL AMT'])
  if each['BALANCE AMT'] != '':
    total_balance +=  float(each['BALANCE AMT'])

print("Total Withdrawals: ", total)
print("Total of Balances: ", total_balance)


#

from pprint import pprint

with open('data/prize.json','r') as jsonfile:
    data = json.load(jsonfile) # load the json content and serialize it.
print(type(data)) #dict
pprint(data)      # print the entire file content. 






