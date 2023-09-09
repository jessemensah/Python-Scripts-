
# MENU
class Food:
    def __init__(self, foodname, foodprice):
        self.name = foodname
        self.price = foodprice

    # string representation of the class
    def __str__(self):
        return "Item: " + self.name + "\n" + "Price: $" + str(self.price) + "\n"

    def get_price(self):
        return self.price


# INSTANCES OF THIS CLASS IS ABOVE
# CAN BE ANY FOOD

pizza = Food("Mag Pizza", 10.99)
burger = Food("Beef Burger", 7.99)
banku = Food("Banku", 15.99)

print(pizza)
print(burger)
print(banku)


class Jollof(Food):
    def __init__(self, jollofname, jollofprice):
        super(Jollof, self).__init__(jollofname, jollofprice)
        self.dressings = []

    def add_dressings(self, dressing):
        if dressing not in self.dressings:
            self.dressings.append(dressing)

    def __str__(self):
        s = super(Jollof, self).__str__()
        s = s + "Dressings:" + ", ".join(self.dressings)
        return s


# creating instances of the Jollof Class
spicy_jollof = Jollof("Spicy Jollof Rice", 9.99)
vegetable_jollof = Jollof("Vegetable Jollof Rice", 8.99)

# add dressings to the jollof rice
spicy_jollof.add_dressings("Hot Pepper Sauce")
vegetable_jollof.add_dressings("Cucumber Slices")

print(spicy_jollof)


class Drink(Food):
    def __init__(self, drinkname, drinksize, drinkprice):
        super(Drink, self).__init__(drinkname, drinkprice)
        self.drinksize = drinksize

    def __str__(self):
        s = super(Drink, self).__str__()
        s = s + "Size: " + str(self.drinksize) + "oz"
        return s


cola = Drink("Cola", 12, 1.99)
orange_juice = Drink("Orange Juice", 8, 2.49)
water = Drink("Water", 16, 0.99)
print(cola)
print(orange_juice)
print(water)


class Side(Food):
    def __init__(self, sidename, sideprice):
        super(Side, self).__init__(sidename, sideprice)


# Assuming you have already defined the Food and Side classes as described
# Creating instances of the Side class

fries = Side("French Fries", 2.49)
coleslaw = Side("Coleslaw", 1.99)
onion_rings = Side("Onion Rings", 3.29)

# Printing the string representation of the instances
print(fries)
print(coleslaw)
print(onion_rings)


class Combo(Food):
    def __init__(self, foodname, thejollof, thedrink, theside, discount):
        self.name = foodname
        self.Jollof = thejollof
        self.Drink = thedrink
        self.Side = theside
        self.discount = discount
        self.price = self.Jollof.get_price() + self.Drink.get_price() + self.Side.get_price() - self.discount

    def __str__(self):
        s = ""
        s = s + "Combo: " + self.name + "\n"
        s = s + str(self.Jollof) + "\n" + str(self.Drink) + "\n" + str(self.Side) + "\n"
        s = s + "Combo Price Before Discount: $" + str(self.Jollof.get_price() + self.Drink.get_price()
                                                       + self.Side.get_price()) + "\n"
        s = s + "Discount: $" + str(self.discount) + "\n"
        s = s + "Combo Price After Discount: $" + str(self.price) + "\n"
        return s


# Create instances of the Food class to use as components of the combo
jollof = Food("Jollof Rice", 5.99)
drink = Drink("Cola", 12, 1.99)
side = Side("French Fries", 2.49)

# Creating instances of the Combo class
combo1 = Combo("Combo 1", jollof, drink, side, 1.50)
combo2 = Combo("Combo 2", jollof, drink, side, 2.00)
print(combo1)
print(combo2)


