class Produkts:
    def __init__(self, name, price, qolgan):
        self.name = name
        self.price = price
        self.qolgan = qolgan

    def get_info(self):
        return f"Mahsulot nomi: {self.name}, narxi: {self.price} so'm, qolgan: {self.qolgan} ta"
