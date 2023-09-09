# ORDER CLASS
from menu import Jollof, Drink, Side


class JollofOrder:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def get_price(self):
        price = 0.0
        for item in self.items:
            price = price + item.get_price()
        return price

    def __str__(self):
        s = [str(item) for item in self.items]
        return "\n".join(s)

    def display(self):
        print("==============================")
        print('Here is a summary of your order please')
        print("Order for " + self.name)
        print("Here is a list of items in the order")

        for item in self.items:
            print("--------------------")
            print(str(item))
        print("------------------------")
        print("Total Order Amount : $" + str(self.get_price()))
        print("==============================================")


# Create instances of the class
order1 = JollofOrder("Jesse's Order")

# adding items to the order
order1.add_items(Jollof("Spicy Jollof Rice", 9.99))
order1.add_items(Drink("Orange Juice", 8, 2.49))
order1.add_items(Side("Onion Rings", 3.29))

order1.display()
order1.display()

