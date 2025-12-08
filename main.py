#menu
# 1.product list
# 2.productni pasmiylashtiradi
# 3.rasmiylashtirlgan narsalani ko`rish
# 4.exit

class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def get_info(self):
        return f"{self.name} - {self.price} so`m (qolgan: {self.qty} ta)"


class Catalog:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def get_info(self):
        print("\nRadius - Mahsulotlar:")
        for i in self.products:
            print(i.get_info())


class Order:
    orders = []
    def __init__(self, product, qty):
        self.product = product
        self.qty = qty
        Order.orders.append(self)

catalog = Catalog()
catalog.add(Product("olma", 10000, 2000))
catalog.add(Product("nok", 15000, 3000))
catalog.add(Product("guruch", 5000, 5000))


def menu():
    while True:
        a = input("1.productlar\n2.savat\n3.exit\n>>> ")

        if a == "1":
            b = input("produkt qoshamizmi (ha yoki yo`q): ")
            if b == "ha":
                catalog.get_info()   # ❗ print bilan emas!
            elif b == "":
                catalog.get_info()
                menu()
            elif b == "exit":
                pass
        elif a == "2":
            print("savat bo‘sh")
            menu()

        elif a == "3":
            print("chiqish")
            break
menu()
