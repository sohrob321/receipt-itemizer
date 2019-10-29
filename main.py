class Receipt():
    def __init__(self):
        self.items = []
        self.people = {}
        self.tax = 1.0925

    def add_people(self, *args):
        for name in args:
            self.people[name] = Person(name)

    def add_item(self, i):
        self.items.append(i)

    def print_items(self):
        for person in self.people:
            print(self.people[person].name, " - ", self.people[person].total)
            print()
            self.people[person].print_items()
            print("==========")
            print()


class Person():

    def __init__(self, n):
        self.name = n
        self.total = 0
        self.purchased_items = []

    def assign_item(self, item):
        self.purchased_items.append(item)
        self.total += round(item.price, 2)
        self.total = round(self.total, 2)

    def print_items(self):
        for item in self.purchased_items:
            print(item.stringvalue)


class Item():
    rc = None

    def __init__(self, name, buyer, price, taxed=True):
        self.name = name
        self.buyer = buyer
        self.price = round(price * self.rc.tax if taxed else price, 2)
        self.taxed = taxed
        self.stringvalue = "*" + self.name + " - " + str(round(self.price, 2))
        self.rc.people[buyer].assign_item(self)

    def add_receipt(self, rc):
        self.rc = rc


rc = Receipt()
rc.add_people("Jordan", "Sohrob", "Themis", "Margaret", "Rohan")
Item.rc = rc
Item("Cold Brew", "Themis", 14.6, False)
Item("Cold Brew", "Themis", 14.6, False)
Item("Pub Mix", "Themis", 7, False)
Item("Canada Dry", "Jordan", 13)
Item("Buffalo Hood", "Sohrob", 16)
Item("Clif Builder", "Rohan", 19, False)
Item("Pretzel/3", "Jordan", 2.866666667, False)
Item("Pretzel/3", "Themis", 2.866666667, False)
Item("Pretzel/3", "Sohrob", 2.866666667, False)
Item("Cheez it", "Margaret", 8, False)
Item("Peet Coffee", "Rohan", 14.5, False)
Item("Stroopwafel", "Margaret", 4, False)
Item("Stroopwafel", "Rohan", 4, False)
Item("Chewy Bars", "Margaret", 9, False)
Item("Go Macro", "Sohrob", 20, False)
Item("Fruit Bar", "Sohrob", 11, False)
Item("Biscoff", "Rohan", 4.8, False)
Item("Deluxe Bunch", "Rohan" , 10)

rc.print_items()


'''
# venmo api

You have a receipt that has items with prices and names and a tax/not taxed checkbox.
item_name, price, tax/untaxed, who's paying for it.

Create Items

'''


