class Catalog:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def get_info(self):
        print("\nRadius - Mahsulotlar:")
        for i in self.products:
            print(i.get_info())
