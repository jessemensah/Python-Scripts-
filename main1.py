from menu import Jollof, Drink, Side, Combo
from order import JollofOrder

JOLLOFPRICE = 10.00
JOLLOFDRESSING = ["tomatoes", "lettuce", "cream"]

DRINKS = ["fanta", "coca cola", "pepsi"]
DRINKSIZE = [12, 16, 20]
DRINKPRICE = [1.00, 2.00, 3.00]

SIDEPRICE = 3.00
SIDES = ["Fries", "small chops", "salad"]

COMBODISCOUNT = 2.00


def getjolloforder():
    jollof = Jollof("Jollof", JOLLOFPRICE)
    questiontocustomer = input("Do you want dressings on your Jollof? (y for yes) ")
    if questiontocustomer.lower() == "y":
        for dressing in JOLLOFDRESSING:
            anotherquestiontocustomer = input("Do you want " + str(dressing) + "? (y/n)")
            if anotherquestiontocustomer.lower() == "y":
                jollof.add_dressings(dressing)
    return jollof


def getdrinkorder():
    print("These are the available drinks")
    print(DRINKS)
    print("These are the available sizes")
    print(DRINKSIZE)
    customerchoice = False
    drinkname = None
    drinksize = None
    drinkprice = None
    while customerchoice == False:
        questiontocustomer = input("What drink do you want? ")
        if questiontocustomer.lower() in DRINKS:
            customerchoice = True
            drinkname = questiontocustomer.lower()
        else:
            print("Please enter a valid drink.")
    customerchoice = False
    while customerchoice == False:
        questiontocustomer = input("What size do you want? " + str(DRINKSIZE) + ": ")
        if int(questiontocustomer) in DRINKS:
            customerchoice = True
            drinksize = int(questiontocustomer)
        else:
            print("Please enter a valid size")

    drinkprice = DRINKPRICE[DRINKS.index(drinksize)]
    drink = Drink(drinkname, drinksize, drinkprice)
    return drink


def getsideorder():
    print("These are the available sides: ")
    print(SIDES)
    customerchoice = False
    sidename = None
    while customerchoice == False:
        questiontocustomer = input("What do you want? ")
        if questiontocustomer.lower() in SIDES:
            customerchoice = True
            sidename = questiontocustomer.lower()
        else:
            print("Please enter a valid size")
    side = Side(sidename, SIDEPRICE)
    return side


# GET COMBO ORDER
def getcomboorder():
    print("Lets get you a Jollof Combo meal!")
    print("First, lets order the jollof for your combo.")
    jollof = getjolloforder()
    print("Now lets order the drink for your combo.")
    drink = getdrinkorder()
    print("Finally, lets order the side for your combo")
    side = getsideorder()
    combo = Combo("Combo", jollof, drink, side, COMBODISCOUNT)
    return combo


# ORDER ONCE
def orderonce():
    possibleoptions = [1, 2, 3, 4]
    print("Type 1 for the Jollof.")
    print("Type 2 for the Drink.")
    print("Type 3 for a Side.")
    print("Type 4 for a Combo.")
    customerchoice = None
    while customerchoice == None:
        questiontocustomer = input("Please enter your choice: ")
        if int(questiontocustomer) in possibleoptions:
            customerchoice = int(questiontocustomer)
    item = None
    if customerchoice == 1:
        item = getjolloforder()
    elif customerchoice == 2:
        item = getdrinkorder()
    elif customerchoice == 3:
        item = getdrinkorder()
    elif customerchoice == 4:
        item = getcomboorder()
    return item


def ordermany():
    print("Welcome to Cool Corner Shop!")
    questioncustomer = input("May I have your name for order")
    order = JollofOrder()
    print("Let's get your order in!")
    done = False
    while done == False:
        item = orderonce()
        order.add_items(item)
        questioncustomer = input("Do you need more items? (Enter n to stop) ")
        if questioncustomer.lower() == "n":
            done = True
    return order


clientorder = ordermany()
clientorder.display()














