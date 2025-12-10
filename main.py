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
    def __init__(self, product, qty):
        self.product = product
        self.qty = qty

    def total_prise(self):
        return self.product.price * self.qty

class OrderCatalog:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add(self, order):
        self.orders.append(order)

    def get_info(self):
        if not self.orders:
            return "Savat bo'sh"
        text = f'{self.name}\n'
        for o in self.orders:
            text += f"{o.product.name} - {o.qty}\n"
        return text

def find_product(name):
    for p in catalog.products:
        if p.name == name:
            return p
    return None
catalog = Catalog()
catalog.add(Product("olma", 10000, 2000))
catalog.add(Product("nok", 15000, 3000))
catalog.add(Product("guruch", 5000, 5000))


order_catalog = OrderCatalog("Rasmiylashtirilgan buyurtmalar")


def menu():
    while True:
        a = input("1.productlar\n2.savat\n3.exit\n>>> ")

        if a == "1":
            b = input("produkt qoshamizmi (ha yoki yo`q): ")
            if b == "ha":
                product1 =input("product nomi: ")
                product2 =int(input("product narxi: "))
                product3 = int(input("product qty: "))
                catalog.add(Product(product1, product2, product3))
                catalog.get_info()
            else:
                catalog.get_info()

        elif a == "2":
            catalog.get_info()
            name = input("qaysi mahsulotni qo`shamiz: ")

            product = find_product(name)

            if product is None:
                print("Mahsulot topilmadi!")
            else:
                qty = int(input("Nechta qo`shamiz: "))
                if qty <= product.qty:
                    order_catalog.add(Order(product, qty))
                    product.qty -=qty
                    print("Mahsulot savatga qo`shildi!")
                else:
                    print("Mahsulot yetarli emas!")

        elif a == "3":
            print("chiqish")
            break
menu()
