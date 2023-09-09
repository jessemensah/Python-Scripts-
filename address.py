
# Name => First LastName
# Date Created => Current Date
# Purpose => code along with python course

user_address = input("Enter an address (e.g. 60 Barnsley Street): ")

if user_address.strip():
    print("Your address is " + user_address + ".")
    split_address = user_address.split()
    print("Your house number is " + split_address[0] + ".")
    print("Your street is " + " ".join(split_address[1:])+".")

