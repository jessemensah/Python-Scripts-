
# WRITE THESE IN NORMAL FUNCTIONS
# WHY USE LAMBDA OVER FUNCTIONS
x = lambda a: a + 10
print(x(5))


#
x = lambda a : a ** 2
print(x(10))


#

x = lambda a, b : a * b
print(x(5, 6))

#

x = lambda a, b : a / b
print(x(6, 5))

y = lambda a, b : a / b
print(y(5, 6))


#

PerPerson = lambda items, people : items / people
print(PerPerson(20, 5))  # Correct
print(PerPerson(5, 20))  # Wrong


#

x = lambda a, b, c: a + " " + b + " " + c
print(x("This", "String", "Is Concatenated."))


#

def myfunc(n):
    return lambda a : a * n

doubler = myfunc(2) # we set the value of n

print(doubler(11)) # we set the value of a



#

def pow_n(n):
  return lambda a: a ** n

pow_2 = pow_n(2)
print(pow_2(6))


#

def to_upper_case(s):
    return str(s).upper()

names=['haythem','mike','james']
print(names)

names_upper = map(to_upper_case, names) # apply to_upper_case function to each element in names
print(type(names_upper))

names_upper_list = list(names_upper) # convert the names_upper map object to a python list.
print(names_upper_list)
print(type(names_upper_list))




#

def fromCSV(path,delimiter,quotechar):
    import csv  # import the csv module
    data=list() # convert the CSV data into a list
    with open(path, newline='') as csvfile: # open the file
        filecontent = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
        # access the content of the file
        for row in filecontent:  # iterate through the rows
            data.append(row)     # save each row as a dictionary
                                 # item in the data list
    return data

def extract_month(row):
    # input is the entire row of data
    # extract the month from the date field
    # add the month field to the row and return the row
    value = row['Date']
    MM=""
    # split function in python used to divide strings based on some delimiter
    a = value.split("/")
    MM = a[0]
    #implement logic here
    new_row = row.copy()
    new_row.update({'Month':MM})
    return new_row

data=fromCSV(path='data/stocks.csv',delimiter=',',quotechar='|')
print(data[0])

data_mapped = map(extract_month,data)
data_mapped_list = list(data_mapped)
print(data_mapped_list[0])


#

list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)
print(list_numbers)
print(tuple_numbers)

map_iterator = map(lambda x, y: x + y, list_numbers, tuple_numbers)

map_list= list(map_iterator) # convert map output to a list

print(map_list)


#

exchange_rate = [1.25, 2, 1.3, 1.18]
transaction_amt = (5, 6, 7, 8)
print(exchange_rate)
print(transaction_amt)

map_iterator = map(lambda x, y: x * y, exchange_rate, transaction_amt)

map_list= list(map_iterator)
print(map_list)



#

def initial_h(dataset):
    for x in dataset:
        if str.lower(x[0]) == "h": # normalize the case of the
                                   # first letter and look for 'h'
            return True
        else:
            return False

names=['Haythem','Mike','James','Helen','Mary']
print(names)

# extract the True results from the initial_h function to a new filter object
names_filtered = filter(initial_h,names)
print(type(names_filtered))

# convert the filter object to a list object
names_filtered_list = list(names_filtered)
print(type(names_filtered_list))

print(names_filtered_list)


#

def contains_e(dataset):
    if 'e' in dataset:
        return True
    else:
        return False


names = ['Haythem', 'Mike', 'James', 'Helen', 'Mary']
print(names)

names_filtered = filter(contains_e, names)
print(type(names_filtered))

names_filtered_list = list(names_filtered)
print(type(names_filtered_list))

print(names_filtered_list)


#

def fromCSV(path,delimiter,quotechar):
    import csv # import the csv module
    data=list() # any data we will read will be returned in a list
    with open(path, newline='') as csvfile: #o pen the file
        filecontent = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
        # access the content of the file
        for row in filecontent: # iterate through the rows
            data.append(row) # save the rows in the data list. Each row is a dictionary
    return data

data=fromCSV(path='data/stocks_short.csv',delimiter=',',quotechar='|')

# filter all elements in data where the open price is lower than the close price
data_filtered = filter(lambda x: x['Open'] < x['Close'], data)
print(type(data_filtered))

data_filtered_list = list(data_filtered) # convert the filter object into a list
for row in data_filtered_list: # display each element in the filtered list
    print(row)


#

from functools import reduce

list_numbers = [2, 4, 6, 8]

product = reduce(lambda x, y: x * y,list_numbers)

print(type(product))

print(product)



#


from functools import reduce

value_list = []

while True:
  user_input = input("Enter the deposits to add to the series to sum [type quit to exit]: ")
  if user_input.lower() == 'quit':
    break
  else:
    value_list.append(int(user_input))

product = reduce(lambda x, y: x + y,value_list)

print("The total is: " + str(product))



#

from functools import reduce

list_numbers = [2, 4, 6, 8]

product = reduce(lambda x, y: x * y,list_numbers,5) #initial value = 5

print(type(product))

print(product)


#

value_list = []
prev_bal = int(input("Enter your previous balance: "))

while True:
  user_input = input("Enter the deposits to add to the series to sum [type quit to exit]: ")
  if user_input.lower() == 'quit':
    break
  else:
    value_list.append(int(user_input))

product = reduce(lambda x, y: x + y,value_list,prev_bal)
print("New balance is: " + str(product))



#

list_numbers =  [1,20,300,560,4]

max_element =reduce(lambda a,b : a if a > b else b,list_numbers)

print(max_element)


#

value_list = []

while True:
  user_input = input("Enter the deposits to determine the lowest deposit [type stop to exit]: ")
  if user_input.lower() == 'stop':
    break
  else:
    value_list.append(int(user_input))

if len(value_list) > 0:
  product = reduce(lambda x, y: x if y > x else y,value_list)
else:
  product = "Nothing."

print("The values you entered were: "+ str(value_list))
print("The lowest value is: " + str(product))

















































