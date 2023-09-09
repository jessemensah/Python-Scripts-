a = 1
b = 0

try: # check that the operation is valid
  x = a/b
except ZeroDivisionError as e: # The type of exception is division by zero.
  # print a custom message when the execption occurs
  print("Oops! We cannot divide a number by zero. Try again...")
  print(format(e)) #print the exception error message



#

try:
  file_object = open("data/bank_transacts.txt",'r')
except FileNotFoundError as e:
  print("The file was not found")
  print("The error was:\n" + str(e))


#

import sys

a = 1
b = 'c'

try:
    x = a / b

# if we have a division by zero, this block will execute
except ZeroDivisionError as e:
    print("Oops, ZeroDivisionError! We cannot divide a number by zero. Try again...")

# if we have an error type (a non-valid integer such as char or string), this block will execute
except TypeError as t:
    print("Oops, TypeError! That was not a valid number. Try again...")

# the following will execute if the try statement fails with a different exception from those above
except:
    print("Unexpected error. Try again.", sys.exc_info()[0])
    raise


#

value_1 = input("Please enter a number: ")
value_2 = input("Please enter a second number [do not enter 0]: ")
try:
 x = int(value_1)/int(value_2)
 print(x)
except ValueError:
  try:
   x = float(value_1)/float(value_2)
   print(x)
  except ValueError:
   try:
    x = float(value_1)
   except:
    print("The first value entered is not an integer or a float.")
   try:
    x = float(value_2)
   except:
    print("The second value entered is not an integer or a float.")
except ZeroDivisionError:
  print("Oops, there's a zero in the second value. You can't divide by zero.")


#

a = 1
b = 'c'
try:
  x = a/b
except (ZeroDivisionError,TypeError) as e:
  print("Input is not a valid number")
  print(format(e))


#

def check_numbers(input_list):
  list = []
  for x in input_list:
    try:
      a = float(x)
      list.append(x)
    except ValueError:
      try:
        a = int(x)
        list.append(x)
      except (ValueError,ZeroDivisionError,TypeError):
        print(x + " is not a valid number.")
    except (ZeroDivisionError,TypeError) as e:
      print(x + " is not a valid number.")
  return list


input_list = [1,'c',"Haythem",23,6,6.7,-1,"String"]
print(input_list)

# check_numbers should return a list that contains the valid numbers.
numbers = check_numbers(input_list)
print(numbers)


#

import sys

b = 0
a = 1
c = 'd'

try:
    # This will throw an exception, which will trigger an except statement
    y = a / c

    # This would also throw an exception, but python ignores it because
    # it is the second exception

    x = a / b
    print(x)
    print(y)

except ZeroDivisionError as e:
    print("Oops, ZeroDivisionError! We cannot divide by zero. Try again...")

except TypeError as t:
    print("Oops, TypeError! That was not a valid number. Try again...")

except:
    print("Unexpected error. Try again.", sys.exc_info()[0])
    raise



#

print("starting...")
#raise ValueError("This is a custom ValueError")
#raise TypeError("This is a raised TypeError.")
#raise ZeroDivisionError("I raised this ZeroDivisionError.")
print("...ending")


#

try:
  f = open("data/another_file_do_not_exist.txt", "r")
  print(f.read())
  f.close()
except IOError as e:
  print("Oops! File Not Found.")
  print(format(e))


#

def read_csv(filepath,delimiter=","):
  import csv
  dataset = list()
  try:
    with open(filepath) as f: # Use open function to read the C.csv file
                              # and create a file object f

      # Use the reader function under the csv module to read the
      # file using comma a delimiter
      csv_file = csv.DictReader(f, delimiter=delimiter)

      # csv_file is an iterable object that we can iterate on using a for loop
      for row in csv_file:
        dataset.append(row)
    return dataset
  except IOError as e:
    print("Unable to access file.")

a = read_csv("file.txt","r") #do not change this line


#

try:
  f = open("data/text.txt", "r")
    # file does not exist so this line throws a FileNotFound exception
  print(len(f.read()))

# This except statement runs only if Python does not find the file
except IOError as e:
  print("Oops! File Not Found.")

# This finally statement runs whether or not Python finds
# the file
finally:
  print("Thanks for trying!")


#

class extract:
    def fromCSV(self, file_path, delimiter=",", quotechar="|"):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import csv
        dataset = list()
        with open(file_path) as f:
            csv_file = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar)
            for row in csv_file:
                dataset.append(row)
        return dataset

    def fromJSON(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path.")
        import json
        dataset = list()
        with open(file_path) as json_file:
            dataset = json.load(json_file)
        return dataset


e = extract()
dataset1 = e.fromCSV(file_path="data/missing_file.csv")
dataset2 = e.fromJSON(file_path="data/missing_file.json")






























