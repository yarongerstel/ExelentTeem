import datetime


class Item:

    def __init__(self, name="item", price=0, amount_in=0, amount_out=0):
        self._name = name
        self._price = price
        self._amount_in = amount_in
        self._amount_out = amount_out
        self.rep = []

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_amount_in(self):
        return self._amount_in

    def get_amount_out(self):
        return self._amount_out

    def refill_out(self, amount):
        if self._amount_in >= amount:
            self._amount_out += amount
            self._amount_in -= amount
            self.rep.append([datetime.datetime.now(), self._name, 0, "refill_out"])
        else:
            n = self.get_name()
            print("You do not have enough" + n + " in the warehouse")

    def refill_in(self, amount, balance):
        while self._amount_in < amount and self.get_price() / 2 <= balance:
            self._amount_in += 1
            balance -= self.get_price() / 2
            self.rep.append([datetime.datetime.now(), self._name, (-self._price / 2), "refill_in"])
        return balance

    def buy_one(self):
        if self._amount_out > 0:
            self._amount_out -= 1
            self.rep.append([datetime.datetime.now(), self._name, self._price, "buy"])
        else:
            print("The product is out of stock, try filling it out of the warehouse")


class Shop:
    def __init__(self, list_items=None, balance=0):
        self._balance = balance
        self._list_items = list_items

    def refill(self):
        max_on_the_shelf = 10
        for i in self._list_items:
            if i.get_amount_in() > 0 and i.get_amount_out() < max_on_the_shelf:
                # There is enough to fill the entire quantity on the shelf
                if (max_on_the_shelf - i.get_amount_out()) <= i.get_amount_in():
                    i.refill_out(max_on_the_shelf - i.get_amount_out())
                else:
                    i.refill_out(i.get_amount_in())

    def checkout(self, lis):
        s = 0
        for i in lis:
            for j in self._list_items:
                if i == j.get_name():
                    s += j.get_price()
        return s

    def purchase(self, lis, money):
        s = 0
        if self.checkout(lis) <= money:
            for i in lis:
                for j in self._list_items:
                    if i == j.get_name() and j.get_amount_out() > 0:
                        s += j.get_price()
                        j.buy_one()
            self._balance += s
            print("Your surplus:\t", money - s)
        else:
            print("The purchase was not made, there is not enough money")
        return money - s

    def restock(self):
        max_on_the_warehouse = 50
        for i in self._list_items:
            if self._balance >= i.get_price() / 2:
                self._balance = i.refill_in(max_on_the_warehouse, self._balance)

    def end_of_day(self, sbalunce):
        sm = 0

        for i in self._list_items:
            for j in i.rep:
                delta = datetime.timedelta(hours=12)
                if j[0] >= datetime.datetime.now() - delta:
                    print(j[0],"\t\titem:",j[1],"\tprice:",j[2],"\toperation:",j[-1])
                    print()
                    sm += j[2]
        print("bulans:",sbalunce + sm)
        if sbalunce + sm == self._balance:
            print("Everything is fine")
        else:
            print("There are gaps")


lis = []
a = Item("a", 1, 10, 5)
b = Item("b", 1, 10, 5)
c = Item("c", 1, 10, 5)
d = Item("d", 1, 10, 5)
e = Item("e", 1, 10, 5)
lis.append(a)
lis.append(b)
lis.append(c)
lis.append(d)
lis.append(e)
roki = Shop(lis,100000)
roki.purchase(["a","a","a","a","a","b","b","a","a","c","a","d"],500)
roki.end_of_day(100000)
